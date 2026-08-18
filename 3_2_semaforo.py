#=================================================
# Función para iniciar el contador del semáforo ==
#=================================================

def iniciar_contador_semaforo(segundos_totales):

    segundo_actual = segundos_totales

    print(f"Semáforo en marcha ({segundos_totales} segundos).")
    print("Presiona ENTER para avanzar el tiempo o escribe 'p' para INTERRUMPIR.")

    while segundo_actual > 0:
        # Motrar los segundos
        entrada = input(f"Contador: {segundo_actual}s | Presiona tecla: ")

        # Si el usuario escribe algo o pulsa 'p', se interrumpe el tiempo
        if entrada != "":
            print(f"¡Interrupción manual a los {segundo_actual} segundos!")

            # Evaluamos el estado del semáforo según el tiempo restante
            if segundo_actual >=6:
                return "verde"
            elif segundo_actual <6 and segundo_actual >=1:
                return "amarillo"

        # Avanzamos 1 segundo en la cuenta
        segundo_actual -= 1

    # Contador llegó a 0
    print("Se agotó el tiempo")
    return "rojo"

#=======================
# Programa principal  ==
#=======================

# 1. Llamamos a la función de contador pasando 20 segundos
estado_semaforo = iniciar_contador_semaforo(20)

print("=" * 45)
print(f"Estado final SEMÁFORO: {estado_semaforo.upper()}")
print("=" * 45)

# 2. Validamos el estado devuelto por la función
if estado_semaforo == "verde":
    print("Avanzar en el vehículo")
elif estado_semaforo == "amarillo":
    print("Reduzca la velocidad")
elif estado_semaforo == "rojo":
    print("Detener el vehículo")
else:
    print("Estado no válido")