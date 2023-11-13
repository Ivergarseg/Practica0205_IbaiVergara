'''Escribir una función que convierta un número decimal en binario 
y otra que convierta un número binario en decimal.'''

def binario_to_decimal(numbinario):
    '''Dado un número binario, devuelva su valor decimal.'''
    lista = list(numbinario)
    lista_a_sumar = []
    for valor in range(len(lista)):
        if lista[valor] != '0' and lista[valor]!= '1':
            return 'El número no es un número binario.'
        elif lista[valor] == '1':
            elem_a_sumar = 2**(len(lista) - valor - 1)
            lista_a_sumar.append(elem_a_sumar)
        
    valor_decimal = sum(lista_a_sumar)
    return valor_decimal

numbinario = input('Ingrese un número binario sin espacios: ')

print(binario_to_decimal(numbinario))

def decimal_to_binario(numdecimal):
    '''Dado un número decimal, devuelva su valor binario.'''
    exp = 0
    resto = 0
    lista_solucion = []
    while 2**exp <= numdecimal: #busco el exponente con el 
        exp += 1                #que voy a tener que empezar a trabajar
     
    for i in reversed(range(exp)): #trabajo con los exp en orden descendente
        if numdecimal - 2**(i) >= 0:
            resto = numdecimal - 2**(i)
            lista_solucion.append('1')
            numdecimal = resto
        else: 
            lista_solucion.append('0')

    solucion = ''.join(lista_solucion)
    
    return solucion


numdecimal = int(input('Ingrese un número decimal: '))
print (decimal_to_binario(numdecimal))