# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input('Indique su edad por favor'))

if edad >= 18:
    print('Su edad es ' + str(edad) + ' por lo tanto usted es mayor de edad')
else:
    print('Usted es menor de edad porque tiene menos de 18 años')

