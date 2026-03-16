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
sudo python3 eth_speed_server.py eth0
```

The script automatically configures the static IP address `10.55.0.1`.

### Clients

The client device under test connects to one or two servers and measures the TCP bandwidth.

Benchmark script: [eth_speed_client.py](./eth_speed_client.py)

Usage:

```
sudo python3 eth_speed_client.py <INTERFACE> <STREAMS> <SECONDS>
```

The script automatically configures the static IP address `10.55.0.2` and uses multiple parallel TCP streams to reach maximum throughput.


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

All results were obtained using **4 TCP streams for 10 seconds** per interface.

Tests were performed on idle systems with no additional network traffic.

Results may vary depending on system load, USB devices, kernel version, and adapter chipset.

### Raspberry Pi 5

| Configuration | Interface(s)               | Throughput (Mbps) |
| :-----------: | -------------------------- | ----------------- |
|     `ETH`     | Gigabit Ethernet           | TODO              |
|     `USB`     | USB 2.0                    | TODO              |
|     `USB`     | USB 3.0                    | TODO              |
|  `ETH`+`USB`  | Gigabit Ethernet + USB 3.0 | TODO + TODO       |

### Strato Pi Max with CM5

| Configuration | Interface(s)            | Throughput (Mbps) |
| :-----------: | ----------------------- | ----------------- |
|     `ETH`     | LAN1 (Gigabit Ethernet) | 936               |
|     `ETH`     | LAN2 (10/100 Ethernet)  | 93.5              |
|     `USB`     | USB1 (USB 2.0)          | 93.5              |
|     `HUB`     | USB1 (USB 2.0)          | 93.5              |
|  `ETH`+`USB`  | LAN1 + USB1             | TODO + TODO       |
