def interseccion(li1,li2):
    lista3 = []
    for i in li1:
        for j in li2:
            if i == j:
                aux = i
                lista3.append(aux)
    print(lista3)

def main():
    lista1 = [1,2,3,4,5,6,7]
    lista2 = [2,4,5,6,8,9,15]
    interseccion(lista1,lista2)
main()