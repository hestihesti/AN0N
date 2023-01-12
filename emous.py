import os
import sys
import time
from termcolor import colored
import pyfiglet


def hide():
	ascii_banner = pyfiglet.figlet_format(' EMOUS')
	print(ascii_banner)
	i = 0
	while i < 5:
		i += 1
		if i == 1:
			nord = 'nordvpn connect'
			os.system(nord)
			print(colored('NordVPN Has Started', 'green'))

		if i == 2:
			tor = 'service tor start'
			os.system(tor)
			print(colored('TOR Relays Have Started', 'green'))

		if i == 3:
			servSTOP = 'service NetworkManager stop'
			ifconDOWN = 'ifconfig wlan0 down'
			macChng = 'macchanger -r wlan0'
			macChng2 = 'macchanger -r eth0'
			ifconUP = 'ifconfig wlan0 up'
			servSTART = 'service NetworkManager start'

			os.system(servSTOP)
			os.system(ifconDOWN)
			os.system(macChng)
			os.system(macChng2)
			os.system(ifconUP)
			os.system(servSTART)
			print(colored('Your MAC Address Has Been Spoofed', 'green'))

		if i == 4:
			prxychn = 'proxychains'
			os.system(prxychn)
			cat = 'cat /etc/proxychains.conf'
			os.system(cat)

		if i == 5:
			print(colored('You Are Now Secure', 'yellow'))

		else:
			print(colored('. . . ', 'red'))



hide()
