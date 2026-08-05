'''
Juan Zapata Vélez - ADSO
+57 3045530299
jzvelez1997@gmail.com
'''
#==============================
# Sistema de Cine
#==============================

#Ejercicio 1:** Un cine cobra $8.000 la entrada. 
# Si el cliente es estudiante, tiene 20% de descuento. Escribe los pasos para calcular cuánto debe pagar.

print("Bienvenido al cine")
print("El precio de la entrada es de $8.000")

precio_entrada = 8000
es_estudiante = input("¿Es estudiante? (s/n): ") == "s"

if es_estudiante:
    monto_a_pagar = precio_entrada * 0.8  # Aplicar descuento del 20%
else:
    monto_a_pagar = precio_entrada

print(f"El cliente debe pagar: ${monto_a_pagar}")