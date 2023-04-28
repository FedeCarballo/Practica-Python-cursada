# Ejercicio 5.2. Escribir un programa:
# a) que contenga una contraseña de 4 caracteres inventada, que le pregunte al usuario
# la contraseña y no le permita continuar hasta que la haya ingresado correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad fija de
# intentos. Al finalizar, deberá imprimir en pantalla “Eureka” si acertó la clave o, en
# caso contrario, “Clave incorrecta” y la cantidad de intentos fallidos.
# c) Modificar el programa anterior para que después de cada intento agregue una
# pausa cada vez mayor, utilizando la función time.sleep(…) del módulo time.

#-----------------------------------------------------------------------------------------------------
import time
def main():
    intentos_fallidos = 0
    contraseña  = 1235
    intentos = 5
    preg = input('ingrese su contraseña:  ')
    while(preg != contraseña & intentos_fallidos < 5):
        intentos = intentos-1
        intentos_fallidos+=1
        if(intentos == 0 ):
            return print('Programa bloqueado,pc bloqueado, llamando al 911 maquinola')
        print('contraseña incorrecta')
        print('intentos fallidos: ',intentos_fallidos, 'intentos restantes: ', intentos)
        preg = input('ingrese su contraseña:  ')
        time.sleep(intentos_fallidos)
    else:
        print('Eureka')
main()    
