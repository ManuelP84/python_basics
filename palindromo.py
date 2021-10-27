


def run():
    
    mensaje =    """
    Bienvenido al identificador de palindromos.
    //Este software identifica si una palabra es palindrome//
    
    """
    print(mensaje)

    palabra = input("Ingrese por favor la palabra: ")
    palabra=palabra.strip().lower().replace(" ","")
    palabra_invertida=palabra[::-1]
    #print(palabra)
    #print(palabra_invertida)

    if palabra == palabra_invertida:
        print("Es palindrmo")

    else:
        print("No es palindrmo")

if __name__ == '__main__':
    run()






