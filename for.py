def run():
    mensaje="""
    ****************************************************
    ****************************************************
    ****PROBANDO EL CICLO FOR AL RECORRER UNA CADENA****    
    ****************************************************
    ****************************************************
    """
    print(mensaje)

    cadena=input("Escriba la cadena de caracteres que desea imprimir: ")

    for letra in cadena:
        print(letra.upper())


if __name__=='__main__':
    run()