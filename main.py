# 3)Crear un programa para un gimnasio que calculé la mensualidad:
# -plan básico: $2000
# -plan intermedio: $3500
# -plan premium: $5000
# Descuentos:
# -pago anual: 20% de descuento
# -pago semestral: 10% de descuento
# -pago estudiante:15% adicional
# -grupo familiar (tres o más):25% adicional
# Mostrar:
# -plan seleccionado
# -descuentos aplicables
# -total a pagar

print("1- plan basico : 2000")
print("2- plan intermedio : 3500")
print("3- plan premium : 5000")
plan_elegido= int(input("cual es tu plan?"))

costo_plan = 0

if  plan_elegido == 1:
    costo_plan = 2000
elif plan_elegido == 2:
    costo_plan = 3500
elif plan_elegido == 3:
    costo_plan =5000

costo_plan = int(input(f"costo_plan: {costo_plan}"))
print(1- pago anual : 20% de descuento )



