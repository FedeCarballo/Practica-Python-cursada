def main() :
    p = float(input('ingrese la tarifa por segundo: '))
    n = int(input('ingrese la cantidad de llamadas realizadas: '))
    for x in range(n):
        h = int(input('cuantas horas: '))
        m = int(input('cuantos minutos: '))
        s = int(input('cuantos segundos: '))
        duracion = a_segundos(h,m,s)
        costo = duracion * p
        print("duracion: ",duracion," costo: ",costo)

def a_segundos(horas, minutos,segundos):
    return 3600 * horas +60 * minutos + segundos

main()