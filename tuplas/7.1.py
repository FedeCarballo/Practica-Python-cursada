def vote_por_mi(tuplota):
    for tuplita in tuplota:
        if tuplita[1] == "M":
            print ("Estimado", tuplita[0])
        elif tuplita[1] == "F":
            print ("Estimada", tuplita[0])
        else:
            print ("Estimade", tuplita[0])
def main():
    t = (("Juan", "M"),("Ana", "F"),("Pedro", "O"),("Federica","F"))
    vote_por_mi(t)
main()