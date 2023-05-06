# Escribir un programa de astrología que pida al usuario que ingrese el
# número de día y el número de mes correspondientes a su fecha de cumpleaños, e
# imprima en pantalla el signo del zodíaco al que pertenece. Considere las siguientes
# fechas:
# Aries: 21 de marzo al 20 de abril.
# Tauro: 21 de abril al 20 de mayo.
# Geminis: 21 de mayo al 20 de junio.
# Cáncer: 21 de junio al 21 de julio.
# Leo: 22 de julio al 22 de agosto.
# Virgo: 23 de agosto al 22 de septiembre.
# Libra: 23 de septiembre al 22 de octubre.
# Escorpio: 23 de octubre al 22 de noviembre.
# Sagitario: 23 de noviembre al 21 de diciembre.
# Capricornio: 22 de diciembre al 20 de enero.
# Acuario: 21 de enero al 19 de febrero.
# Piscis: 20 de febrero al 20 de marzo.

def astrología_en_casa():
    fecha = int(input("Ingrese la fecha: "))
    mes = int(input("Ingrese mes: "))
    if(mes==1):
        if((fecha> 0) & (fecha<=20)):
            return print("sos de Capricornio ")
        elif((fecha>20)& (fecha<31)):
            return print("sos de Acuario")
    elif(mes == 2):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Acuario")
        elif((fecha>20)& (fecha<28)):
            return print("sos de Piscis")
    elif(mes == 3):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Piscis")
        elif((fecha>20)& (fecha<31)):
            return print("sos de Aries")
    elif(mes == 4):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Aries")
        elif((fecha>20)& (fecha<30)):
            return print("sos de Tauro")
    elif(mes == 5):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Tauro")
        elif((fecha>20)& (fecha<31)):
            return print("sos de Geminis")
    elif(mes == 6):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Geminis")
        elif((fecha>20)& (fecha<30)):
            return print("sos de Cáncer")
    elif(mes == 7):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Cáncer")
        elif((fecha>20)& (fecha<31)):
            return print("sos de Leo")
    elif(mes == 8):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Leo")
        elif((fecha>20)& (fecha<31)):
            return print("sos de Virgo")
    elif(mes == 9):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Virgo")
        elif((fecha>20)& (fecha<30)):
            return print("sos de Libra")
    elif(mes == 10):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Libra")
        elif((fecha>20)& (fecha<31)):
            return print("sos de Escorpio")
    elif(mes == 11):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Escorpio")
        elif((fecha>20)& (fecha<30)):
            return print("sos de Sagitario")
    elif(mes == 12):
        if((fecha>0)& (fecha<=19)):
            return print("sos de Sagitario")
        elif((fecha>20)& (fecha<31)):
            return print("sos de Capricornio")
    else: print("ingresa un mes valido")
    
astrología_en_casa()