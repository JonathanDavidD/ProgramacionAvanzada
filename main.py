from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia

while True:
    escuela=Escuela()
    print ("\n")
    print("***  MINDBOX  ***")
    print("1. Registrar estudiate")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiante")
    print("7. Mostrar maestros")
    print("8. Mostrar materias")
    print("9. Mostrar grupos")
    print("10. eliminar estudiantes")
    print("11. Eliminar maestros")
    print("12. Eliminar materias")
    print("13. Salir")

    opcion = input("Selecciona una opcion para continuar: ")

    if opcion =="1":

        print("Seleccionaste la opcion para registrar un estudiante")
        nombre=input("Ingresa el nombre del estudiante: ")
        apellido=input("Ingresa el apeliido del estudiante: ")
        curp=input("Ingresa la curp del estudiante: ")
        ano=int (input("Ingresa el año de nacimiento del estudiante: "))
        mes=int (input("Ingresa el mes de nacimiento del estudiante: "))
        dia=int (input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento=datetime(ano, mes, dia)
        numero_control= escuela.generar_numero_control()
        estudiante=Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, ano=ano, mes=mes, dia=dia,fecha_nacimiento=fecha_nacimiento)
        escuela.registar_estudiante(estudiante)
        print("Se registro el alumno ")


    elif opcion == "2":
        print("Seleccionaste la opcion para registrar un maestro")
        nombre=input("Ingresa el nombre: ")
        apellido=input("Ingresa el apellido: ")
        rfc=input("Ingresa el RFC: ")
        sueldo=input("Ingresa el sueldo: ")
        ano_nacimiento=input("Ingresa el año de nacimiento: ")

        numero_control_maestro=escuela.generar_numero_control_maestros(rfc=rfc, nombre=nombre, ano_nacimiento=ano_nacimiento)
        print(numero_control_maestro)
        maestro=Maestro(numero_control=numero_control, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo, ano_nacimineto=ano_nacimiento)
        escuela.registrar_maestros(maestro)

        

    elif opcion == "3":
        print("Seleccionaste la opcion para registar una materia")
        nombre= input("Ingresa el nombre de la materia: ")
        descripcion=input("Ingresa la descripcion de la materia: ")
        semestre=input("Ingrese el semestre al que corresponde la materia: ")
        creditos=input("Ingrese los creditos de la materia: ")
        
        escuela.registrar_materia()
        numero_control_materia=escuela.generar_numero_control_materia(nombre=nombre, semestre=semestre, creditos=creditos)
        print(numero_control_materia)
        materia=Materia(nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)
        escuela.registrar_materia(materia)
    
    elif opcion == "6":
        print("Estudiantes en el sistema")
        escuela.listar_estudiantes(estudiante)

    elif opcion == "7":
        print("Maestros en el sistema")
        escuela.listar_maestros(maestro)

    elif opcion == "8":
        print("Materias en el sistema")
        escuela.listar_materias(materia)
    

    elif opcion == "9":
        pass


    elif opcion == "10":
        print("Selecci0naste la opcion para eliminar un estudiante")
        numero_control=input("Ingresa el numero de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control=numero_control)

    elif opcion == "11":
        print("Seleccionaste la opcion para eliminar un maestro")
        numero_control=input("Ingresa el numero de control del maestro: ")
        escuela.eliminar_maestro(numero_control=numero_control)

    elif opcion == "12":
        print("Seleccionaste la opcion para eliminar una materia")
        numero_control=input("Ingresa el numero de control de la materia: ")
        escuela.eliminar_materia 
    
    elif opcion == "13":
        print("\n Hasta luego")
        break

    