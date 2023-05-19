# Ejercicio 4.10. Definir una función denominada “es_primo”, que reciba un número
# entero por parámetro y devuelva un resultado booleano que indique si es primo, o no.
# [Un número natural es primo, si solamente es divisible por sí mismo y por 1].

def es_primo(num):
    aux = num
    for i in range(2,(aux-1)):
        if(aux%i == 0):
             return False
    if((aux%1==0) & (aux%aux==0)):
        return True
print(es_primo(25))
