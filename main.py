from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime


while True:
    escuela=Escuela()
    print("***  MINDBOX  ***")
    print("1. Registrar estudiate")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Salir")

    opcion = input("Selecciona una opcion para continuar: ")

    if opcion =="1":

        numero_control= escuela.generar_numero_control()
        print(numero_control)


        print("Seleccionaste la opcion para registrar un estudiante")
        nombre=input("Ingresa el nombre del estudiante: ")
        apellido=input("Ingresa el apeliido del estudiante: ")
        curp=input("Ingresa la curp del estudiante: ")
        ano=int (input("Ingresa el año de nacimiento del estudiante: "))
        mes=int (input("Ingresa el mes de nacimiento del estudiante: "))
        dia=int (input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento=datetime(ano, mes, dia)

    elif opcion == "2":
        print("Seleccionaste la opcion para registrar un maestro")
        nombre=input("Ingresa el nombre: ")
        apellido=input("Ingresa el apellido: ")
        rfc=input("Ingresa el RFC: ")
        sueldo=input("Ingresa el sueldo: ")
        ano_nacimiento=input("Ingresa el año de nacimiento: ")

        numero_control_maestro=escuela.generar_numero_control_maestros(rfc=rfc, nombre=nombre, ano_nacimiento=ano_nacimiento)
        print(numero_control_maestro)
        #escuela.registrar_maestros(maestro)

        

    elif opcion == "3":
        print("Seleccionaste la opcion para registar una materia")
        nombre= input("Ingresa el nombre de la materia: ")
        descripcion=input("Ingresa la descripcion de la materia: ")
        semestre=input("Ingrese el semestre al que corresponde la materia: ")
        creditos=input("Ingrese los creditos de la materia: ")

        numero_control_materia=escuela.generar_numero_control_materia(nombre=nombre, semestre=semestre, creditos=creditos)
        print(numero_control_materia)
    
    elif opcion == "4":
        pass
    
    elif opcion == "5":
        pass
    
    elif opcion == "6":
        print("\n Hasta luego")
        break

    