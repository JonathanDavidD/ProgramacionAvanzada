from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from semestre.semestre import Semestre
from carrera.carrera import Carrera
from grupos.grupos import Grupo
from datetime import datetime


class Menu:
  escuela: Escuela = Escuela()
  usuario_estudiante: str = "Juan123"
  contrasena_estudiante: str="12345"
  usuario_maestro: str = "Hilary123"
  contrasena_maestro: str="54321"

  def login(self):
        intentos = 0
        while intentos <5:
            print("*** BIENVENIDO ***")
            print("Inicia sesion para continuar")

            nombre_usuario=input("Ingresa el nombre de usuario: ")
            contrasena_usuario=input("Ingresa la contreaseña: ")

            if nombre_usuario == self.usuario_estudiante:
                if contrasena_usuario == self.contrasena_estudiante:
                    self.mostrar_menu_estudiante()
                    intentos=0
                else:
                    intentos=self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)

            elif nombre_usuario==self.usuario_maestro:
                if contrasena_usuario==self.contrasena_maestro:
                    self.mostrar_menu_maestro()
                    intentos=0

                else:
                    intentos=self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)

            else:
               intentos=self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)




  def mostrar_menu_estudiante(self):
        opcion = 0
        while opcion != 7: 
            print(" MINDBOX ")
            print("1. Ver maestros")
            print("2. Ver materias")
            print("3. Ver grupos")
            print("4. Ver horarios")
            print("5. Registrar materias")
            print("6. Registrar Horario")
            print("7. Salir")

            opcion=int(input("Ingresa una opcion: "))

            if opcion == 7:
                break

  def mostrar_menu_maestro(self):
        opcion=0
        while opcion !=5:
            print(" MINDBOX ")
            print("1. Ver horarios")
            print("2. Ver grupos")
            print("3. Ver materias")
            print("4. Ver alumnos")
            print ("5. Salir")

            opcion=int(input("Ingresa una opcion: "))

            if opcion == 5:
                break



  def mostrar_intento_sesion_fallido(self, intentos_usuario):
      print("Usuario o contraseña incorrecto")
      return intentos_usuario+1

  def mostrar_menu(self):
        while True:
        
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
            print("13. Registrar carrera")
            print("14. Registrar semestre")
            print("15. Mostrar carreras")
            print("16. Mostrar semestres")
            print("17. Mostrar grupos")
            print("18. Salir")

            opcion = input("Selecciona una opcion para continuar: ")

            if opcion =="1":

                print("Seleccionaste la opcion para registrar un estudiante")
                nombre=input("Ingresa el nombre del estudiante: ")
                apellido=input("Ingresa el apeliido del estudiante: ")
                curp=input("Ingresa la curp del estudiante: ")
                ano=int (input("Ingresa el año de nacimiento del estudiante: "))
                mes=int (input("Ingresa el mes de nacimiento del estudiante: "))
                dia=int (input("Ingresa el dia de nacimiento del estudiante: "))
                contrasenia=input("Ingresa la contraseña del estudiante: ")
                fecha_nacimiento=datetime(ano, mes, dia)
                numero_control= self.escuela.generar_numero_control()
                estudiante=Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, ano=ano, mes=mes, dia=dia,fecha_nacimiento=fecha_nacimiento, contrasena=contrasenia)
                self.escuela.registar_estudiante(estudiante)
                print("Se registro el alumno ")


            elif opcion == "2":
                print("Seleccionaste la opcion para registrar un maestro")
                nombre=input("Ingresa el nombre: ")
                apellido=input("Ingresa el apellido: ")
                rfc=input("Ingresa el RFC: ")
                sueldo=input("Ingresa el sueldo: ")
                ano_nacimiento=input("Ingresa el año de nacimiento: ")
                contrasenia=input("Ingresa la contraseña del maestro: ")
                numero_control_maestro=self.escuela.generar_numero_control_maestros(rfc=rfc, nombre=nombre, ano_nacimiento=ano_nacimiento)
                print(numero_control_maestro)
                maestro=Maestro(numero_control=numero_control, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo, ano_nacimineto=ano_nacimiento, contrasenia=contrasenia)
                self.escuela.registrar_maestros(maestro)

            

            elif opcion == "3":
                print("Seleccionaste la opcion para registar una materia")
                nombre= input("Ingresa el nombre de la materia: ")
                descripcion=input("Ingresa la descripcion de la materia: ")
                semestre=input("Ingrese el semestre al que corresponde la materia: ")
                creditos=input("Ingrese los creditos de la materia: ")
            
                self.escuela.registrar_materia()
                numero_control_materia=self.escuela.generar_numero_control_materia(nombre=nombre, semestre=semestre, creditos=creditos)
                print(numero_control_materia)
                materia=Materia(nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)
                self.escuela.registrar_materia(materia)


            elif opcion =="4":
                print("Seleccionaste la opcion para registrar un nuevo grupo")
                tipo=input("Ingresa el tipo de grupo (A/B)")
                id_semestre=input("Ingresa el id del semestre al que pertenece el grup0")
                grupo=Grupo(tipo=tipo, id_semestre=id_semestre)
                self.escuela.registrar_grupo(grupo=grupo)
        
            elif opcion == "6":
                print("Estudiantes en el sistema")
                self.escuela.listar_estudiantes(estudiante)

            elif opcion == "7":
                print("Maestros en el sistema")
                self.escuela.listar_maestros(maestro)

            elif opcion == "8":
                print("Materias en el sistema")
                self.escuela.listar_materias(materia)
        

            elif opcion == "9":
                pass


            elif opcion == "10":
                print("Selecci0naste la opcion para eliminar un estudiante")
                numero_control=input("Ingresa el numero de control del estudiante: ")
                self.escuela.eliminar_estudiante(numero_control=numero_control)

            elif opcion == "11":
                print("Seleccionaste la opcion para eliminar un maestro")
                numero_control=input("Ingresa el numero de control del maestro: ")
                self.escuela.eliminar_maestro(numero_control=numero_control)

            elif opcion == "12":
                print("Seleccionaste la opcion para eliminar una materia")
                numero_control=input("Ingresa el numero de control de la materia: ")
                self.escuela.eliminar_materia(numero_control=numero_control) 
        
            elif opcion == "13":
                print("Seleccionaste la opcion para registrar una carrera")
                nombre=input("Ingresa el nombre de la carrera")
                carrera= Carrera(nombre=nombre)


            elif opcion =="14":
                print("Seleccionaste la opcion para registrar un semestre")

                numero=input("Ingresa edl numero de semestre")
                id_carrera=input("Ingresa el ID de la carrera")

                semestre= Semestre(numero=numero, id_carrera=id_carrera)
                self.escuela.registrar_semestre(semestre=semestre)

            elif opcion =="15":
                print("Carreras en el sistema")
                self.escuela.listar_carreras(carrera)
    
            elif opcion =="18":
                break

    