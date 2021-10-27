import random

def generar_contraseña():

    contraseña = []
    mayuscula = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    especiales = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    caracteres = mayuscula + minuscula + numeros + especiales

    longitud_contraseña = int(input("De que longitud desea la contraseña: "))

    for i in range(longitud_contraseña):
        caracter = random.choice(caracteres)
        contraseña.append(caracter)

    contraseña = "".join(contraseña)

    return contraseña

def run():
    contraseña=generar_contraseña()
    print("Tu nueva contraseña es: " + contraseña)


if __name__=="__main__":
    run()