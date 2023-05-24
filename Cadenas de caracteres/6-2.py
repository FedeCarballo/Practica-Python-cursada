# Ejercicio 6.2. Definir una función “segm_3_txt” que, dados como parámetros una cadena de 
# caracteres y un carácter (que denominaremos selector), 
# a) imprima los tres primeros caracteres de la cadena, si el valor del selector es la letra 
# ‘P’, o los tres últimos caracteres si el valor del selector es ‘U’, o el mensaje ‘Error en 
# el selector’ si el valor del selector no es ‘P’ ni ‘U’.
# b) modificar la solución anterior, para que sólo imprima el primero o el último carácter, 
# respectivamente, cuando la longitud de la cadena sea menor que 3.

def segm_3_txt(text):
    #a
    for c in text:
        if (c == 'P' | c== 'p'):
            print((text[:3]))
        elif(c == 'U' | c== 'u'):
            print((text[-3:]))
        else:
            print("Error en el Selector")
    #b
    if(len(text) < 3):
        print((text[:1]))
    else:
        print((text[-1:]))
segm_3_txt("holatengoqueponeruntextolargo")