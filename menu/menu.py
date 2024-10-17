from datetime import datetime
from zoologico.zoologico import Zoologico
from veterinarios.veterinario import Veterinario
from guias.guia import Guia
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
            print("1.- Registrar veterinario")
            print("2.- Registrar guia")
            print("3.- Registrar visitante")
            print("4.- Registrar visita")
            print("5.- Registrar animal")
            print("6.- Registrar mantenimientos")
            print("7.- Modificar datos veterinario")
            print("8.- Modificar datos guia")
            print("9.- Modificar datos visitante")
            print("10.- Modificar datos animal")
            print("11.- Eliminar veterinario")
            print("12.- Eliminar guia")
            print("13.- Eliminar visitante")
            print("14.- Eliminar animal")
            print("15.- Mostrar veterinario")
            print("16.- Mostrar guia")
            print("17.- Mostrar visitantes")
            print("18.- Mostrar visitas")
            print("19.- Mostrar animal")
            print("20.- Mostrar mantenimientos")
            print("21.- Agregar visitante a visita")
            print("22.- Salir")
            opcion = input("Ingrese la opcion de lo que desea realizar: ")


            if opcion == "1":
                print("\nINGRESE DATOS DEL VETERINARIO")
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
                veterinario = Veterinario(nombre=nombre,apellido=apellido,id=id,curp=curp,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,rfc=rfc,salario=salario)
                self.zoologico.registrar_veterinario(veterinario=veterinario)
                
            if opcion == "2":
                print("\nINGRESE DATOS DEL GUIA")
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
                guia = Guia(nombre=nombre,apellido=apellido,id=id,curp=curp,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,rfc=rfc,salario=salario)
                self.zoologico.registrar_guia(guia=guia)
                
            elif opcion == "3":
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



            elif opcion == "4":

                
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
                    


            elif opcion == "5":
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

                


            elif opcion == "6":
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


            elif opcion == "7":
                print("\nMODIFIQUE LOS DATOS DE UN VETERINARIO\n")
                id_veterinario = input("Ingrese el ID del veterinario que desea modificar la informacion: ")
                self.zoologico.modificar_datos_veterinario(id_veterinario=id_veterinario)
            
            elif opcion == "8":
                print("\nMODIFIQUE LOS DATOS DE UN GUIA\n")
                id_guia = input("Ingrese el ID del guia que desea modificar la informacion: ")
                self.zoologico.modificar_datos_guia(id_guia=id_guia)


            elif opcion == "9":
                pass


            elif opcion == "10":
                print("MODIFICAR ANIMAL")
                id_animal=input("Ingrese el ID del animal: ")
                self.zoologico.modificar_datos_animal(id_animal=id_animal)



            elif opcion == "11":
                print("\nELIMINE UN VETERINARIO\n")
                id_veterinario = str(input("Coloque el ID del veterinario que desea eliminar: "))
                self.zoologico.eliminar_veterinario(id_veterinario=id_veterinario)
            
            elif opcion == "12":
                print("\nELIMINE UN GUIA\n")
                id_guia = str(input("Coloque el ID del guia que desea eliminar: "))
                self.zoologico.eliminar_guia(id_guia=id_guia)

            elif opcion == "13":
                print("\nELIMINE UN VISITANTE\n")
                id = str(input("Coloque el ID del VISITANTE que desea eliminar: "))
                self.zoologico.eliminar_visitante(id=id)


            elif opcion == "14":
                print("Eliminar animal")
                id_animal=str(input("Ingrese el ID del animal a eliminar: "))
                self.zoologico.eliminar_animal(id_animal=id_animal)                

            elif opcion == "15":
                self.zoologico.mostrar_veterinarios()
            
            elif opcion == "16":
                self.zoologico.mostrar_guias()

            elif opcion == "17":
                self.zoologico.mostrar_visitantes()


            elif opcion == "18":
                pass


            elif opcion == "19":
                self.zoologico.mostrar_animal()

            
            elif opcion == "20":
                self.zoologico.mostrar_mantenimiento()
            
            elif opcion == "21":
                id_v_a= input("Ingresa id del visitante")
                id_vt= input("Ingresa el id de la visita")

                self.visita.ingresar_visitantes(id_v_a=id_v_a, id_vt=id_vt)

          
            elif opcion == "22":
                print("Hasta luego\n")
                break