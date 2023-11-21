#########################################################################
#
#               Script by @TK109  script version: vß0.2
#
#########################################################################



import os
import time
import pyttsx3
import colorama
import pyautogui
import wikipedia
import webbrowser
import speech_recognition as sr

from os import *
from time import sleep
from colorama import Fore, init



# Variables necesarios

init()  # Inicialización libreria colorama
# Colores de colorama
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

# Activamos reconocimiento de voz
listener = sr.Recognizer()

# Configuración del motor tts
tts = pyttsx3.init()    # Inicialización
voces = tts.getProperty('voices')
tts.setProperty('voice', voces[0].id)


# Condición para la escucha (que esté su nombre en la oración)
zyrox = "Zyrox"




def respuesta(texto):
    global prompt
    global prompt_as_list
    prompt = f"{lblue}{blod}$ {reset}"  # Prompt del input
    prompt_as_list = list("$"," ")
    print(prompt + texto)
    tts.say(texto)
    tts.runAndWait()


try:
    while True:
        print(f"{green}{blod}[{lgreen}{blod}+{green}{blod}] {white}{blod}Aplicación iniciada y en escucha...{reset}")
        tts.say("Aplicación iniciada y en escucha...")
        tts.runAndWait()
        with sr.Microphone() as micro:
            voz = listener.listen(micro)
            grabacion = listener.recognize_google(voz)
            grabacion = grabacion.lower()
            if zyrox in grabacion:
                respuesta(grabacion)


except KeyboardInterrupt:
    print(f"{yellow}[{lyellow}!{yellow}] {white}Saliendo...")
    quit()

except:
    print(f"{red}{blod}[{lred}{blod}x{red}{blod}] {white}{blod}Hubo un error, saliendo...")

