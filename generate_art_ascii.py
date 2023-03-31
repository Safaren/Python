# Programa que transforma una cadena de letras en 
# arte Ascii
# Autor: Sergio Aparicio Manso (Safaren)



import os
import colorama
import time
import shutil

letra_a = [
'          _          ',
'         / /\        ',
'        / /  \       ',
'       / / /\ \      ',
'      / / /\ \ \     ',
'     / / /  \ \ \    ',
'    / / /___/ /\ \   ',
'   / / /_____/ /\ \  ',
'  / /_________/\ \ \ ',
' / / /_       __\ \_\\',
' \_\___\     /____/_/',
]


letra_b = [
'           _        ',
'          / /\      ',
'         / /  \     ',
'        / / /\ \    ',
'       / / /\ \ \   ',
'      / / /\ \_\ \  ',
'     / / /\ \ \___\ ',
'    / / /  \ \ \__/ ',
'   / / /____\_\ \   ',
'  / / /__________\  ',
'  \/_____________/  ',
]
letra_c = [
'          _       ',
'         /\ \     ', 
'        /  \ \    ', 
'       / /\ \ \   ', 
'      / / /\ \ \  ', 
'     / / /  \ \_\ ', 
'    / / /    \/_/ ', 
'   / / /          ', 
'  / / /________   ', 
' / / /_________\  ', 
' \/____________/  ', 
]
letra_d = [
'        _         ',
'       /\ \       ',
'      /  \ \____  ',
'     / /\ \_____\ ',
'    / / /\/___  / ',
'   / / /   / / /  ',
'  / / /   / / /   ',
' / / /   / / /    ',
' \ \ \__/ / /     ',
'  \ \___\/ /      ',
'   \/_____/       ',
]
letra_e = [
'          _      ', 
'         /\ \    ', 
'        /  \ \   ', 
'       / /\ \ \  ', 
'      / / /\ \_\ ', 
'     / /_/_ \/_/ ', 
'    / /____/\    ', 
'   / /\____\/    ', 
'  / / /______    ', 
' / / /_______\   ', 
' \/__________/   ',                 
]
letra_f = [
'          _      ',
'         /\ \    ',
'        /  \ \   ',
'       / /\ \ \  ',
'      / / /\ \_\ ',
'     / /_/_ \/_/ ',
'    / /____/\    ',
'   / /\____\/    ',
'  / / /          ',
' / / /           ',
' \/_/            ',                
]

letra_g = [
'          _        ', 
'         /\ \      ', 
'        /  \ \     ', 
'       / /\ \_\    ', 
'      / / /\/_/    ', 
'     / / / ______  ', 
'    / / / /\_____\ ', 
'   / / /  \/____ / ', 
'  / / /_____/ / /  ', 
' / / /______\/ /   ', 
' \/___________/    ',                  
]
letra_h = [
'          _       _   ',
'         / /\    / /\ ',
'        / / /   / / / ',
'       / /_/   / / /  ',
'      / /\ \__/ / /   ',
'     / /\ \___\/ /    ',
'    / / /\/___/ /     ',
'   / / /   / / /      ',
'  / / /   / / /       ',
' / / /   / / /        ',
' \/_/    \/_/         ',              
]
letra_i = [
'           _     ', 
'          /\ \   ', 
'          \ \ \  ', 
'          /\ \_\ ', 
'         / /\/_/ ', 
'        / / /    ', 
'       / / /     ', 
'      / / /      ', 
'  ___/ / /__     ', 
' /\__\/_/___\    ', 
' \/_________/    ', 
]
letra_j = [
'              _     ',
'             /\ \   ',
'             \ \ \  ',
'             /\ \_\ ',
'            / /\/_/ ',
'   _       / / /    ',
'  /\ \    / / /     ',
'  \ \_\  / / /      ',
'  / / /_/ / /       ',
' / / /__\/ /        ',
' \/_______/         ',                   
]
letra_k = [
'          _        ',
'         /\_\      ',
'        / / /  _   ',
'       / / /  /\_\ ',
'      / / /__/ / / ',
'     / /\_____/ /  ',
'    / /\_______/   ',
'   / / /\ \ \      ',
'  / / /  \ \ \     ',
' / / /    \ \ \    ',
' \/_/      \_\_\   ',                
]
letra_l = [
'          _     ', 
'         _\ \   ', 
'        /\__ \  ', 
'       / /_ \_\ ', 
'      / / /\/_/ ', 
'     / / /      ', 
'    / / /       ', 
'   / / / ____   ', 
'  / /_/_/ ___/\ ', 
' /_______/\__\/ ', 
' \_______\/     ', 
]
letra_m = [
'         _   _       ', 
'        /\_\/\_\ _   ', 
'       / / / / //\_\ ', 
'      /\ \/ \ \/ / / ', 
'     /  \____\__/ /  ', 
'    / /\/________/   ', 
'   / / /\/_// / /    ', 
'  / / /    / / /     ', 
' / / /    / / /      ', 
' \/_/    / / /       ', 
'         \/_/        ', 
]
letra_n = [
'          _           ',
'         /\ \     _   ',
'        /  \ \   /\_\ ',
'       / /\ \ \_/ / / ',
'      / / /\ \___/ /  ',
'     / / /  \/____/   ',
'    / / /    / / /    ',
'   / / /    / / /     ',
'  / / /    / / /      ',
' / / /    / / /       ',
' \/_/     \/_/        ',                    
]
letra_ñ = [
'          _  `--__--   ',
'         /\ \     _ `  ',
'        /  \ \   /\_\ ',
'       / /\ \ \_/ / / ',
'      / / /\ \___/ /  ',
'     / / /  \/____/   ',
'    / / /    / / /    ',
'   / / /    / / /     ',
'  / / /    / / /      ',
' / / /    / / /       ',
' \/_/     \/_/        ',     
]
letra_o = [
'          _       ', 
'         /\ \     ', 
'        /  \ \    ', 
'       / /\ \ \   ', 
'      / / /\ \ \  ', 
'     / / /  \ \_\ ', 
'    / / /   / / / ', 
'   / / /   / / /  ', 
'  / / /___/ / /   ', 
' / / /____\/ /    ', 
' \/_________/     ',
] 
letra_p = [
'          _      ', 
'         /\ \    ', 
'        /  \ \   ', 
'       / /\ \ \  ', 
'      / / /\ \_\ ', 
'     / / /_/ / / ', 
'    / / /__\/ /  ', 
'   / / /_____/   ', 
'  / / /          ', 
' / / /           ', 
' \/_/            ',         
]
letra_q = [
'          _       ', 
'         /\ \     ', 
'        /  \ \    ', 
'       / /\ \ \   ', 
'      / / /\ \ \  ', 
'     / / /  \ \_\ ', 
'    / / / _ / / / ', 
'   / / / /\ \/ /  ', 
'  / / /__\ \ \/   ', 
' / / /____\ \ \   ', 
' \/________\_\/   ', 
]
letra_r = [
'         _      ', 
'        /\ \    ', 
'       /  \ \   ', 
'      / /\ \ \  ', 
'     / / /\ \_\ ', 
'    / / /_/ / / ', 
'   / / /__\/ /  ', 
'  / / /_____/   ', 
' / / /\ \ \     ', 
'  / /  \ \ \    ', 
' /_/    \_\/    ', 
]
letra_s = [
'         _        ', 
'        / /\      ', 
'       / /  \     ', 
'      / / /\ \__  ', 
'     / / /\ \___\ ', 
'     \ \ \ \/___/ ', 
'      \ \ \       ', 
'  _    \ \ \      ', 
' /_/\__/ / /      ', 
' \ \/___/ /       ', 
'  \_____\/        ',  
]
letra_t = [
'        _       ', 
'       /\ \     ', 
'       \_\ \    ', 
'       /\__ \   ', 
'      / /_ \ \  ', 
'     / / /\ \ \ ', 
'    / / /  \/_/ ', 
'   / / /        ', 
'  / / /         ', 
' /_/ /          ', 
' \_\/           ',                
]
letra_u = [
'    _               ', 
'   /\_\             ', 
'  / / /         _   ', 
'  \ \ \__      /\_\ ', 
'   \ \___\    / / / ', 
'    \__  /   / / /  ', 
'    / / /   / / /   ', 
'   / / /   / / /    ', 
'  / / /___/ / /     ', 
' / / /____\/ /      ', 
' \/_________/       ',
]
letra_v = [
'  _          _  ', 
' /\ \    _ / /\ ', 
' \ \ \  /_/ / / ', 
'  \ \ \ \___\/  ', 
'  / / /  \ \ \  ', 
'  \ \ \   \_\ \ ', 
'   \ \ \  / / / ', 
'    \ \ \/ / /  ', 
'     \ \ \/ /   ', 
'      \ \  /    ', 
'       \_\/     ',
]
letra_w = [
'         _           ', 
'        / /\      _  ', 
'       / / /    / /\ ', 
'      / / /    / / / ', 
'     / / /_   / / /  ', 
'    / /_//_/\/ / /   ', 
'   / _______/\/ /    ', 
'  / /  \____\  /     ', 
' /_/ /\ \ /\ \/      ', 
' \_\//_/ /_/ /       ', 
'     \_\/\_\/        ', 
]
letra_x = [
'   _      _      ', 
' /_/\    /\ \    ', 
' \ \ \   \ \_\   ', 
'  \ \ \__/ / /   ', 
'   \ \__ \/_/    ', 
'    \/_/\__/\    ', 
'     _/\/__\ \   ', 
'    / _/_/\ \ \  ', 
'   / / /   \ \ \ ', 
'  / / /    /_/ / ', 
'  \/_/     \_\/  ', 
]
letra_y = [
'  _        _   ', 
' /\ \     /\_\ ', 
' \ \ \   / / / ', 
'  \ \ \_/ / /  ', 
'   \ \___/ /   ', 
'    \ \ \_/    ', 
'     \ \ \     ', 
'      \ \ \    ', 
'       \ \ \   ', 
'        \ \_\  ', 
'         \/_/  ', 
]
letra_z = [
'        _         ', 
'      /\ \        ', 
'     /  \ \       ', 
'  __/ /\ \ \      ', 
' /___/ /\ \ \     ', 
' \___\/ / / /     ', 
'       / / /      ', 
'      / / /    _  ', 
'      \ \ \__/\_\ ', 
'       \ \___\/ / ', 
'        \/___/_/  ', 
]
espacio = [
'                  ',
'                  ',
'                  ',
'                  ',
'                  ',
'                  ',
'                  ',
'                  ',
'                  ',
'                  ',
'                  ',   
]
letras = {
    'a': letra_a,
    'b': letra_b,
    'c': letra_c,
    'd': letra_d,
    'e': letra_e,
    'f': letra_f,
    'g': letra_g,
    'h': letra_h,
    'i': letra_i,
    'j': letra_j,
    'k': letra_k,
    'l': letra_l,
    'm': letra_m,
    'n': letra_n,
    'ñ': letra_ñ,
    'o': letra_o,
    'p': letra_p,
    'q': letra_q,
    'r': letra_r,
    's': letra_s,
    't': letra_t,
    'u': letra_u,
    'v': letra_v,
    'w': letra_w,
    'x': letra_x,
    'y': letra_y,
    'z': letra_z,
    '+': espacio,
}

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

VEL = 2

def ft_title(title):
    n_char = len(title) + 10
    espace = int(check_with()/2) - n_char 
    print( ' ' *  espace + MAGENTA +'*' * n_char )
    print(' ' * espace + MAGENTA + '**** ' + YELLOW + title + MAGENTA +' ****')
    print(' ' * espace + MAGENTA +'*' * n_char)
    time.sleep(VEL)
    clear()

def clear():
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear')

def check_with():
    ancho_terminal = shutil.get_terminal_size((80, 20)).columns
    return ancho_terminal

def input_frase(frase,inicio,fin):
    str =''
    linea_str = ''   
    #desde la fila 0 hasta la ultima que es 11
    for n in range(0,11):
        # creamos lineas en una lista desde la primera letra que cabe 
        # en el ancho de la terminal hasta la ultima.
        for  letra in frase[inicio : fin]: 
            str =letras.get(letra,espacio)
            for char in str[n]: 
                if char == '/' :
                    linea_str += MAGENTA + char
                elif char == '\\' :
                    linea_str += YELLOW + char
                elif char == '_':
                    linea_str += CYAN + char
                else: 
                    linea_str += MAGENTA + char
        # al acabar de dibujar cada linea, salto de linea            
        linea_str += '\n'
        
    return linea_str

        
def main():   
    colorama.init()
    ft_title('ASCII ART')
    while True:
        str = input("Introduce una frase, los caracteres que no sean letras, se dibujan como espacios: ").lower()
        inicio = 0
        colum = int (check_with()/22)
        end_range = len(str)/check_with()
        # calculos para saber cuando hay que saltar de linea
        if end_range <= 0:
            fin = len(str)
        elif len(str) % check_with() != 0:
            fin = colum
        else :
            fin = int (check_with()/22)
        if fin > len(str) :
            fin = len(str)
        clear()
        while fin <= len(str) :
            print( input_frase(str,inicio,fin),end='')
            fin += colum
            if fin <= len(str):
                inicio +=  colum
            # si no es una división exacta de columnas por caracteres.
            elif fin > len(str) and fin - int (check_with()/22) != len(str) :
                inicio +=  colum
                print( input_frase(str,inicio,len(str)),end='')
            exit = input("Pulsa (Q) para salir, otra letra continuar: ").lower()
        if  exit == 'q': 
            break
if __name__ == '__main__':
    main()
