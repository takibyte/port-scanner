#!/usr/bin/env python3
"""
A simple port scanner utilising the python socket module.

"""

import socket

def scan_port(host, port):
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        try:
            s.settimeout(1)
            result = s.connect_ex((host, port))

            return result == 0
        
        except socket.timeout:
            print("Error: The scan has timed out.")
            return False
        
        except socket.gaierror:
            print("Error: The host couldn't resolve.")
            return False

if scan_port("localhost", 22):
    print("port open")
else:
    print("port closed")


    