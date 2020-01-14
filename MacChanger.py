#!/bin/bash
import subprocess
import random

MacAddresses = ["fc:08:77:b2:c0:8e","fc:22:9c:00:09:7c","fc:17:94:08:00:46","f8:e4:fb:00:07:0e","f8:e4:fb:00:00:8f"]

MacAddresse = random.randrange(0,4)

interfaceName = input("The Name of Your Interface ( write ifconfig to get it ) : ")
subprocess.call(["sudo","ifconfig",interfaceName,"down"])
subprocess.call(["sudo","service","network-manager","stop"])
subprocess.call(["sudo","ifconfig",interfaceName,"hw","ether",MacAddresses[MacAddresse]])
subprocess.call(["sudo","ifconfig",interfaceName,"up"])
subprocess.call(["sudo","service","network-manager","start"])

#By Fayz Sabir