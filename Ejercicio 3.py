'''Escribir una función que calcule el área de un círculo y
otra que calcule el volumen de un cilindro usando la primera función.'''

def area_circulo(radio):
    return 3.14 * radio ** 2

def volumen_cilindro(altura):
    volumen = area_circulo(radio) * altura
    return volumen

radio = float(input('Ingrese el radio del círculo en cm: '))

print('El área del círculo es', area_circulo(radio), 'cm^2')

altura = float(input('Ingrese la altura del cilindro en cm: '))

print('El volumen del cilindro es', volumen_cilindro(altura), 'cm^3')