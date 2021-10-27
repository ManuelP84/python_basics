def run():
    texto=input("Ingrese una palabra. Se contará el número de vocales:  ")
    contador =0

    for i in texto:
        if i=='a' or i=='e' or i=='i' or i=='o'or i=='u':
            contador +=1

        
    print("El texto ingresado contiene " + str(contador) + " vocales.")

if __name__=='__main__':
    run()