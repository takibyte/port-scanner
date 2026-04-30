#!/usr/bin/env python3
"""

A simple port scanner utilising the python socket module.

"""

import socket

def display_host():
    hostname = socket.gethostname()
    ip = socket.gethostbyname("localhost")

    print(f"Hostname: {hostname}")
    print(f"IP: {ip}")

display_host() 




def scan_port():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)


    return


#with socket.socket(family=AF_INET, type=SOCK_STREAM) as s:
    