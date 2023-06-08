# . Definir una función ‘encaja_domino’, que reciba por parámetro dos tuplas que
# representan fichas de dominó y devuelva un resultado booleano que indique si encajan o no.
# [Ej: las fichas (3, 4) y (4, 1) encajan, porque coinciden en el número 4. Ídem (4, 4) y (5, 4) ]

def encaja_domino(par1,par2):
    if ((par1[0] == par2[0]) or (par1[0] == par2[1]) or (par1[1] == par2[0]) or (par1[1] == par2[1])):
        print("Encaja")
    else:
        print("No encaja")
def main():
    t1 =(3,4)
    t2=(2,4)
    encaja_domino(t1,t2)
main()