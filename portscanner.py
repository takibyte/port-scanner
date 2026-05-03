#!/usr/bin/env python3
"""
A simple port scanner utilising the python socket module.

"""

import socket

def scan_port_range(host, start_port, end_port):
    try:
        for i in range(start_port, end_port + 1):
            with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
                s.settimeout(1)

                result = s.connect_ex((host, i))
                if result == 0:
                    print(f"Open port: {i}", end=" - ")
                    try:
                        print(socket.getservbyport(i))
                    except OSError:
                        print("Error: Service not known.")

        return
    
    except socket.timeout:
        print("Error: The scan has timed out.")
        return False
    
    except socket.gaierror:
        print("Error: The host couldn't resolve.")
        return False

scan_port_range("localhost", 0, 100)

