 # Paso 1:  Definir cuántos centímetros entran en una pulgada.
pulgada = 2.54

# Paso 2:  Solicitar al usuario que ingrese las medidas de la pieza del mueble en cm.
medidas_cm = float(input("Por favor, ingrese las medidas de la pieza en centímetros para convertirla a pulgadas: "))
# Paso 3: Realizar la conversión de centímetros a pulgadas.
medidas_pulgadas = medidas_cm * pulgada

# Paso 4: Mostrarle al usuario las medidas convertidas a pulgadas.
print("Las medidas en pulgadas de la pieza ingresada son:", medidas_pulgadas)