#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#Color
#Ruedas
#Puertas

class Vehiculo:   
    color = "Azul"    
    ruedas: int = 4
    puertas: int = 5

#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#Velocidad
#Cilindrada

class Coche(Vehiculo):
    velocidad: float = 110.5
    cilindrada: float = 1.6

#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

miCoche = Coche()

print('Color: ' + (str(miCoche.color)))
print('Cantidad de ruedas: ' + (str(miCoche.ruedas)))
print('Cantidad de puertas: ' + (str(miCoche.puertas)))
print('Cilindrada:' + (str(miCoche.cilindrada)))

