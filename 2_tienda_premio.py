'''
Juan Zapata Vélez - ADSO
+57 3045530299
jzvelez1997@gmail.com
'''
#==============================
# Sistema de Tienda de Premios
#==============================

# **Ejercicio 2:** Una tienda da un premio si el cliente compra 5 productos o más. Escribe los pasos para decidir si aplica el premio.

print("Bienvenido a la tienda")
print("¿Cuántos productos compró?")

cantidad_productos = int(input("Ingrese la cantidad de productos: "))

if cantidad_productos >= 5:
    print("¡Ganaste un premio!")
else:
    print("Sigue comprando para ganar.")