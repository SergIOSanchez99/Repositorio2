def calculadora_suma(a,b):
    return a+b

def calculadora_resta(a,b):
    return a-b

def calculadora_multiplicacion(a,b):
    return a*b

def calculadora_division(a,b):
    return a/b

def menu_Calculadora():
    print("Bienvenido usuario 👽👽👽:")
    print("1.Suma") 
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")

    opcion = input("Seleccione: ")
    x=int(input("Valor 1-->"))
    y=int(input("Valor 2-->"))   

    if(opcion=='1'):
        resultado = calculadora_suma(x,y)
    elif(opcion=='2'):
        resultado =  calculadora_resta(x,y)
    elif(opcion=='3'):
        resultado =  calculadora_multiplicacion(x,y)
    elif(opcion=='4'):
        resultado = calculadora_division(x,y)
    return resultado

final = menu_Calculadora()

print(final)
