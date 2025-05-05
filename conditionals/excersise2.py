# Consigna 2: Determinar si una persona es mayor de edad.

temperatura = int(input("Temperatura: "))
humedad = int(input("Humedad: "))

if temperatura > 25:
    print("Refrigeración activada.")
elif temperatura < 18:
    print("Activar calefacción.")
else:
    print("Mantener apagado.")

if humedad > 60:
    print("Activar deshumidificador.")

#########################################################


print("1 - Entrada general. Costo: 1000$")
print("2 - Entrada 3D. Costo: 1500$")
print("3 - Entrada 4D. Costo: 2000$")
entrada_comprada = int(input("Ingrese el numero de entrada a elegir: "))

costo_entrada = 0

if entrada_comprada == 1:
    costo_entrada = 1000
elif entrada_comprada == 2:
    costo_entrada = 1500
elif entrada_comprada == 3:
    costo_entrada = 2000

descuento_total = 0 # porcentaje, resultado de la suma de descuentos

tiene_club = int(input("Forma parte de un club? (1 para si, 0 para no): ")) # club 15%
if tiene_club == 1:
    descuento_total = 0.85

es_estudiante = int(input("Es estudiante? (1 para si, 0 para no): ")) # Estudiantes - 30%
if es_estudiante == 1:
    descuento_total = 0.7

es_jubilado = int(input("Es jubilado? (1 para si, 0 para no): "))# Jubilados - 40%
if es_jubilado == 1:
    descuento_total = 0.6

edad_ingresada = int(input("Ingrese su edad: ")) # Menores de 12 - 50%
if edad_ingresada < 12:
    descuento_total = 0.5

es_miercoles = int(input("Es miercoles? (1 para si, 0 para no): ")) # miercoles 20% adicional
if es_miercoles == 1:
    es_miercoles = 0.8

precio_final = costo_entrada * (descuento_total + es_miercoles)

print(f"Descuento aplicado: {descuento_total}")
print(f"Precio final: {precio_final}")
