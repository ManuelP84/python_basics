
menu = """

        Bienvenido al sistema de cambio de moneda

        Escoja que tipo de moneda desea cambiar:

        1. Cambio de pesos colombianos a dolares
        2. Cambio de pesos argentinos a dolares
        3. Cambio de pesos mexicanos a dolares
        
        """

opcion=int(input(menu))


if opcion==1:
    valor_pesos= int(input("Cuantos pesos colombianos deseas convertir a dolares: "))
    trm = 3500
    valor_dolares = round(valor_pesos/trm,2)
    print("$ " + str(valor_pesos) + " pesos equivalen a "+ "$" +str(valor_dolares)+" dolares")

elif opcion ==2:
    valor_pesos= int(input("Cuantos pesos argentinos deseas convertir a dolares: "))
    trm = 65
    valor_dolares = round(valor_pesos/trm,2)
    print("$ " + str(valor_pesos) + " pesos equivalen a "+ "$" +str(valor_dolares)+" dolares")

elif opcion ==3:
    valor_pesos= int(input("Cuantos pesos mexicanos deseas convertir a pesos dolares: "))
    trm = 24
    valor_dolares = round(valor_pesos/trm,2)
    print("$ " + str(valor_pesos) + " pesos equivalen a "+ "$" +str(valor_dolares)+" dolares")
else:
    print("Ingrese una opción válida")

