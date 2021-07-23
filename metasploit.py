import os

os.system("clear")

print("#########################")
print("                         ")
print("Mrpleak Metasploit Kurucu")
print("                         ")
print("#########################")
print()

print("1.Metasploit")

veri = input("İşlem :")

if veri =="4":
	x =input("Metasploit açılcaktır Enter'a basınız")
	os.system("pkg update && pkg upgrade -y &&pkg install postgresql && pkg install openssh wget curl git -y && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh && chmod +x  metasploit.sh && ./metasploit.sh")
	os.system("msfconsole")
