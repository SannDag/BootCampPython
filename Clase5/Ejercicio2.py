#Escribe una función que pueda decirte si un número (número entero) es primo o no.

num: int = 0
print(input("Ingrese un numero entero: "))

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo, el", n, "es divisor")
            return False
    print("Es primo")
    return True

print(es_primo(num))