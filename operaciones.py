def potencia(x,y):
    res = x**y
    return res

def radicacion(x,y):
    res = x**(1/y)
    return res

a=float(input("Valor 1: "))
b=float(input("Valor 2: "))

op=input("Selecicone 'P' o 'p' para Potenciacion y 'R' o 'r' para Radicacion: ")

if(op=='P' or op=='p'):
    pot = potencia(a,b)
    pot = str(pot)
    print("La potencia es: "+pot)
elif(op=='R' or op=='r'):
    rad = radicacion(a,b)
    rad = str(rad)
    print("El radical es: "+rad)
else:
    print("Opcion no valida")

