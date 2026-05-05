#!/usr/bin/env python3
"""
A simple port scanner utilising the python socket module.

"""

import argparse
import socket
import threading
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser(
    prog="portscanner",
    description="A simple port scanner")


def valid_port(value):
    port = int(value)
    if not (0 <= port <= 65535):
        raise argparse.ArgumentTypeError(f"{value} is not a valid port, valid range is: 0-65535")
    return port


parser.add_argument('host', type=str, nargs='?', help='hostname or IPv4 address')
parser.add_argument('--start', type=valid_port, default=0, help='start of the port range to be scanned')
parser.add_argument('--end', type=valid_port, default=1001, help='end of the port range to be scanned')
args = parser.parse_args()


hostname = args.host
ports = range(args.start, args.end)

print_lock = threading.Lock()

def scan_port(host, port):
    try:
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
            s.settimeout(1)

            result = s.connect_ex((host, port))

            with print_lock:
                if result == 0:
                    print(f"Open port: {port}", end=" - ")
                    try:
                        print(socket.getservbyport(port))
                    except OSError:
                        print("Error: Service not known.")

        return
    
    except socket.timeout:
        print("Error: The scan has timed out.")
        return False
    
    except socket.gaierror:
        print("Error: The host couldn't resolve.")
        return False
    

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(lambda port : scan_port(hostname, port), ports)


