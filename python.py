from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jinja2 import Template
import yaml
import sys

junos_hosts = ['vMX1','vMX2']
for host in junos_hosts:
	try:
		myFile = host + '.yml'
		with open(myFile,'r') as fh:
			data = yaml.load(fh.read())
		with open('case1.j2','r') as t_fh:
			t_format = t_fh.read()
			