

def run():
    exponente_maximo = int(input("Por favor ingrese la potencia máxima a la cual desea elevar: "))
    base=int(input("Ahora ingrese la base a elevar :"))
    exponente = 0
    potencia=base
    #potencia=potencia**exponente
    potencia=base**exponente

    while exponente<=exponente_maximo:
        print(str(base)+" elevado a la " + str(exponente) + " es igual a " + str(potencia))
        exponente=exponente+1
        potencia=base**exponente

if __name__=='__main__':
    run()
    

