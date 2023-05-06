# Ejercicio 4.11. Definir una función denominada “rango_etario”, que reciba por
# parámetro un número natural (que representa una edad) y devuelva como resultado la
# denominación de su respectivo grupo etario. Considere la siguiente clasificación:
# “primera infancia” (0 a 5 años), “infancia” (6 a 11 años), “adolescencia” (12 a 18 años),
# “juventud” (19 a 29 años), “adultez” (30 - 64 años) y “vejez” (65 años o más).


def main():
    rango_etario = int(input("ingrese una edad: "))
    rango_etario2(rango_etario)
def rango_etario2(num):
        if((num>0) & (num <=5)):
            return print(num," pertenece a primera infancia")
        elif ((num>5) & (num <=11)):
            return print(num," pertenece a infancia")
        elif ((num>12) & (num<=18)):
            return print(num," pertenece a adolescencia")
        elif ((num>19) & (num <=29)):
            return print(num," pertenece a juventud")
        elif ((num>30) & (num <=64)):
            return print(num," pertenece a adultez")
        elif ((num>65) & (num<200)):
            return print(num," pertenece a vejez")
        else:  
            print("sos mirtha legrand")
main()