import os
def menu():
    print("************ VARIABLES************")
    print("")
    print("")
    print("1. Numericos")
    print("2. booleanos")
    print("3. cadenas de caracteres")
    print("4. Salir")
    print("")
    print("")


menu()
opcion=input("Seleccione una opcion por favor: ")
while opcion != "4":
    if opcion=="1":
        print("**enteros/int: numeros enteros. Ejemplo: -6, -2, 0, 1, 2, 6...")
        print("**puntoFlotante/Float: numeros con coma(solo que con punto en python), irracionales. Ejemplo: 3.4, 5.6666, -1.2")
        print("**complejos/complex: numeros complejos, osea con componente imaginario y componente real. ejemplo: 1+2j, 30+46j")
        print("")
        print("")
        print(" Pruebe usted mismo: ")
        x=int(input("ingrese un entero: "))
        y=int(input("ahora ingrese otro para concretar la suma: "))
        operacion1=x+y
        print("su resultado: ", operacion1)
        x2=float(input("ingrese un numero de punto flotante: "))
        y2=float(input("ahora ingrese otro para concretar la multiplicacion: "))
        operacion2=x2*y2
        print("su resultado: ", operacion2)
        x3=complex(input("ingrese un numero complejo: "))
        y3=complex(input("ahora ingrese otro para concretar la resta: "))
        operacion3=x3-y3
        print("su resultado: ", operacion3)
    elif opcion=="2":
        print("los booleanos/bool son los que comprueba un verdadero o falso son los que generalmente usamos en en condiciones como el if o el while")
    elif opcion=="3":
        print("cadenas de caracteres o string(str), son básicamente secuencias de caracteres, o mas mundanamente dicho, texto")
        print("Para que una cadena de caracteres sea un string hay que ponerla entre comillas dobles " ", o simples ' ', de lo contrario no será tomada como tal")
        print("se pueden hacer algunas operaciones como suma entre strings o multiplcar un string por un entero")
        print("compruebelo usted mismo: ")
        texto1=input("ingrese 'hola' u algun string: ")
        texto2=input("ingrese ' mundo' u algun otro string para concretar esta suma: ")
        sumat=texto1+texto2
        print("he aqui el resultado: ", sumat)
        texto3=input("ingrese algun string a multiplicar: ")
        multiplo=int(input("ahora ingrese un numero entero para multiplicar: "))
        multiplot=texto3*multiplo
        print("he aqui el resultado: ", multiplot)
    else:
        print("Opcion invalida")
    input("presione [ENTER] para continuar")
    os.system("cls")
    menu()
    opcion=input("seleccione una opcion[5 para salir]: ")

print("Ha salido del menu")


