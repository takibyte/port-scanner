# port-scanner

This is a simple multi-threaded port scanner written in Python. It allows you to scan a range of ports on a specified host to check which ports are open.

```
usage: portscanner [-h] [--start START] [--end END] [host]

positional arguments:
  host           hostname or IPv4 address

options:

-h, --help     show help message and exit

--start START  start of the port range to be scanned

--end END      end of the port range to be scanned


example usage:
  python3 portscanner.py --start 0 --end 1000 example.com
```