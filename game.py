import os
import time
import sys
import random

blue ='\033[34;1m'
green ='\033[32;1m'
purple ='\033[35;1m'
cyan ='\033[36;1m'
red ='\033[31;1m'
white ='\033[37;1m'
yellow ='\033[33;1m'


        
os.system("clear")

os.system("toilet PBH TOOLS | lolcat")
print red,"__________________________"
print ""
print white, "AUTHOR : starX"

print red, "TEAM   : PADANG BLACKHAT "
print white,"__________________________" 
print ""

print red,"LIST "
print white,"    TOOLS"
print ""
print red,"[1] TOOLS SPAMMER "
print white,"[2] TOOLS WEBSITE SCAN"
print red,"[3] TOOLS ADMIN FINDER"
print ""
name = input("[?]masukkan keyword: ")

if name ==1:
  os.system("apt update")
  os.system("apt upgrade")
  os.system("pkg install git")
  os.system("pkg install php")
  os.system("git clone https://github.com/MrErroer/FCTspammer")
  os.system("figlet succes")

  
elif name ==2:
  os.system("clear")
  os.system("pkg install php")
  os.system("pkg install git")
  os.system("git https://github.com/anouarbensaad/vulnx")
  os.system("cd vulnx")
  os.system("chmod +x install.sh")
  os.system("./install.sh")

elif name ==3:
  os.system("clear")
  os.system("pkg install python2")
  os.system("pkg install git")
  os.system("git clone  https://github.com/the-c0d3r/admin-finder.git")
  os.system("cd admin-finder")
  os.system("python2 admin-finder.py")
else:
  print "your input not found"
