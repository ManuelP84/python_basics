
def conversor(trm, moneda):
    valor_pesos= int(input("Cuantos pesos " + moneda + "deseas convertir a dolares: "))
    valor_dolares = round(valor_pesos/trm,2)
    print("$ " + str(valor_pesos) + " pesos " + moneda + " equivalen a "+ "$" +str(valor_dolares)+" dolares")


menu = """

        Bienvenido al sistema de cambio de moneda

        Escoja que tipo de moneda desea cambiar:

        1. Cambio de pesos colombianos a dolares
        2. Cambio de pesos argentinos a dolares
        3. Cambio de pesos mexicanos a dolares
        
        """

opcion=int(input(menu))

if opcion==1:
    conversor(3500, "colombianos")

elif opcion ==2:
    conversor(65, "argentinos")

elif opcion ==3:
    conversor(24, "mexicanos")
else:
    print("Ingrese una opción válida")

