# Ejercicio 7.2. Definir una función …
# a) que reciba como parámetro una tupla tup con nombres, y para cada nombre imprima
# el mensaje “Estimado <nombre>, vote por mí “.
# b) modificar la solución anterior, para que el mensaje distinga el género del destinatario,
# considerando que tup es una tupla integrada por tuplas de la forma (nombre,
# género). [ Valores de género: ‘M’  masculino; ‘F’  femenino; ‘O’  otres ]

def main():
    tup = ("maria","F","alexander","M","rogelio","M", "lucia","F","mauricio","M", "alberto","M", "Helicoptero apache","O", "Boeng 747","O","Euclides","M")
    aux = 0
    for i in tup:
        aux +=1
        if((i == "F") | (i == "M") | (i== "O")):
            next
        else:
            count = tup[aux]
            if(count == "F"):
                print(i,"Femenino")
            elif (count == "M"):
                print(i,"Masculino")
            elif (count == "O"):
                print(i,"Otros")
main()