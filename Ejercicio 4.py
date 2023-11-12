'''Escribir una función que reciba una muestra 
de números en una lista y devuelva su media.'''

def media(lista_int):
    '''Recibe una lista de números y devuelva su média.'''
    media1 = sum(lista_int) / len(lista_int)
    return media1

cadena = input('Ingrese una lista de números separados por espacios: ')
lista_str = cadena.split(' ')
lista_int = [int(elemento) for elemento in lista_str]

print(help(media))
print(f'La media de la lista es: {media(lista_int)}')