#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

num1: int = 1
num2: int = 100
num_ordenadoInverso: [int] = []

for i in reversed(range(num1, num2+1)):
    num_ordenadoInverso.append(i)

print(num_ordenadoInverso)
