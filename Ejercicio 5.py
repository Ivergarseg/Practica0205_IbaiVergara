'''Escribir una función que reciba una muestra de números en una 
lista y devuelva otra lista con sus valores al cuadrado.'''

def lista_cuadrada(num_lista):
    lista_cuadrada1 = []
    for num in num_lista:
        lista_cuadrada1.append(num**2)
    return lista_cuadrada1

cadena = input('Ingrese una lista de números separados por espacios: ')
lista_str = cadena.split(' ')
num_list = [int(elemento) for elemento in lista_str]

print(lista_cuadrada(num_list))