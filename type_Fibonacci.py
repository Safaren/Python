import os
import colorama
import time

MAGENTA = colorama.Fore.MAGENTA
RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW
CYAN = colorama.Fore.CYAN
GREEN = colorama.Fore.GREEN

VEL = 2

lon = 20

espace = 0
n_char = 0
end_menu = ""


def ft_fibonacci_iterativo(lon):
    succesion = [0, 1]
    for i in range(2,lon + 1):
        succesion.append(succesion[i-1] + succesion[i-2])
    return succesion

def ft_fibonacci_recursive_for(lon):
    succesion = [0, 1]
    for n in range(2, lon +1):
        succesion.append(ft_fibonacci_recursive(n))
    return succesion

def ft_fibonacci_recursive(lon):
    if lon <= 1:
        return lon
    else:
        return (ft_fibonacci_recursive(lon-1) + ft_fibonacci_recursive(lon-2))

def ft_fibonacci_other(lon):
    ant_number = 1
    ant_number2 = 0
    number = 1
    sucesion = [0, 1, 1]
    while len(sucesion) <= lon:
        ant_number2 = ant_number
        ant_number = number
        number = ant_number + ant_number2
        sucesion.append(number)
    return sucesion

def ft_change_count():
    global lon
    
    while True:
        number = input(CYAN + 'Escribe la longitud de la cadena: ')
        if number.isdigit():
            lon = int(number)
            break
        else:
            ft_carabela()
    
    clear()

def ft_quit():
    exit()

chose_fibonacci = {
    '1': ft_fibonacci_iterativo,
    '2': ft_fibonacci_recursive_for,
    '3': ft_fibonacci_other,
    '4': ft_change_count,
    '5': ft_quit,
}


def ft_carabela():
    print(RED)
    print('''
           /\\
          /  \\
         /____\\
      <   O  O   >
       \_  ~  _/
         /  ! \\
    ''')

def clear():
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear')

def ft_title(title):
    global espace, n_char
    n_char = len(title) + 10
    espace = int(check_witdh()/2) - n_char 
    print( ' ' *  espace + MAGENTA +'*' * n_char )
    print(' ' * espace + MAGENTA + '**** ' + YELLOW + title + MAGENTA +' ****')
    print(' ' * espace + MAGENTA +'*' * n_char)
    time.sleep(VEL)
    # clear()


def check_witdh():
    ancho_terminal = os.get_terminal_size().columns
    return ancho_terminal

def len_str_menu(menu):
    lineas = []
    count = 0
    for char in menu:
        if char !='.' :
            count += 1
            
        elif char =='\n' :
            count -=1
        else:
            lineas.append(count)
            count = 0
    for n in range(len(lineas)): 
        if n > 0:
            if lineas[n] > lineas[n-1]:
                max_long = lineas[n]
    lineas.append(max_long)
    return lineas

def create_menu(menu):
    global espace, n_char, end_menu
    char = ''
    width_box = len_str_menu(menu)

    n = 0
    long_line = (espace + int(n_char/2)) - int((width_box[len(width_box)-1]+8)/2)
    end_menu += GREEN + ' ' * long_line + '╔' + '═' * (width_box[len(width_box)-1] + 6) + '╗'
    for char in menu:
        if char =='(' or char == ')':
            end_menu += GREEN
            if char =='(': 
                end_menu +=' ' * long_line  + '║' + ' ' * 3

        elif char == '.': 
            end_menu += GREEN +char + ' ' * (3 + (width_box[len(width_box)-1] - width_box[n] ))+ '║'
            n += 1
        else:
            end_menu += MAGENTA
        if char !='.':
            end_menu += char
    end_menu += GREEN + ' ' * long_line + '╚' + '═' * (width_box[len(width_box)-1] + 6) + '╝\n'

def ft_input():
    while True:
        print(end_menu, end='')
        choice = input('\n' + MAGENTA +' ' * 6 + "Seleciona una función de la secuencia de Fibonacci: ")
        if int(choice) < 4: 
            print(CYAN + "\nLos primeros {} números de la secuencia de Fibonacci son:".format(lon))
            print('{}'.format(chose_fibonacci[choice](lon)))
            input(YELLOW + "\nPulse ENTER para continuar")
        else:
            chose_fibonacci[choice]()

def main():
    colorama.init() 
    clear()
    ft_title("Secuencia de Fibonacci")
    menu = '''
(1) - Función de Fibonacci.
(2) - Función de Fibonacci recursiva.
(3) - Función de Fibonacci otra forma.
(4) - Cambiar longitud de la cadena de la succesion de Fibonacci.
(5) - Salir.\n'''
    create_menu(menu)
    ft_input()

if __name__ == "__main__":
    main()