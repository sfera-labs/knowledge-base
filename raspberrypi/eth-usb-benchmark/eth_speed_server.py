#!/usr/bin/env python3
import socket
import sys
import threading
import os
import subprocess

DEFAULT_PORT = 5001
CHUNK = 1024 * 256

args = sys.argv[1:]

if len(args) < 2:
    print("Usage:")
    print("  eth_speed_server.py <iface> <server_ip> [port]")
    sys.exit(1)

iface = args[0]
ip_server = args[1]
port = int(args[2]) if len(args) > 2 else DEFAULT_PORT

# Configure interface
subprocess.run(["ip","addr","flush","dev",iface], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(["ip","addr","add",ip_server+"/24","dev",iface])
subprocess.run(["ip","link","set",iface,"up"])

print(f"Interface {iface} configured with {ip_server}")

def handle(conn):
    buf = os.urandom(CHUNK)
    try:
        while True:
            conn.sendall(buf)
    except:
        pass
    finally:
        conn.close()

# Create server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((ip_server, port))
s.listen()

print(f"Server ready on {ip_server} port {port}")

while True:
    conn, _ = s.accept()
    t = threading.Thread(target=handle, args=(conn,))
    t.daemon = True
    t.start()
