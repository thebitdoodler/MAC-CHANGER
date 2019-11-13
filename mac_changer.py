#!usr/bin/env python

import subprocess
import optparse


print("**\/**  ---  +++ ")
print("**  ** /   \ |   ")
print("**  ** *===* |   ")
print("**  ** *   * +++ CHANGER\n")
print("---------------------by 0x48iffy\n\n")




def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface", dest="interface", help="choose the wchich mac address to be changed")
	parser.add_option("-m","--mac", dest="new_mac", help="new MAC address to be assigned")
	(options,arguments)=parser.parse_args()
	if not options.interface:
		parser.error("[-] Please enter an interface, --help for more info")
	elif not options.new_mac:
		parser.error("[-] Please enter a new MAC adddress, --help for more info")
	return options

def change_mac(interface,new_mac):
	print("[+] Changing MAC adress for "+interface+ " to "+ new_mac)
	subprocess.call(["ifconfig", interface ,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])



options = get_arguments()
change_mac(options.interface, options.new_mac)


