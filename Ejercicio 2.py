'''Escribir una función que reciba un número entero positivo y devuelva su factorial. 
Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.'''

numero = int(input('Ingrese un numero: '))
solucion = 1

for i in range(1, numero + 1):
    solucion = solucion * i

print(solucion)

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
print(factorial(numero))