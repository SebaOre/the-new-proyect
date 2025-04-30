print("el terrible proyecto")
print("calculadora brijida")
while True:
    print("1.sumar")
    print("2.restar")
    print("3.salir")
    opc=int(input("ingrese una opcion: "))
    if opc==1:
        num1=int(input("ingrese un numero:"))
        num2=int(input("ingrese un numero:"))
        print("el resuletado es: ",num1+num2)
    elif opc==2:
        num1=int(input("ingrese un numero:"))
        num2=int(input("ingrese un numero:"))
        print("el resuletado es: ",num1-num2)
    elif opc==3:
        break;
    else:
        print("ingrese un numero valido")
        
        
