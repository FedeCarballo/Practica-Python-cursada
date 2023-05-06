# Ejercicio 5.3. Escribir un programa que elija un número al azar, entre 1 y 99, y lo mantenga
# en secreto (utilice la función random.randrange (1,100) del módulo random). El programa
# debe solicitar al usuario que adivine el número. Si el número que ingresa el usuario es
# mayor, el programa debe responder "Incorrecto, mi número es menor"; si el número
# ingresado es menor, el programa debe responder "Incorrecto, mi número es mayor". En
# ambos casos deberá solicitar otro número hasta que el usuario acierte el correcto. Mostrar la
# cantidad de intentos realizados para adivinar.

#----------------------------------------------------------------------------------------------------
import random
def main():
    num = int(random.randrange(1,99))
    intentos = 0
    user = input('Adivina el numero, ingrese el valor para ver si lo adivina: ')
    while(num != user & type(user) == int):
        intentos = intentos+1
        if(num< user):
            print('Incorrecto, el numero es menor')
            user = int(input('ingrese el numero nuevamente: '))
        else:
            print('Incorrecto, el numero es mayor')
            user = int(input('ingrese el numero nuevamente: '))
    print('Correcto! adivinaste, el numero es: ', num, 'cantidad de intentos: ',intentos)
main()