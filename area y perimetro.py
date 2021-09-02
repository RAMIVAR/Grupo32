#area y perimetro de un cuadrado
def area_perimetro (lado):
    area = lado * lado
    perimetro = lado * 4
    print("el area del cuadrado es: ",area)
    print("el perimetro del cuadrado es: ",perimetro)
area_perimetro(lado = int(input ("ingrese medida: ")))
