'''
Juan Zapata Vélez - ADSO
+57 3045530299
jzvelez1997@gmail.com
'''
#==============================
# Sistema de Semáforo
#==============================

#Le pedimos al usuario que ingrese el estado del semáforo
estado_semaforo = input("Ingrese el estado del semáforo (rojo, amarillo, verde): ")



#Validamos el estado del semáforo y mostramos el mensaje correspondiente
if estado_semaforo == "verde":
    print("Avanzar el vehículo")
elif estado_semaforo == "amarillo":
    print("Reduzca su velocidad")
elif estado_semaforo == "rojo":
    print("Detener el vehículo")
    
#La condición else se ejecuta si el usuario ingresa un estado no válido
else:
    print("Estado no válido")
    
