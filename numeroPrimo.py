
# def dividir(dividendo, divisor):
#         pass


def es_primo(numero):
    contador=0
    if numero==1:
        return False
    else:
        for i in range(1,numero+1):
            if numero%i==0:
                contador+=1
        if contador>=3:
            return False
        else:
            return True
                
def run():
    
    numero=int(input("Por favor ingresa el número que deseas validar: "))

    if es_primo(numero):
        print("El número es primo")

    else:
        print("El número no es primo")

if __name__=='__main__':
    run()