from pwn import log
import os
import sys
import platform
import socket 
from requests import get
import sys

"""
if sys.platform != "linux":
	os.system("cls")
else:
	os.system("clear")"""
	
banner="""
  ____ _               _    _                         
 / ___| |__   ___  ___| | _(_)_ __   __ _             
| |   | '_ \ / _ \/ __| |/ / | '_ \ / _` |            
| |___| | | |  __/ (__|   <| | | | | (_| |  _   _   _ 
 \____|_| |_|\___|\___|_|\_\_|_| |_|\__, | (_) (_) (_)
                                    |___/      """
                                    
def get_local_ip():
    import socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))

        return sock.getsockname()[0]
    except socket.error:
        try:
            return socket.gethostbyname(socket.gethostname())
        except socket.gaierror:
            return '127.0.0.1'
    finally:
        sock.close() 
                                    

print(banner)

log.info("Checking starting")
log.info("Local ip: "+get_local_ip())
def pub_ip():
	ip = get('https://api.ipify.org').content.decode('utf8')
	log.info('Your public ip is: {}'.format(ip))
def pubyt():
	log.progress("Checking your public ip address")
	pub_ip()
pubyt()
user= os.getlogin()
user = str(user)
log.info("User: "+user)

hostname = platform.node()
hostname = str(hostname)
log.info("Hostname: "+hostname)

opersys = platform.system()
opersys = str(opersys)
log.info("Operating System: "+opersys)

release = platform.release()
release = str(release)
log.info("Release: "+release)

bit = platform.machine()
bit = str(bit)
log.info("Bit: "+bit)

plat = platform.platform()
plat = str(plat)
log.info("Platform: "+plat)

dir = os.getcwd()
dir = str(dir)
log.info("Dir: "+dir)

version = sys.version
log.info("Python Version: "+version)

progressor = platform.processor()
progressor = str(progressor)
log.info("CPU: "+progressor)



def find_service_name(): 
    protocolname = 'tcp' 
    for port in [80, 25]: 
        print ("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))) 
     
    print ("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))) 
     
#if __name__ == '__main__': 
#    find_service_name() 
log.info("finding service")
find_service_name()