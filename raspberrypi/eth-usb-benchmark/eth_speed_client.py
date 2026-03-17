#!/usr/bin/env python3
import socket
import sys
import threading
import time
import subprocess

DEFAULT_PORT = 5001
CHUNK = 1024 * 256

args = sys.argv[1:]

streams = 4
duration = 10

# Parse optional trailing args: [streams] [duration]
if len(args) >= 1 and args[-1].isdigit():
    duration = int(args[-1])
    args = args[:-1]

if len(args) >= 1 and args[-1].isdigit():
    streams = int(args[-1])
    args = args[:-1]

if not args:
    print("Usage:")
    print("  eth_speed_client.py <iface:client_ip:server_ip[:port]> [...] [streams] [seconds]")
    sys.exit(1)

# Parse interface configs
interfaces = []
for cfg in args:
    parts = cfg.split(":")
    if len(parts) < 3:
        raise ValueError("Invalid config: " + cfg)

    iface = parts[0]
    ip_client = parts[1]
    ip_server = parts[2]
    port = int(parts[3]) if len(parts) > 3 else DEFAULT_PORT

    interfaces.append((iface, ip_client, ip_server, port))

totals = {iface: 0 for iface, _, _, _ in interfaces}
locks = {iface: threading.Lock() for iface, _, _, _ in interfaces}
stops = {iface: False for iface, _, _, _ in interfaces}

# Configure interfaces
for iface, ip_client, ip_server, port in interfaces:
    subprocess.run(["ip","addr","flush","dev",iface], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["ip","addr","add",ip_client+"/24","dev",iface])
    subprocess.run(["ip","link","set",iface,"up"])
    print(f"Interface {iface} configured with {ip_client} -> {ip_server} port {port}")

# Connection sync
connect_count = 0
connect_lock = threading.Lock()
connect_event = threading.Event()
expected = len(interfaces) * streams

def worker(iface, ip_server, port):
    global connect_count

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, 25, iface.encode())
    s.connect((ip_server, port))

    with connect_lock:
        connect_count += 1
        if connect_count == expected:
            connect_event.set()

    while not stops[iface]:
        data = s.recv(CHUNK)
        if not data:
            break
        with locks[iface]:
            totals[iface] += len(data)

threads = []

for iface, _, ip_server, port in interfaces:
    for _ in range(streams):
        t = threading.Thread(target=worker, args=(iface, ip_server, port))
        t.start()
        threads.append(t)

connect_event.wait()

# Warm-up (ignored)
time.sleep(1)

# Reset counters
for iface in totals:
    totals[iface] = 0

last = time.monotonic()
last_bytes = {iface: 0 for iface in totals}

samples = {iface: [] for iface in totals}
samples_total = []

start = last

# Measurement loop
while time.monotonic() - start < duration:
    time.sleep(1)

    now = time.monotonic()
    delta = now - last

    total_rate = 0
    per_iface_rate = {}

    for iface in totals:
        with locks[iface]:
            now_bytes = totals[iface]

        rate = (now_bytes - last_bytes[iface]) * 8 / delta / 1e6
        per_iface_rate[iface] = rate
        total_rate += rate

        last_bytes[iface] = now_bytes

    for iface in totals:
        samples[iface].append(per_iface_rate[iface])
        print(f"{iface}: {per_iface_rate[iface]:.1f} Mbps", end="  ")

    samples_total.append(total_rate)
    print(f"| Total: {total_rate:.1f} Mbps")

    last = now

# Stop workers
for iface in stops:
    stops[iface] = True

for t in threads:
    t.join()

print("\nFinal results:")

grand_total = 0

for iface in samples:
    avg = sum(samples[iface]) / len(samples[iface]) if samples[iface] else 0
    grand_total += avg
    print(f"{iface}: {avg:.2f} Mbps")

total_avg = sum(samples_total) / len(samples_total) if samples_total else 0
print(f"Total: {total_avg:.2f} Mbps")
