#!/usr/bin/env python3
import socket
import threading
import os
import sys
import subprocess

PORT = 5001
CHUNK = 1024 * 256
IP_SERVER = "10.55.0.1"
IP_CLIENT = "10.55.0.2"

iface = sys.argv[1]

subprocess.run(["ip","addr","flush","dev",iface],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
subprocess.run(["ip","addr","add",IP_SERVER+"/24","dev",iface])
subprocess.run(["ip","link","set",iface,"up"])

print("Interface",iface,"configured with",IP_SERVER)

def handle(conn):
    try:
        buf = os.urandom(CHUNK)
        while True:
            conn.sendall(buf)
    except:
        pass
    conn.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((IP_SERVER,PORT))
s.listen()

print("Server ready")

while True:
    conn,addr = s.accept()
    threading.Thread(target=handle,args=(conn,),daemon=True).start()
