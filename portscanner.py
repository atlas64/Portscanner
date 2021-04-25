#!/usr/bin/python3
#title           :portscanner.py
#description     :threaded network port scanner, can scan range of addresses
#author          :atl4s
#date            :4/25/21
#python_version  :3.7.9   
#==============================================================================


import sys
import socket
import time
from threading import Thread 

st1 = ""
en1 = ""
net2 = ""
threads = []

#take in network address and range 
def takeinput():
	global st1
	global en1
	global net2

	print("-" * 50)
	print("		Network Port Scanner")
	net = input("->Network address: ")
	net1 = net.split('.')
	a = '.'
	net2 = net1[0] + a + net1[1] + a + net1[2] + a
	st1 = int(input("->Begin scanning at: "))
	en1 = int(input("->End scanning at: "))
	en1 = en1 + 1
	localtime = time.asctime( time.localtime(time.time()) )
	print ("Scan started :", localtime)

#create socket and tcp connection
def portscan(start, end, ip):
	s = int(start)
	e = int(end)
	try:
		for port in range(s, e):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			openports = sock.connect_ex((ip, port))
			if openports == 0:
				print("[*]Port {}: Open".format(port))
				servname = socket.getservbyport(port)
				print("Running {} services\n".format(servname))
			sock.close()
	except KeyboardInterrupt:
		print("\nQutting program...")
		sys.exit()
	except socket.gaierror:
		print("\nHostname could not be resolved...")
	except socket.error:
		print("Running unknown services\n")
		pass

#threading the portscans to run in parallel 
def threader(ip):
	tno = 2000
	for x in range(tno):
		if((x+1)*(65536/tno)<=65536):
			th = Thread(target = portscan, args = (x*(65536/tno), (x+1)*(65536/tno), ip))
		else:
			th = Thread(target = portscan, args = (x*(65536/tno), 65536, ip))			
		th.start()
		threads.append(th)
	for x in threads:
		x.join()

#iterating port scans through provided range
def netscan(st1, en1):
	for ip in range(st1, en1):
		addr = net2 + str(ip)
		print("-" * 50)
		print("| " + addr + " |")
		print("-" * 50)
		threader(addr)

def main():
	takeinput()
	netscan(st1, en1)

if __name__ == "__main__":
	main()
