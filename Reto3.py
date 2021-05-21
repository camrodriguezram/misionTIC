#-------------------------INICIALIZACION DE VARIABLES-----------------------------
dias = 0
maxTotal= 0
minTotal = 0
errorTempMax = 0
errorTempMin = 0
ErrorAmbosValores = 0
diasTotales = 0
#-----------------------------ITERACION------------------------------------------
while True:
    #input de temperaturas
    temp_max = float(input("Ingrese la temperatura máxima > "))
    temp_min = float(input("Ingrese la temperatura mínima > "))
    #Test a variables en caso de terminar el programa
    if temp_max == 0 and temp_min == 0:
        break
    #Test en caso e que la temperatura maxima sea menor a la minima
    if temp_max<temp_min:
        print("La temperatura maxima es menor a la minima, Ingrese los valores nuevamente en el orden correcto")
        continue
     #Revisar si ambas temperaturas son erroneas
    if (temp_max > 35 or temp_max < 5) and (temp_min < 5 or temp_min > 35):
        ErrorAmbosValores= ErrorAmbosValores +1
        continue
    #Revisar si la temperatura maxima esta en el rango
    elif temp_max > 35 or temp_max < 5:
        errorTempMax = errorTempMax +1
        minTotal = minTotal + temp_min
        continue
    #Revisar si la temperatura minima esta en el rango
    elif temp_min < 5 or temp_min > 35:
        errorTempMin = errorTempMin +1
        maxTotal = maxTotal + temp_max
        continue
    
    #contador para los dias de la salida de campo
    dias = dias +1

    #suma de temperaturas
    maxTotal = maxTotal + temp_max
    minTotal = minTotal + temp_min
#-------------------OPERACIONES Y VALIDACIONES INTERNAS-------------------------------------

#dias+ErrorAmbosValores+errorTempMax+errorTempMin
diasTotales = dias+ErrorAmbosValores+errorTempMax+errorTempMin
#Promedio temperatura maxima
if (dias+errorTempMin) == 0:
    tempMaxAvg = 0
else:
    tempMaxAvg = round(maxTotal/(dias+errorTempMin),2)
#Promedio temperatura minima dias son donde ambos datos son validos mas donde solo el dato erroneo fue temp max
if (dias+errorTempMax) == 0:
    tempMinAvg = 0
else:
    tempMinAvg = round(minTotal/(dias+errorTempMax),2)
#Porcentaje dias correctos a error
diasConErrores = errorTempMax + errorTempMin + ErrorAmbosValores
porcentajeDias = round((diasConErrores/(diasConErrores+dias))*100,1)


#------------------------Muestra de resultados----------------------------------

print("******************************* RESULTADOS **************************************\n")
print(f"Numero de dias registados en la salida de campo es: {diasTotales}")
#Numero de dias con Error 
# Preguntar si es exclueyente es decir si hubo un error en ambas temperaturas tambien cuenta el maxima solo
print(f"Numero de dias donde se registro un error unicamente en la temperatura máxima: {errorTempMax}")
print(f"Numero de dias donde se registro un error unicamente en la temperatura mínima: {errorTempMin}")
print(f"Numero de dias donde se registro un error en la temperatura máxima y mínima: {ErrorAmbosValores}")
#media de temperaturas
print(f"La temperatura media máxima fue de: {tempMaxAvg}")
print(f"La temperatura media mínima fue de: {tempMinAvg}")
#Porcentaje de errores con respeto a los dias
print(f"El porcentaje de errores con respecto a los dias es : {porcentajeDias}%\n")
print("*********************************************************************************")
