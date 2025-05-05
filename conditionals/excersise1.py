# Consigna 1: Diseñar un programa que pueda definir si un
# alumno es aprobado o reprobado por su nota.

if (1 > 0):
    print("Hello World!")

anio_ingresado = int(input("Ingrese año: "))

if (anio_ingresado % 4) == 0 and (anio_ingresado % 100) != 0 or (anio_ingresado % 400) == 0:
    print("Es Bisieto.")
    if True:
        print("Print.")
else:
    print("No es Bisieto.")


monto_ingresado = int(input("Ingrese monto: "))

es_jubilado = int(input("Es jubildado? (1 o 0): "))

descuento_jubilado = 0

descuento_aplicado = 0

if es_jubilado == 1:
    descuento_jubilado = 0.05

if monto_ingresado > 5000:
    descuento_aplicado = 0.85
elif monto_ingresado >= 3000:
    descuento_aplicado = 0.90
elif monto_ingresado > 1000:
    descuento_aplicado = 0.95

print(f"Al monto de  {monto_ingresado}  se le aplicara un {descuento_aplicado + descuento_jubilado:.2f} de descuento quedando en:  "
      f"{monto_ingresado * (descuento_aplicado + descuento_jubilado)}")



