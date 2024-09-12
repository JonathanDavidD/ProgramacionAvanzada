from circulo import Circulo 


circulo_uno = Circulo(10)
circulo_dos = Circulo(12)
circulo_tres = Circulo(6)

print("El radio de circulo uno es: ",circulo_uno.radio)
print("El area del circulo uno es: ",circulo_uno.calcular_area())
print("El perimetro del circulo uno es: ",circulo_uno.calcular_perimetro())

print("\n")
print("El radio de circulo dos es: ",circulo_dos.radio)
print("El area del circulo dos es: ",circulo_dos.calcular_area())
print("El perimetro del circulo dos es: ",circulo_dos.calcular_perimetro())


print("\n")
print("El radio de circulo tres es: ",circulo_tres.radio)
print("El area del circulo tres es: ",circulo_tres.calcular_area())
print("El perimetro del circulo tres es: ",circulo_tres.calcular_perimetro())
