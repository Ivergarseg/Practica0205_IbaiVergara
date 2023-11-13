'''Escribir una función que reciba un fragmento de texto en una cadena de caracteres 
y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
Escribir otra función que reciba el diccionario generado con la función anterior
y devuelva una tupla con la palabra más repetida y su frecuencia.'''


texto = input('Introduce el texto: ')


def frecuencia_palabras(texto):
    '''Función que recibe un fragmento de texto en una cadena de caracteres y devuelva un diccionario 
    con cada palabra que contiene y su frecuencia.'''
    diccionario = {}
    palabras = texto.split()
    for palabra in palabras: # Iterar sobre cada palabra
        letras = ''.join(i for i in palabra if i.isalpha()) #Extraer solo las letras
        diccionario[letras] = diccionario.get(letras, 0) + 1
    return diccionario

diccionario = frecuencia_palabras(texto)

def palabra_mas_repetida(diccionario):
    '''Función que recibe el diccionario generado con la función anterior y devuelva una tupla 
    con la palabra más repetida y su frecuencia.'''
    palabra_mas_repetida = None
    frecuencia_palabra_mas_repetida = 0
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_palabra_mas_repetida:
            frecuencia_palabra_mas_repetida = frecuencia
            palabra_mas_repetida = palabra
    return palabra_mas_repetida, frecuencia_palabra_mas_repetida


print('El diccionario creado con todas las palabras del texto es:',frecuencia_palabras(texto))    
print('\n')
palabra_frecuencia = palabra_mas_repetida(diccionario)
print('La palabra más repetida en el texto es:',palabra_frecuencia[0],', y su frecuencia es de',palabra_frecuencia[1],'veces.')
