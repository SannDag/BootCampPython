#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función #que calcule el área de un círculo recibiendo el radio del mismo.

import math

def calculo_area_triangulo(base, altura):
    resultado = (base * altura) / 2
    return resultado

print(f"El area del triangulo es: {round(calculo_area_triangulo(8, 10), 2)}")    

def calculo_area_circulo(radio):
    radio = math.pow(radio, 2)
    pi = math.pi
    resultado = pi * radio
    return resultado

print(f"El area del circulo es: {round(calculo_area_circulo(6), 2)}")