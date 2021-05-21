nombre = input("Digite su Nombre: ")
apellido= input("Digite su apellido: ")
edad = int(input("Digite su edad: "))
examen = float(input("Digite el puntaje obtenido en el examen: "))
ingresos = float(input("Digite ingreso familiar dado por salarios minimos: "))

#descuentoEdad esta dado por la edad del estudiante
if 15 <= edad <= 18:
    descuentoEdad = 25
elif 19 <= edad <= 21:
    descuentoEdad = 15
elif 22 <= edad <= 25:
    descuentoEdad = 10
else:
    descuentoEdad = 0

#descuentoIngresos esta dado por el ingreso familiar
if ingresos <= 1:
    descuentoIngresos= 30
elif 1 < ingresos <= 2:
    descuentoIngresos=20 
elif 2 < ingresos <=3:
    descuentoIngresos=10
elif 3<ingresos<=4:
    descuentoIngresos=5
else:
    descuentoIngresos= 0
#descuentoExamen dado por puntaje
if examen >= 96:
    descuentoExamen= 45
elif 91 <= examen <96:
    descuentoExamen=40 
elif 86 <= examen < 91:
    descuentoExamen=35
elif 80<=examen<86:
    descuentoExamen=30
else:
    descuentoExamen= 0

#Suma de descuentos
total=descuentoEdad+descuentoIngresos+descuentoExamen

print("---------------")
print("Los descuentos obtenidos por",nombre.upper(), apellido.upper(), "son:")
print("Descuento por Edad:",descuentoEdad,"%" )
print("Descuento por Ingresos: ", descuentoIngresos,"%")
print("Descuento por Examen: ", descuentoExamen,"%")
print("Descuento total: ", total,"%")

