#Escribe un programa en la consola de python que pida al usuario su peso (en kg) 
#y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
#e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa 
#corporal calculado redondeado con dos decimales. 
#Tienes que subir capturas de pantalla en una carpeta comprimida zip.

kg = input('Ingrese su peso en kg')
68
estatura = input('Ingrese su estatura en mts')
1.71

estatura = float(estatura)
kg = float(kg)

estatura = estatura**2

masaCorporal = kg / estatura
masaCorporal = round(masaCorporal, 2)
masaCorporal = str(masaCorporal)

print('Tu índice de masa corporal es ' + masaCorporal)

