#!/usr/bin/env python3
import socket
import sys
import threading
import time
import subprocess

PORT = 5001
IP_SERVER = "10.55.0.1"
IP_CLIENT = "10.55.0.2"

iface = sys.argv[1]
streams = int(sys.argv[2]) if len(sys.argv)>2 else 4
duration = int(sys.argv[3]) if len(sys.argv)>3 else 10

subprocess.run(["ip","addr","flush","dev",iface],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
subprocess.run(["ip","addr","add",IP_CLIENT+"/24","dev",iface])
subprocess.run(["ip","link","set",iface,"up"])

print("Interface",iface,"configured with",IP_CLIENT)

total = 0
lock = threading.Lock()
stop = False

def worker():
    global total
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,25,iface.encode())
    s.connect((IP_SERVER,PORT))
    while not stop:
        data = s.recv(1024*256)
        if not data:
            break
        with lock:
            total += len(data)

threads=[]

for _ in range(streams):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

start=time.time()
last=start
last_bytes=0

while time.time()-start < duration:
    time.sleep(1)

    with lock:
        now_bytes = total

    now=time.time()
    delta=now-last
    rate=(now_bytes-last_bytes)*8/delta/1e6

    print("Current:",round(rate,1),"Mbps")

    last=now
    last_bytes=now_bytes

stop=True

for t in threads:
    t.join()

elapsed=time.time()-start
mbps=(total*8)/elapsed/1e6

print()
print("Total received:",total,"bytes")
print("Average speed:",round(mbps,2),"Mbps")
