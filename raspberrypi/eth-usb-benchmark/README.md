# Ethernet Throughput Benchmark

This document provides reference Ethernet throughput measurements for Raspberry Pi–based systems under different configurations.

The benchmark compares:

- **Raspberry Pi models**
- **native Ethernet interfaces**
- **USB Ethernet adapters**
- adapters connected **directly** or through a **USB hub**
- **single-interface** and **parallel dual-interface transfers**


## Test Method

- Up to two independent servers generate data in memory and stream it to the client.
- The client connects to one or two servers through different interfaces.
- For each interface, the client counts the total number of received bytes during the test.
- Throughput is reported as sustained **TCP bandwidth (Mbps)** measured on the client.


## Test Setup

Servers and clients run Raspberry Pi OS (64-bit), Linux kernel 6.12.

### Servers

The server generates a continuous TCP data stream.

| Device | Interface |
|--------|-----------|
| Raspberry Pi 5 | Native Gigabit Ethernet |

For parallel interface tests, two servers are used, each connected to a different client interface.

Benchmark script: [eth_speed_server.py](./eth_speed_server.py)

Usage:

```
sudo python3 eth_speed_server.py <INTERFACE> <SERVER_IP> [PORT]
```

The script configures the specified static IP address on the selected interface.

Example, two servers:

```
sudo python3 eth_speed_server.py eth0 10.55.1.1
```

```
sudo python3 eth_speed_server.py eth0 10.55.2.1
```

### Clients

The client device under test connects to one or two servers and measures the TCP bandwidth.

Benchmark script: [eth_speed_client.py](./eth_speed_client.py)

Usage:

```
sudo python3 eth_speed_client.py <IFACE:CLIENT_IP:SERVER_IP[:PORT]> [...] [STREAMS] [SECONDS]
```

The script configures the specified static IP address on each interface and uses multiple parallel TCP streams per interface to reach maximum throughput.

Example, single interface:

```
sudo python3 eth_speed_client.py eth0:10.55.1.2:10.55.1.1
```

Example, two interfaces:

```
sudo python3 eth_speed_client.py eth0:10.55.1.2:10.55.1.1 eth1:10.55.2.2:10.55.2.1
```

## Test Configurations

|    ID   | Connection                                                    |
| :-----: | ------------------------------------------------------------- |
|  `ETH`  | Direct Ethernet connection                                    |
|  `USB`  | Ethernet via USB Ethernet adapter                             |
|  `HUB`  | Ethernet via USB Ethernet adapter connected through a USB hub |
| `X`+`Y` | Parallel test with configurations `X` and `Y` from above      |

Ethernet cable: Cat 5e UTP

USB Ethernet adapter: USB 3.0 Gigabit Ethernet adapter

USB hub: 4-port USB 3.0 hub (self-powered)


## Results

All results were obtained using **4 TCP streams per interface for 10 seconds**.

Tests were performed on idle systems with no additional network traffic.

Results may vary depending on system load, USB devices, kernel version, and adapter chipset.

### Strato Pi Max with CM5

Interfaces:
- LAN1: Native Gigabit Ethernet
- LAN2: 10/100 Ethernet via LAN9514 USB-to-Ethernet bridge
- USB1, USB2: USB 2.0 via LAN9514 USB hub

| Configuration | Interface(s) | Throughput (Mbps)   |
| :-----------: | ------------ | ------------------- |
|     `ETH`     | LAN1         | 936.46              |
|     `ETH`     | LAN2         | 93.65               |
|  `ETH`+`ETH`  | LAN1 + LAN2  | 936.45 + 93.65      |
|     `USB`     | USB1         | 333.62              |
|     `HUB`     | USB1         | 321.79              |
|  `ETH`+`USB`  | LAN1 + USB1  | 936.44 + 333.13     |
|  `ETH`+`USB`  | LAN2 + USB1  | 73.59 + 266.71      |

### Raspberry Pi 5

Interfaces:
- LAN: Gigabit Ethernet
- USB1, USB2: USB 2.0
- USB3, USB4: USB 3.0

| Configuration | Interface(s) | Throughput (Mbps)   |
| :-----------: | ------------ | ------------------- |
|     `ETH`     | LAN          | TODO                |
|     `USB`     | USB1         | TODO                |
|     `USB`     | USB3         | TODO                |
|  `ETH`+`USB`  | LAN + USB1   | TODO                |
|  `ETH`+`USB`  | LAN + USB3   | TODO                |
