from datetime import datetime
from empleados.empleado import Empleado

class Menu:
    
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
            print("12.- Mostrar empleados")
            print("13.- Mostrar visitantes")
            print("14.- Mostrar visitas")
            print("15.- Mostrar animal")
            print("16.- Mostrar mantenimientos")
            print("17.- Salir")
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
                # horario = str(input("Ingrese el horario de trabajo: "))
                
                fecha_nacimiento = datetime(dia,mes,anio)
                fecha_ingreso = datetime(dia_ingreso,mes_ingreso,anio_ingreso)
                empleado = Empleado(nombre=nombre,apellido=apellido,curp=curp,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,rfc=rfc,salario=salario)

            elif opcion == "2":
                pass

            elif opcion == "3":
                pass    


            elif opcion == "4":
                pass


            elif opcion == "5":
                pass


            elif opcion == "6":
                print("\nMODIFIQUE LOS DATOS DE UN EMPLEADO\n")


            elif opcion == "7":
                pass


            elif opcion == "8":
                pass


            elif opcion == "9":
                print("\nELIMINE UN EMPLEADO\n")


            elif opcion == "10":
                pass


            elif opcion == "11":
                pass


            elif opcion == "12":
                print("\n** EMPLEADOS **\n")


            elif opcion == "13":
                pass


            elif opcion == "14":
                pass


            elif opcion == "15":
                pass

            
            elif opcion == "16":
                pass
            
            elif opcion == "17":
                print("Hasta luego\n")
                break
          