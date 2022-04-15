#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numero_inicial: int = int(input("Ingrese el primer numero: "))
numero_final: int = int(input("Ingrese el segundo numero: "))
numeros_impares: [int] = []

while numero_final <= numero_inicial:
    numero_final: int = int(input("El segundo numero debe sermayor al primero. Ingrese otro numero: "))

for i in range(numero_inicial, numero_final+1):
    if(i % 2 == 1):
        numeros_impares.append(i)

print(f"Lista de numeros impares entre {numero_inicial} y {numero_final}: ")
print(numeros_impares)

    