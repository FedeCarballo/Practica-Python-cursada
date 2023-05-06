# Ejercicio 5.9. Escribir un programa que le pida al usuario que ingrese una sucesión de
# calificaciones de estudiantes (primero el número de legajo, luego la calificación, y así para
# cada estudiante, hasta que el usuario ingrese el legajo -1 como condición de salida). Al
# final, el programa debe imprimir cuántas calificaciones fueron ingresadas, su valor máximo
# ingresado, la suma total de las calificaciones y el promedio.

def main():
    aux = 0
    num = 0
    calificaciones = int(input("ingrese la calificacion: "))
    legajo = int(input("ingrese el legajo: "))
    while(legajo != -1):
        aux = calificaciones + aux
        num +=1
        calificaciones = int(input("ingrese la calificacion: "))
        legajo = int(input("ingrese el legajo: "))
    promedio = aux//num
    return print("el promedio es: ",promedio)
main()    