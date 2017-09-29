#!/usr/local/bin/python3.6
import socket
import struct

def cidr_to_netmask(cidr):
	"""
	Converts CIDR to netmask
	Usage
	cidr_to_netmask('10.10.1.32/27')
	Returns:
	('10.10.1.32', '255.255.255.224')
	"""
	network, net_bits = cidr.split('/')
	host_bits = 32 - int(net_bits)
	netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
	return network, netmask
