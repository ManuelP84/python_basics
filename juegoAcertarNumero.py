import random

def run():
    texto="""

    ******BIENVENIDO**********
    ***********A**************
    ******ADIVINANDO**********

    """
    print(texto)
    vidas=4
    numero_aleatorio=random.randint(1,50)
    print("Debes elegir un número entre 1 y 50. Tienes 5 portunidades")
    numero=int(input("Escoge un número: "))

    while numero_aleatorio != numero and vidas>0 :
        vidas -=1

        if numero>numero_aleatorio:
            print("Debes escoger un número menor")
        else:
            print("Debes escoger un número mayor")
        
        numero=int(input("Escoge otro número: "))
        print(vidas)
    
    if numero==numero_aleatorio and vidas >=0: 
        print("Ganaste!!!")
    else:
        print("Perdiste...")


if __name__ == "__main__":
    run()