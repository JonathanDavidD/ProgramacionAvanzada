import tkinter as tk
from tkinter import messagebox
from typing import List
from excepciones import CantidadInvalidaException, PrecioInvalidoException, ProductoInvalidoException

class Producto:
    nombre:str
    precio:float
    cantidad:int


    def __init__(self,  nombre:str, precio:float, cantidad:int):

        if nombre == "":
            raise ProductoInvalidoException("Error")
        
        if precio<= 0:
            raise PrecioInvalidoException("Error")
        
        if cantidad< 0:
            raise CantidadInvalidaException("Error")
        
        
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad

    
    def calcular_valor(self):
        valortotal=self.precio*self.cantidad
        return valortotal
    
    def mostrar_info_productos(self):
        valor=self.calcular_valor()
        info=(f"Producto: {self.nombre}"),(f"\n Precio: {self.precio}"),(f"Cantidad: {self.cantidad}"),(f"Valor total: {valor}")


lista_productos:List[Producto]=[]

def agregar():
    try:
        nombre=entrynombre.get()
        precio=entryprecio.get()
        cantidad=entrycantidad.get()

        producto=Producto(nombre=nombre, precio=float(precio), cantidad=int(cantidad))
        lista_productos.append(producto)
        messagebox.showinfo("*", "Producto agregado")

    except ProductoInvalidoException as error:
        messagebox.showinfo(error, "El nombre del producto es incorrecto")

    except PrecioInvalidoException as error:
        messagebox.showinfo(error, "El precio del producto es incorrecto")

    except CantidadInvalidaException as error:
       messagebox.showinfo(error, "La cantidad de productos es incorrecta")

def mostrar():

    for producto in lista_productos:
        info = producto.mostrar_info_productos()
        
    messagebox.showinfo("Productos ", info)

  



ventana = tk.Tk()
ventana.title("Abarrotes")
ventana.geometry("225x225")
ventana.config(bg="deepskyblue2")

labelnombre= tk.Label(ventana, text="Nombre del producto", bg="lemon chiffon", font=("Georgia", 11, "bold"))
labelnombre.grid(row=0, column=1)
entrynombre= tk.Entry(ventana, bg="lavender", font=("Georgia", 11, "bold"))
entrynombre.grid(row=1, column=1)

labelprecio= tk.Label(ventana, text="Precio del producto", bg="lemon chiffon", font=("Georgia", 11, "bold"))
labelprecio.grid(row=2, column=1)
entryprecio= tk.Entry(ventana, bg="lavender", font=("Georgia", 11, "bold"))
entryprecio.grid(row=3, column=1)

labelcantidad= tk.Label(ventana, text="Cantidad de productos", bg="lemon chiffon", font=("Georgia", 11, "bold"))
labelcantidad.grid(row=4, column=1)
entrycantidad= tk.Entry(ventana, bg="lavender", font=("Georgia", 11, "bold"))
entrycantidad.grid(row=5, column=1)

boton1= tk.Button(ventana, text="Agregar producto", command=agregar, font=("Georgia", 11, "bold"),  relief="sunken", bg="mediumorchid1", fg="white")
boton1.grid(row=6, column=1)

boton2= tk.Button(ventana, text="Mostrar inventario", command=mostrar, font=("Georgia", 11, "bold"), relief="sunken", bg="mediumorchid1", fg="white")
boton2.grid(row=7, column=1)

ventana.mainloop()

   




