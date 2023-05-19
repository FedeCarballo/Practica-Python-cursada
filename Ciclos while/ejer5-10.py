
# Ejercicio 5.10. Definir una función que reciba como parámetro un número natural e
# imprima todos los números primos que hay hasta ese número. Utilice la función del
# ejercicio 4.10.

from ejer410 import es_primo 

def TodosPrimos(num):
    for i in range(1,num):
        if(es_primo(i) == True):
            print (i)
            i=i+1
TodosPrimos(29)