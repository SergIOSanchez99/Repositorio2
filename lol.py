import random

def run():
    numero_aleatorio=random.randint(1,100)
    numero_elegido=int(input("Elige un numero entre el 1 y 100-->"))
    vidas=5
    while numero_elegido!=numero_aleatorio:
        if(numero_elegido<numero_aleatorio):
            print("Numero muy pequeño, busque uno mayor")
            vidas-=1
        elif(numero_elegido>numero_aleatorio):
            print("Numero muy grande, busque uno pequeño")
            vidas-=1
        else:
            print("Ganaste")
            break
        numero_elegido=int(input("Digite de nuevo-->"))
        if(vidas==0):
            print("Perdiste |:'<")
            print("El numero era ",str(numero_aleatorio),".")
            break
        print("Tienes "+str(vidas)+" vidas")
    if(numero_aleatorio==numero_elegido):
        print("Ganaste")

if __name__=='__main__':
    run()