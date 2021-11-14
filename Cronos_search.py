import subprocess
from os import system
import os


os.system("color 0A")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒")
print("▒▒█▒▒▒▄██████████▄▒▒▒▒")
print("▒█▐▒▒▒████████████▒▒▒▒")
print("▒▌▐▒▒██▄▀██████▀▄██▒▒▒")
print("▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒")
print("▐┼▐▒▒██████████████▒▒▒")
print("▐▄▐████─▀▐▐▀█─█─▌▐██▄▒")
print("▒▒█████───PITER──▐███▌")
print("▒▒█▀▀██▄█─▄───▐─▄███▀▒")
print("▒▒█▒▒███████▄██████▒▒▒")
print("▒▒▒▒▒██████████████▒▒▒")
print("▒▒▒▒▒██████████████▒▒▒")
print("▒▒▒▒▒█████████▐▌██▌▒▒▒")
print("▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")


#os.system("shodan init 2E7JoDWBjIej37P6sCUhd1MKTtF73Rlo")
while True:
    print("1-> Dispositivos vulnerables ADB")
    print("CARGANDO...")
    os.system("shodan search --fields ip_str,port,org,android debug bridge")
    o = input("Para salir escriba [exit], Para reintentar [Enter]-> ")
    while o == "exit":
    	print("Saliendo")
