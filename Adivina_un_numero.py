
import colorama
from random import randint


# initialize the screen

colorama.init()






def autoText(long):
    Lenstr = len(long)
    print(colorama.Fore.YELLOW + "*" * Lenstr)

def adivina():
    number = randint(0,100)
    count = 0
    salir = 0
    cadena = "***** Adivina el número *****"
    autoText(cadena)
    print(colorama.Fore.MAGENTA + cadena)
    autoText(cadena)
    print("\n")
    print(colorama.Fore.GREEN)


    numberuser = input("Escribe un número del 0 al 100: ")
    while salir == 0:
        
        if int(numberuser) > 100:
            numberuser = input("Ese número es mayor que 100, anda quieres jugar o no: ")
        elif int(numberuser)< number : 
            numberuser = input("Uyys el número que eligistes es más pequeño, intentalo otra vez: ")
        elif int(numberuser) > number :
            numberuser = input("Uyys el número elegido es mayor, intentalo otra vez: ")
        elif int(numberuser) == number: 
            print("Adivinastes el número al {}º intento.".format(count))
            salir = 1
        else:
            numberuser = input("Pero por que escribes letras, ¿Crees que estamos en otra base que no sea la decimal?, anda escribe un número en base 10 :")
        count += 1
    choice = input("- Quieres volver a jugar (S/N): ")

    if choice == "S" or choice == "s":
        print(" ")
        adivina()
    else:
        print("- Hasta otra.")
adivina()

colorama.deinit()
