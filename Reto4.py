
def sueldo_bruto(precio, horas):
    if horas > 40:
        horasExtra= horas-40
        sueldo_brutototal = (40*precio) + (horasExtra*(precio*1.5))
    else:
        sueldo_brutototal = horas*precio
    return sueldo_brutototal

def descuentos(sueldo):
    parafiscales = sueldo*0.09
    salud = sueldo * 0.04
    pension = sueldo * 0.04
    #descuento = parafiscales+salud+pension
    print(f"Parafiscales: $ {parafiscales}")
    print(f"Salud: $ {salud}")
    print(f"Pension: $ {pension}")
    return parafiscales+salud+pension

def sueldo_neto(sueldo,descuento):
    return(sueldo-descuento)


def calculoProvisiones(sueldoBruto):
    prima = sueldoBruto * 0.0833
    cesantias = sueldoBruto * 0.0833
    interesCesantias = cesantias * 0.01
    vacaciones = sueldoBruto * 0.0417
    print(f"Prima: $ {prima}")
    print(f"Cesantias: $ {cesantias}")
    print(f"Intereses cesantias: $ {interesCesantias}")
    print(f"Vacaciones: $ {vacaciones}")
    return (prima+cesantias+interesCesantias+vacaciones)



nombre = input("Digite el Nombre del Docente: ")
horas = int(input("Digite las horas laboradas: "))
precio = int(input("Digite el valor por hora: "))

print("--------------- Resultados ---------------")
sueldo = sueldo_bruto(precio,horas)
print(f"El Sueldo bruto es: $ {sueldo}")
print("---   DESCUENTOS   ---")
descuento = descuentos(sueldo)
print(f"Descuento totales: $ {descuento}")
sueldoNeto = sueldo_neto(sueldo,descuento)
print(f"Sueldo Neto: $ {sueldoNeto}")
print("---   PROVISIONES   ---")
provisiones = calculoProvisiones(sueldo)
print(f"Provisiones totales : $ {provisiones} ")


