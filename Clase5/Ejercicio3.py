#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)): 
    print("El año ingresado es bisiesto")
else: 
    print("El año ingresado no es bisiesto")


