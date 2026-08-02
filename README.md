# pscan

This is a simple multi-threaded port scanner written in Python. It allows you to scan a range of ports on a specified host to check which ports are open.

```
usage: pscan [-h] [--start START] [--end END] [host]

A simple port scanner

positional arguments:
  host           hostname or IPv4 address

options:
  -h, --help     show this help message and exit
  --start START  start of the port range to be scanned
  --end END      end of the port range to be scanned

example usage: 
python3 pscan.py --start 1 --end 1024 example.com
```