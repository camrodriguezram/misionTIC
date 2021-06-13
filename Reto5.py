import os
import json
import ast
#-----------Creacion archivo-----------
#agenda = open("agenda.txt","w")
#agenda.close()
#json
directorio = {}
#with open("agenda.txt") as f:
#    data = f.read()
#    directorio = ast.literal_eval(data)

 #Borrar datos del archivo
#archivo= open("agenda.txt","r+")
#archivo.truncate(0)
#archivo.close   
#-----------Funciones-----------


#Funcion para crear archivo
def crearArchivo():
    agenda = open("agenda.txt","w")
    agenda.close()
    print("Archivo agenda.txt creado")


#Funcion para buscar un celular con el nombre
def buscador():
    buscar = input("Digite el nombre del beneficiario: ")
    try:
        datosBeneficiario=directorio[buscar]
        print("El celular de "+buscar+" "+datosBeneficiario[0]+" es "+datosBeneficiario[1])
    except:
        print("Usuario no encontrado")


#Funcion para gregar un usuario
def addUser():
    new = 0
    archivo = open("agenda.txt","a")
    nombre = input("Ingrese el nombre del beneficiario: ")
    apellido = input ("Ingrese el apellido del beneficiario: ")
    cedula = input("Ingrese numero de cedula del beneficiario: ")
    celular = input("Ingrese el numero de celular: ")
    for i in directorio:
        usuario=directorio[i]
        if usuario[2]==cedula:
            print("Ya se encuentra un beneficiario con la cedula digitada")
            new = 1
    if new == 0:
        directorio[nombre] = [apellido,celular,cedula]
        archivo.write("Nombre: "+nombre+" "+apellido+"\r")
        archivo.write("Celular: "+celular+"\r")
        archivo.write("Cedula: "+cedula+"\r")
        archivo.write("\r")
        archivo.close
        print("Beneficiario agregado")

#Funcion para mostrar todos los usuarios en la agenda
def showAll():
    for i in directorio:
        datosBeneficiario=directorio[i]
        print(i + " "+datosBeneficiario[0])
        print(datosBeneficiario[2])
        print(datosBeneficiario[1])
        

#Funcion para eliminar un usuario
def deleteUser():
    eliminar= input("Digite la cedula del usuario a eliminar: ")
    for i in directorio:
        datosBeneficiario=directorio[i]
        if datosBeneficiario[2] == eliminar:
            delete = i
    try:
        del directorio[delete]
        print("Usuario eliminado ")
        archivo= open("agenda.txt","r+")
        archivo.truncate(0)
        archivo.close
        archivo = open("agenda.txt","a")
        for i in directorio:
            datosBeneficiario=directorio[i]
            archivo.write("Nombre: "+i+"\r")
            archivo.write("Apellido: "+datosBeneficiario[0]+"\r")
            archivo.write("Celular: "+datosBeneficiario[1]+"\r")
            archivo.write("Cedula: "+datosBeneficiario[2]+"\r")
            archivo.write("\r")
        archivo.close
        #with open("agenda.txt", "w") as file:
        #    file.write(json.dumps(directorio))
    except:
        print("Usuario no encontrado")

#Funcion para imprimir solo los usuario que contengan una inicial en especifico
def usuarioPorLetra():
    letra = input("Ingrese letra: ")
    print("Beneficiarios con la letra "+letra+": ")
    for i in directorio:
        if i[0] == letra:
            datosBeneficiario=directorio[i]
            print("\r")
            print(i+" "+datosBeneficiario[0])
            print(datosBeneficiario[2])
            print(datosBeneficiario[1])
            
        
#--------------MENU--------------
while True:
    print("\r")
    print("       **************************** MENU ***************************************")
    print("       *         1. Crear archivo                                              *")
    print("       *         2. Buscar numero de celular de un beneficiario                *")
    print("       *         3. Ingresar nuevo beneficiario                                *")
    print("       *         4. Borrar un beneficiario                                     *")
    print("       *         5. Mostrar todos los beneficiarios                            *")
    print("       *         6. Mostar los beneficiarios que inician con letra digitada    *")
    print("       *         7. Salir                                                      *")
    print("       *************************************************************************")
    print("\r")
    try:
        option = int(input("Digite numero de opcion deseada: "))
        if option == 7:
            #Borrar usuarios en el archivo 
            archivo= open("agenda.txt","r+")
            archivo.truncate(0)
            archivo.close
            break
        elif option == 1:
            crearArchivo()
        elif option == 2:
            buscador()
        elif option == 3:
            addUser()
        elif option == 4:
            deleteUser()
        elif option == 5:
            print("BENEFICIARIOS INSCRITOS: ")
            print("\r")
            showAll()
            print("\r")
        elif option == 6:
            usuarioPorLetra()
        else:
            print("opcion no valida digite nueva opcion")
    except:
        print("Opcion no valida Ingeres un numero")


