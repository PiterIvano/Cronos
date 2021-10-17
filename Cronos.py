import subprocess
from os import system
import os


os.system("color 0A")
while True:
    print("Opciones relevantes:")
    print("1-> Conectar dispositivo")
    print("2-> Abrir shell")
    print("3-> Ver dispositivos conectados")
    print("4-> Desconectar Dispositivo")
    print("5-> Tomar captura de pantalla")
    print("6-> Mover captura al PC")
    print("7-> Ver Paquetes instalados")
    print("8-> Ver interfaz Grafica")
    print("9-> Reiniciar ADB")

    option = int(input("Ponga su opcion aqui-> "))

    if(option == 1):
        ips = input("Escriba su ip aqui-> ")
        ip = os.system(f"adb connect {ips}")
    elif(option == 2):
        ip = os.system(f"adb shell")
    elif(option == 3):
        ip = os.system(f"adb devices")
    elif(option == 4):
        ips = input("Escriba su ip aqui-> ")
        ip = os.system(f"adb disconnect {ips}")
    elif(option == 5):
        ip = os.system("adb shell screencap -p /sdcard/piter.png")
    elif(option == 6):
        print("/users/Piter/Downloads -> ejemplo")
        cap = input("poner direccion destino -> ")
        ip = os.system(f">adb pull /sdcard/piter.png {cap}")
    elif(option == 7):
        ip = os.system("adb shell pm list packages")
    elif(option == 8):
        ip = os.system("start scrcpy.exe")
    elif(option == 9):
        ip = os.system("adb kill-server")
