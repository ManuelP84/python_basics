def run():
    nombre="Manuel Guillermo"

    
    for letra in nombre:
        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
            nombre=nombre.replace(letra,"")

        print(nombre)

    # nombre2= nombre.translate(None, "AEIOUaeiou")
    # print(nombre)
               

if __name__ == "__main__":
    run()