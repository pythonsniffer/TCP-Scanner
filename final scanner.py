import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def port_scan(target, port, timeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "No banner received"
            print(f"[+] Port {port} is OPEN | Banner: {banner}")
        s.close()
    except:
        pass

parser = argparse.ArgumentParser(description="Simple Python Port Scanner with Banner Grabbing")
parser.add_argument("--target", required=True, help="Target IP or hostname")
parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
parser.add_argument("--timeout", type=float, default=1.0, help="Socket timeout in seconds (default: 1.0)")

args = parser.parse_args()
target = args.target
start_port = args.start
end_port = args.end
timeout = args.timeout

print(f"\n[~] Scanning {target} from port {start_port} to {end_port} \n")


with ThreadPoolExecutor(max_workers=1000) as executor:
    for port in range(start_port, end_port + 1):
        executor.submit(port_scan, target, port, timeout)

print("\n[✔] Scan Complete")
