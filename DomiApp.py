'''
Juan Zapata Vélez - ADSO
+57 3045530299
jzvelez1997@gmail.com
'''
#==============================
# Sistema de Domicilio - Etapa
#==============================

distancia_km = float(input ("Ingrese la distancia en km: "))

print(f"distancia_km: {distancia_km}")

#   Funcion mientras se cumpla una condición 
continuar = "s"

while(continuar == "s"):

    # Evaluar condiciones
    if distancia_km <= 3:
            costo_domicilio = 3000
            print (f"Su pedido cuesta {costo_domicilio}")
    elif distancia_km <= 8:
            costo_domicilio = 7000
            print (f"Su pedido cuesta {costo_domicilio}")
    else:
        costo_domicilio = 0

    if costo_domicilio == 0:
        print (f"Su pedido no tiene covertura")
    else:
        print (f"Costo Domicilio = $ {costo_domicilio}")

    continuar = input("realizar otro cálculo (s/n)")
    
print("Gracias por usar nuestro sistema")


