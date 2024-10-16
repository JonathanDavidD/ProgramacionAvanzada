from datetime import datetime
from zoologico.zoologico import Zoologico
from veterinarios.veterinario import Veterinario
from guias.guia import Guia
from visitantes.visitantes import Visitante
from zoologico.zoologico import Zoologico
from visitas.visita import Visita


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
            print("21.- Salir")
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

                
                
                
                #fecha_de_visitas=self.zoologico.listar_visita()
                #numero_visitas=self.zoologico.generar_fecha_de_visita(visita=visita)


                if ano < 2006:

                    Adulto=Visitante(nombre=nombre, apellido=apellido, curp=curp, ano=ano, mes=mes, dia=dia, id=id, fecha_nacimiento=fecha_nacimiento, fecha_de_registro=fecha_de_registro)
                    self.zoologico.registrar_visitante_adulto(Adulto)

                
                else:

                    Nino=Visitante(nombre=nombre, apellido=apellido, curp=curp, ano=ano, mes=mes, dia=dia, id=id, fecha_nacimiento=fecha_nacimiento, fecha_de_registro=fecha_de_registro)
                    self.zoologico.registrar_visitante_nino(Nino)



            elif opcion == "4":
                dia_v=input("Ingrese dia de la visita")
                mes_v=input("Ingrese mes de la visita")
                ano_v=input("Ingrese año de la visita")
                fecha_visita = datetime(dia_v,mes_v,ano_v)
                visita=Visita(fecha_visita)
                self.zoologico.registrar_visita(visita)    


            elif opcion == "5":
                pass


            elif opcion == "6":
                pass


            elif opcion == "7":
                print("\nMODIFIQUE LOS DATOS DE UN VETERINARIO\n")
            
            elif opcion == "8":
                print("\nMODIFIQUE LOS DATOS DE UN GUIA\n")


            elif opcion == "9":
                pass


            elif opcion == "10":
                pass


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
                pass


            elif opcion == "15":
                self.zoologico.mostrar_veterinarios()
            
            elif opcion == "16":
                self.zoologico.mostrar_guias()

            elif opcion == "17":
                self.zoologico.mostrar_visitantes()


            elif opcion == "18":
                pass


            elif opcion == "19":
                pass

            
            elif opcion == "20":
                pass
            
            elif opcion == "21":
                print("Hasta luego\n")
                break
          