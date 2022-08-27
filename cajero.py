opcion = 0
saldo = 1200000
contrasena = 1122
contrasenaDigitada = 0

print("******Cajero ABC******")
print("Seleccione la opción que desea ejecutar")

print("1: Consultar saldo")
print("2: Retirar dinero")
print("3: Cambiar contraseña")
print("4: Salir")
opcion = int(input("Ingrese su opción: "))

contrasenaDigitada = int(input("Ingrese su contraseña: "))
if (contrasenaDigitada != contrasena):
    print("Nega nega La contraseña no coincide")
else:
    if (opcion == 1):

        print("Su pobreza actual es de : " + str(saldo))
    elif (opcion == 2):

        retiro = int(input("Ingrese la cantidad que se va a perder :(("))
        if (retiro > saldo):
            print("Usted no tiene tanta plata, deje de inventar: ")
        else:
            modulo = retiro % 100000
            cien = (retiro - modulo)//100000
            print("Billetes de cienmil " + str(cien))
            cincuenta = (modulo - modulo % 50000)//50000
            print("Billetes de cincuenta " + str(cincuenta))
            modulo = modulo % 50000
            veintemil = (modulo - modulo % 20000)//20000
            print("Billetes de veintemil " + str(veintemil))
            modulo = modulo % 20000
            diezmil = (modulo - modulo % 10000)//10000
            print("Billetes de diezmil " + str(diezmil))
            modulo = modulo % 10000
            cincomil = (modulo - modulo % 5000)//5000
            print("Billetes de cincomil " + str(cincomil))
            modulo = modulo % 5000
            dosmil = (modulo - modulo % 2000)//2000
            print("Billetes de dosmil " + str(dosmil))
            modulo = modulo % 2000
            mil = (modulo - modulo % 1000)//1000
            print("Billetes de mil " + str(mil))

            saldo = saldo - retiro

            print(
                "Felicitaciones ahora está más pobre que antes, le quedan: " + str(saldo))
    elif (opcion == 3):
        contrasena = int(input("ingrese su nueva contraseña: "))
        print("Su nueva contraseña es:  " + str(contrasena))

    else:
        print("La buena parce se cuida :)")
