#########################################################################
#
#               Script by @TK109  script version: vß0.2.3
#
#########################################################################



import os
import time
import pyttsx3
import colorama
import pyautogui
import wikipedia
import pywhatkit
import subprocess
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
voices = tts.getProperty('voices')       # Configurando la voz
tts.setProperty('voice', voices[0].id)   # Configurando la voz




# Función para pasar la respuesta de texto a voz
def answer(text):
    global prompt
    #global prompt_as_list

    prompt = f"{lblue}{blod}$ {reset}"    # Prompt del input
    #prompt_as_list = list("$"," ")    # Prompt del input como lista

    print(prompt + text)
    tts.say(text)
    tts.runAndWait()


# Lambda para transcribir el audio
transcript = lambda text: print(prompt + text)



try:
    print(f"{green}{blod}[{lgreen}{blod}+{green}{blod}] {white}{blod}Aplicación iniciada y en escucha...{reset}")
    tts.say("Aplicación iniciada y en escucha...")
    tts.runAndWait()

    while True:
        with sr.Microphone() as micro:
            listener.adjust_for_ambient_noise(micro, duration=1)    # Eliminación del ruido de fondo
            voice = listener.listen(micro)
            rec = listener.recognize_google(voice, language='es-ES', show_all=True)
            rec = str(rec)
            
            # Saludos
            try:
                if rec == "Zyrox" or "cirox" or "cyrox" or "ciros":
                    print(transcript(rec))
                    answer("Aquí estoy.")

                elif "Zyrox, estás " or "cirox, estás " or "cyrox, estás " or "ciros, estás " in rec:
                    answer("¡Claro!, ¿que quieres?")


            except sr.UnknownValueError:
                print(f"{red}{blod}[{lred}{blod}x{red}{blod}] {white}{blod}No se pudo reconocer el audio")
                answer("No te he entendido")


            # Cosos de GitHub
            try:
                if rec == "Abre" or "Abreme" + "GitHub" or "gitjub":
                    webbrowser.open('https://github.com/')

                if "Abre" or "Abreme" + "el repositorio" or "el repo" + "de":
                    repo = rec.replace('el repo' or "el repositorio", '')
                    user = rec.replace('de', '')
                    answer("Abriendo " + repo + user)
                    webbrowser.open('https://github.com')

            except sr.UnknownValueError:
                print(f"{red}{blod}[{lred}{blod}x{red}{blod}] {white}{blod}No te entendí.")
                answer("No te entendí")


            # Abrir una consola
            try:
                if rec == "Abre" or "Abreme" + "una CMD" or "una cmd":
                    answer("Abriendo CMD en directorio home")
                    os.system('start cmd')

                if rec == "Abre" or "Abreme" + "una POWERSHELL" or "una powershell" or "una POUERSEL" or "una pouersel":
                    answer("Abriendo POWERSHELL en directorio home")
                    os.system('start powershell')

            except sr.UnknownValueError:
                print(f"{red}{blod}[{lred}{blod}x{red}{blod}] {white}{blod}No te entendí.")
                answer("No te entendí")



except KeyboardInterrupt:
    print(f"{yellow}[{lyellow}!{yellow}] {white}Saliendo...")
    exit()

except sr.RequestError as e:
    print(e)

""" except sr.UnknownValueError:
    print(f"{red}{blod}[{lred}{blod}x{red}{blod}] {white}{blod}No se pudo reconocer el audio")
    exit() """


