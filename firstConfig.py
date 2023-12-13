import os
import colorama
from colorama import Fore, init


# Variables necesarias

# Colores
init()  # Inicializamos la libreria

# Definimos los colores

red = Fore.RED
lred = Fore.LIGHTRED_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
reset = Fore.RESET
blod = '\033[1m'


print(f"{blod}{green}[{lgreen}+{green}] {white}Starting instalation...{reset}\n")

print(f"\t{blod}{green}[{lgreen}+{green}] {white}Updating and upgrading instalation methods\n")
os.system('sudo apt update && sudo apt upgrade || pacman -Syu && pip install --upgrade pip & pip3 install --upgrade pip3')  # Update and upgrade instalation methods
os.system('pip install -r requirements.txt || pip3 install -r requirements.txt')    # Install dependencies and libraries


