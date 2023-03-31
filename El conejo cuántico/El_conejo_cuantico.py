import colorama
import time
from random import randint
import os


colorama.init()

file = open("./texto/titulo.txt","r")
char = ''
showtext = file.readline()



MAGENTA = colorama.Fore.MAGENTA
RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW
CYAN = colorama.Fore.CYAN
GREEN = colorama.Fore.GREEN
color = None

chose_color = {
    1: MAGENTA, 
    2: RED,
    3: YELLOW,
    4: CYAN,
    }

chose_casa = {
    'A': "./texto/A_Escena_casa.txt",
    'B': "./texto/B_Escena_casa.txt",
    'C': "./texto/C_Escena_casa.txt",
    'D': "./texto/D_Escena_casa.txt",
    'E': "./texto/Comes.txt",
}

chose_comes = {
    'A': "./texto/Comes.txt",
    'B': "./texto/guardas.txt",
}

chose_ir = {
    'A': "./texto/conejos.txt",
    'B': "./texto/seres.txt",
    'E': "./texto/Comes.txt",
}

chose_number = {
    '73': "./texto/numero.txt",
    '^(?!73)\d+$': "./texto/tarta.txt",
    'E': "./texto/Comes.txt",
}

titulo = {
    1: "./texto/titulo.txt",
    2: "./texto/GAME_OVER.TXT",
    3: "./texto/WIN.TXT",
}
global escena
escena = {
    1: chose_casa,
    2: chose_ir,
    3: chose_number,
    4: chose_comes,
}




mal = "./texto/mal.txt"
tarta = "./texto/tarta.txt"

comida = 0
nota = 0
velo = 0.03
veloT = 2
up = 0
menu = None

def clear():
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear')
def showtitulo(marque):
    clear()
    global titulo, veloT
    file = open(titulo.get(marque),"r",  encoding='utf-8')
    showtext = file.readline()
    while showtext:
        for char in showtext:
            if char == '█' or char == '_' or char == ':':
                print(MAGENTA + char, end='')
            elif char == '═' or char == '/' or char == '\\' or char == 'I':
                print(YELLOW + char, end='')
            elif char == '╝' or char == '|' or char == 'N':
                print(CYAN + char, end='')
            else:
                print(RED + char, end='')
        showtext = file.readline()
    file.close()
    time.sleep(veloT)

def showscene(filename):
    global velo, up, escena, menu, nota, comida

    file = open(filename,"r", encoding='utf-8')
    showtext = file.readline()
    color = chose_color.get(randint(1, 4))
    print(color)
    inicio = 0
    velo = 0.03
    while showtext :
        for char in showtext:
            if inicio == 0:  # sirve para leer el primer caracter y saber en que escena esta, asi poder mostrar opciones.
                menu = escena.get(int(char),1) # que lista de opciones estaran disponibles
                inicio = 1
            else:
                if up == 1 and (char!='%'): # se comprueba fin de linea para poder seguir escribiendo
                    continue
                else:
                    up = 0
                    if char == '@':
                        color = chose_color.get(randint(1, 4), 0)
                        print(color, end='') 
                        velo = 0
                    elif char == '$' and comida == 1:
                        up = 1
                    elif char == '+' and comida == 0:
                        up = 1
                    elif char == '/' and nota == 1:
                        up = 1
                    elif char == '<' and nota == 1:
                        up = 1                    
                    elif char == '>' and nota == 0:
                        up = 1
                    elif char =='%' or char == '>' or char == '$' or char == '+' or char == '/':
                        continue
                    elif char =='#':
                        time.sleep(veloT)
                        titulo = 2
                        showtitulo(titulo)                        
                        exit()
                    elif char =='*':
                        time.sleep(veloT)
                        titulo = 3
                        showtitulo(titulo)
                        exit()
                    elif char ==']':
                        comida = 1
                    elif char == '[':
                        nota = 1
                    else:
                        print(char, end='')
                        time.sleep(velo)
                    if char =='(' or char == ')':
                        print(GREEN, end='')
                    else:
                        print(color, end='')
        showtext = file.readline()
    file.close()

showtitulo(1)

clear()
showscene("./texto/Escena_casa.txt")
choice = input("\nElige una opción: ")


while choice:
    clear()
    if menu == chose_number: 
        showscene(menu.get(choice.upper(),tarta))
    else:
        showscene(menu.get(choice.upper(),mal))
    choice = input("\nElige una opción: ")




