
def multiplicar(numero):
    for i in range(11):
        print(str(numero) + " por " + str(i) + " es igual a "+ str(numero*i))

def run():
    
    bienvenida="""
    *************************
    LAS TABLAS DE MULTIPLICAR
    *************************    
    """
    print(bienvenida)
    opcion=int(input("Cuál tabla deseas estudiar: "))
    multiplicar(opcion)

if __name__=='__main__':
    run()
