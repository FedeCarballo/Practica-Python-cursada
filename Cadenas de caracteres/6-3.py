# Ejercicio 6.3. Definir una función que reciba una cadena de caracteres como parámetro y
# devuelva como resultado la cadena invertida. (Ej: para el argumento ‘Hola Undav!’ debería 
# devolver al programa principal ‘!vadnU aloH’. No utilizar segmento de cadena [ : : -1 ] )

def text(text):
    aux = ''
    for c in reversed(text):
        aux+=c
    print(aux)    
text('fede')