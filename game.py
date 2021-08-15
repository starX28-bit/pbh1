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

os.system("toilet -f future PBH TOOLS | lolcat")
print "                        v1.0"
print ""
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
print white,"[4] INSTALL SQLMAP"
print red,"[5] INSTALL NMAP"
print white,"[6] INSTALL BAHAN "
print red,"[7] INSTALL WEBDAV "
print white,"[8] INFO AUTHOR"
print red,"[9] EXIT"

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
  os.system("git clone https://github.com/anouarbensaad/vulnx")
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
  
elif name ==4:
  os.system("clear")
  os.system("figlet star")
  os.system("pkg install git")
  os.system("pkg install python2")
  os.system("git clone https://github.com/sqlmapproject/sqlmap")
  os.system("cd sqlmap")
  os.system("ls")
  os.system("python2 sqlmap.py")
  
elif name ==5:
  os.system("pkg install nmap")
  os.system("figlet succes")
  
elif name ==6:
  os.system("pkg install git")
  os.system("pkg install php")
  os.system("pkg install python2")
  os.system("pkg install python2")
  os.system("pkg install ruby")
  os.system("pkg install figlet")
  os.system("gem install lolcat")
  
elif name ==7:
  os.sysytem("git clone https://github.com/B41B4L/WEBDAV")
  os.system("cd WEBDAV")
  os.system("ls")
  os.system("bash bahan.sh")
  os.system("sh dev.sh")
  
elif name ==8:
  os.system("clear")
  print purple,"========================"
  print cyan,"AUTHOR : starX "
  print purple,"TEAM   : PADANG BLACKHAT"
  print cyan,"GITHUB : github/starX28"
  print purple,"========================"

elif name ==9:
  os.system("figlet oke ker")
  

else:
  print "your input not found"


        









  

