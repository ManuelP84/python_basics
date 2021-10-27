

def run():
    
    def contador():
        count = 0
        numero = 1

        for i in range(100):
            print(f'numero: {numero}')
            print(f'contador: {count}')
            cadena= str(numero)
            lista_numero = [int(i) for i in str(cadena)]
            for i in range(len(lista_numero)):
                if lista_numero[i] ==6:
                    count+=1
                
            numero = numero +1
        return count

    numero_buscado = contador()
    print(numero_buscado)
          

if __name__=='__main__':
    run()