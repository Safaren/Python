def conversor_C_F():
    Celsius = input("- Introduce los Celsius a convertir a Fahrenheit: ")
    Fah = round((int(Celsius) * 9 / 5) + 32, 2)
    print("- {} Celsius son Fahreheit: {}".format(Celsius, Fah ))

def conversor_F_C ():
    Fah = input("- Introduce los Fahrenheit a convertir a Celsius: ")
    Celsius = round((int(Fah) - 32) * 5/9, 2)
    print("- {} Fahreheit son Celsius: {}".format(Fah, Celsius ))

salir = 0
while (salir == 0):
    print("\n*=============================================*")
    print("***** Conversor de Fahremheit <-> Celsius *****")
    print("*=============================================*\n")

    print("· (1) Convertir de Fahrenheit a Celsius")
    print("· (2) Convertir de Celsius a Fahrenheit")
    print("· (3) Salir")
    choice = input("**** Elige una opción: ")
    print("")

    if (choice == "1"):
        conversor_F_C()
    elif (choice == "2"):
        conversor_C_F()
    else:
        salir = 1

    if salir == 0:
        print("")
        input("***** Pulse una tecla para continuar *****")