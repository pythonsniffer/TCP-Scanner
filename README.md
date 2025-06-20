# TCP-Scanner
Built a custom Python-based TCP port scanner to identify open ports on a given host.
A lightweight multithreaded TCP port scanner written in Python, featuring:
- Custom port range input
- Timeout handling
- Banner grabbing
---

## Features

- Scan any host or IP address across custom port ranges
- Displays open ports and grabs banners (if available)
- Configurable timeout and thread limits
- Efficient multithreaded scanning 

---

## Usage

```bash
python scanner.py --target <IP or hostname> --start <start_port> --end <end_port> --timeout <seconds> 
