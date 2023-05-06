# Definir una función “nombre_dia” que, dado por parámetro un número
# de día de la semana, devuelva como resultado su nombre. Considere 2do día a “lunes”.

def nombre_dia():
    dia = int(input("ingrese dia de la semana"))
    if(dia == 1):
        return print("el dia es Domingo")
    elif(dia == 2):
        return print("el dia es Lunes")
    elif(dia == 3):
        return print("el dia es Martes")
    elif(dia == 4):
        return print("el dia es Miercoles")
    elif(dia == 5):
        return print("el dia es Jueves")
    elif(dia == 6):
        return print("el dia es Viernes")
    elif(dia == 7):
        return print("el dia es Sabado")
    else: 
        return print("ingresa una fecha valida")
nombre_dia()