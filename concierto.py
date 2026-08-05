'''
Juan Zapata Vélez - ADSO
+57 3045530299
jzvelez1997@gmail.com
'''

#Captura de los datos del usuario
edad = int(input("Ingrese su edad: "))
diasBoletas = int(input("¿Hace cuantos días compró la boleta? "))

#Definir las condiciones para el ingreso al concierto
if edad >= 18 and diasBoletas >= 7:
    boletas = "Vip"
    print(f"Puede ingresar al concierto como {boletas}")

elif edad >= 18 or diasBoletas >= 7:
    boletas = "General"
    print(f"Puede ingresar al concierto como {boletas}")
    
else:
    boletas = "No puede ingresar"
    print(f"{boletas} al concierto")





