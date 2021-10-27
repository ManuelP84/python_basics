
print("*****Bienvenido al programa de vacunación*****")
edad = int(input("Por favor ingresa tu edad: "))
if edad<18:
    print("Debes esperar a la fase indicada para recibir la vacuna")

elif 18<edad<65:
    print("Debes llamar a tu eps para programar cita de vacunación despues del 1 de julio")

else: 
    print("Acercate a tu lugar de conveniencia para recibir la vacuna")