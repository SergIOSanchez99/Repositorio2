def sumatoria(n):
    if n==0:
        return 0
    else:
        return n + sumatoria(n-1)
    
numero=int(input("Coloque el numero a calcular la sumatoria-->"))
while numero<0:
    if numero<0:
        print("Numero no valido")
    else:
        break
    numero=int(input("Digite un numero positivo-->"))

print("Sumatoria de ",str(numero),"-->",sumatoria(numero))

