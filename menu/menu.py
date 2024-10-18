from datetime import datetime
from zoologico.zoologico import Zoologico
from empleados.empleados import Empleado
from visitantes.visitantes import Visitante
from zoologico.zoologico import Zoologico
from visitas.visita import Visita
from mantenimientos.mantenimiento import Mantenimiento
from animales.animales import Animal

class Menu:
    zoologico = Zoologico()
    
        
    def mostrar_menu(self):
        while True:
            print("** MENU PRINCIPAL **")
            print("1.- Registrar empleado")
            print("2.- Registrar visitante")
            print("3.- Registrar visita")
            print("4.- Registrar animal")
            print("5.- Registrar mantenimientos")
            print("6.- Modificar datos empleado")
            print("7.- Modificar datos visitante")
            print("8.- Modificar datos animal")
            print("9.- Eliminar empleado")
            print("10.- Eliminar visitante")
            print("11.- Eliminar animal")
            print("12.- Mostrar empleado")
            print("13.- Mostrar visitantes")
            print("14.- Mostrar visitas")
            print("15.- Mostrar animal")
            print("16.- Mostrar mantenimientos")
            print("17.- Agregar visitante a visita")
            print("18.- Salir")
            opcion = input("Ingrese la opcion de lo que desea realizar: ")

            if opcion == "1":
                print("\nINGRESE DATOS DEL EMPLEADO")
                nombre = str(input("Ingrese el nombre del empleado: "))
                apellido = str(input("Ingrese el apellido del empleado: "))
                curp = str(input("Ingrese la curp del empleado: "))
                dia = int(input("Ingrese el dia de nacimiento: "))
                mes = int(input("Ingrese el mes de nacimeinto: "))
                anio = int(input("Ingrese el año de nacimiento: "))
                dia_ingreso = int(input("Ingrese el dia de ingreso al empleo: "))
                mes_ingreso = int(input("Ingrese el mes de ingreso al empleo: "))
                anio_ingreso = int(input("Ingrese el año de ingreso al empleo: "))
                rfc = str(input("Ingrese el rfc del empleado: "))
                salario = float(input("Ingrese el salario del empleado: "))
                id = self.zoologico.generar_id_empleado(apellido=apellido,rfc=rfc)
                # horario = str(input("Ingrese el horario de trabajo: "))
                
                fecha_nacimiento = datetime(anio, mes, dia)
                fecha_ingreso = datetime(anio_ingreso,mes_ingreso,dia_ingreso)
                empleado = Empleado(nombre=nombre,apellido=apellido,id=id,curp=curp,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,rfc=rfc,salario=salario)
                self.zoologico.registrar_empleado(empleado=empleado)
                
            elif opcion == "2":
                print("\nINGRESE DATOS DEL VISITANTE")
                nombre = input("Ingresa NOMBRE(S) del visitante -> ")
                apellido = input("Ingresa PRIMER APELLIDO del visitante -> ")
                curp = input("Ingresa CURP del visitante -> ")
                ano = int(input("Ingresa AÑO DE NACIMIENTO del visitante -> "))
                mes = int(input("Ingresa MES DE NACIMIENTO del visitante -> "))
                dia = int(input("Ingresa DIA DE NACIMIENTO del visitante -> "))
                fecha_nacimiento = datetime(ano, mes, dia)
                ano_registro = int(input("Ingresa AÑO DE REGISTRO del visitante -> "))
                mes_registro = int(input("Ingresa MES DE REGISTRO del visitante -> "))
                dia_registro = int(input("Ingresa DIA DE REGISTRO del visitante -> "))
                fecha_de_registro = datetime(ano_registro, mes_registro, dia_registro)
                id = self.zoologico.generar_id_visitantes(apellido=apellido)
                print(id)

                visitante = Visitante(nombre=nombre, apellido=apellido, curp=curp, id=id, fecha_nacimiento=fecha_nacimiento, fecha_de_registro= fecha_de_registro, ano=ano)
                
                #fecha_de_visitas=self.zoologico.listar_visita()
                #numero_visitas=self.zoologico.generar_fecha_de_visita(visita=visita)

                if ano < 2006:
                    adulto = visitante
                    self.zoologico.registrar_visitante_adulto(adulto= adulto)
                else:
                    nino = visitante
                    self.zoologico.registrar_visitante_nino(Nino=nino)

            elif opcion == "3":

                
                dia_v=int(input("Ingrese dia de la visita"))
                mes_v=int(input("Ingrese mes de la visita"))
                ano_v=int(input("Ingrese año de la visita"))
                fecha_visita = datetime(ano_v, mes_v, dia_v)
                id_visitante = input("Ingresa el id del visitante")
                guia_a_cargo=input("Ingrese el id del guia a cargo")
                id=self.zoologico.generar_id_visita()
                print(id)
                
                visita=Visita(fecha_visita=fecha_visita, guia_a_cargo=guia_a_cargo,id_visitante=id_visitante, id=id )

                self.zoologico.registrar_visita(visita)
                    
            elif opcion == "4":
                print("\nINGRESE DATOS DEL ANIMAL")
                tipo=str(input("Ingrese el tipo de animal: "))
                dia_ingreso=int(input("Ingrese del dia de llegada: "))
                mes_ingreso=int(input("Ingrese del mes de llegada: "))
                anio_ingreso=int(input("Ingrese del año de llegada: "))
                enfermedades=str(input("Ingrese las enfermedades del animal: "))
                tipo_alimentacion=str(input("Ingrese el tipo de alimentacion: "))
                dia=int(input("Ingrese el dia de nacimiento: "))
                mes=int(input("Ingrese el mes de nacimiento: "))
                anio=int(input("Ingrese el año de nacimiento: "))
                peso=float(input("Ingrese el peso del animal: "))
                frecuencia_alimentacion=str(input("Ingresa la frecuencia de alimentacion: "))
                vacunas=bool(input("El animal tiene vacvunas: "))

                fecha_llegada=datetime(anio_ingreso, mes_ingreso, dia_ingreso)
                fecha_de_nacimiento=datetime(anio, mes, dia)

                animal=Animal(tipo=tipo,fecha_llegada=fecha_llegada, enfermedades=enfermedades, tipo_alimentacion=tipo_alimentacion, fecha_nacimiento=fecha_de_nacimiento, peso=peso, frecuencia_alimentacion=frecuencia_alimentacion, vacunas=vacunas)
                self.zoologico.registrar_animal(animal)

            elif opcion == "5":
                print("\nREGISTRE ALGUN MANTENIMIENTO\n")
                #empleado_encargado
                proceso_realizado = input("Ingrese el proceso que se llevo a cabo: ")
                observaciones = input("Ingrese algunas observaciones que se tienen que tomar en cuenta en el mantenimiento: ")
                id_animal = input("Ingrese el ID de un animal: ")
                dia_proceso = int(input("Ingrese el dia en el que se realizo el mantenimiento: "))
                mes_proceso = int(input("Ingrese el mes en el que se realizo el mantenimiento: "))
                anio_proceso = int(input("Ingrese el año en el que se realizo el mantenimiento: "))
                fecha_proceso = datetime(anio_proceso, mes_proceso, dia_proceso)
                
                mantenimiento = Mantenimiento(proceso_realizado=proceso_realizado,observaciones=observaciones,id_animal=id_animal,fecha_proceso=fecha_proceso)
                self.zoologico.registrar_mantenimiento(mantenimiento)

            elif opcion == "6":
                print("\nMODIFICAR EMPLEADO\n")
                id_empleado = input("Ingrese el ID del empleado que desea modificar la informacion: ")
                self.zoologico.modificar_datos_empleado(id_empleado= id_empleado)
            
            elif opcion == "7": #MODIFICAR DATOS DE VISITANTE
                 print("\nMODIFICAR VISITANTE\n")
                 id_visitante = input("Ingrese el ID del empleado que desea modificar la informacion: ")
                 self.zoologico.modificar_datos_visitante(id_visitante= id_visitante)

            elif opcion == "8":
                print("MODIFICAR ANIMAL")
                id_animal=input("Ingrese el ID del animal: ")
                self.zoologico.modificar_datos_animal(id_animal=id_animal)

            elif opcion == "9":
                print("\nELIMINE UN EMPLEADO\n")
                id_empleado = str(input("Coloque el ID del empleado que desea eliminar: "))
                self.zoologico.eliminar_empleado(id_empleado= id_empleado)
            
            elif opcion == "10":
                print("\nELIMINE UN VISITANTE\n")
                id = str(input("Coloque el ID del VISITANTE que desea eliminar: "))
                self.zoologico.eliminar_visitante(id=id)

            elif opcion == "11":
                print("ELIMINAR UN ANIMAL")
                id_animal=str(input("Ingrese el ID del animal a eliminar: "))
                self.zoologico.eliminar_animal(id_animal=id_animal)                

            elif opcion == "12":
                self.zoologico.mostrar_empleados()
            
            elif opcion == "13":
                self.zoologico.mostrar_visitantes()

            elif opcion == "14": #MOSTRAR VISITAS
                self.zoologico.mostrar_visitas()

            elif opcion == "15":
                self.zoologico.mostrar_animal()

            elif opcion == "16":
                self.zoologico.mostrar_mantenimiento()
            
            elif opcion == "17":
                id_v_a= input("Ingresa id del visitante")
                id_vt= input("Ingresa el id de la visita")

                self.visita.ingresar_visitantes(id_v_a=id_v_a, id_vt=id_vt)

            elif opcion == "18":
                print("Hasta luego\n")
                break