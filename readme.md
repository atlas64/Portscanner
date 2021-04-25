# Portscanner
> Network portscanner with threading. Can scan a range of IP addresses and output any open ports matched up with any well known ports.

![](header.png)

## To Run
```sh
python3 portscanner.py
```
You will be asked for the network address, what host to start the scan on, and what host to stop on. The script will then check all possible open ports, and provide you with the service running on it if it is within the well known range.
