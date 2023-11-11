def bienvenida(nombre):
    ''' 
    Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
    '''   
    print('¡Hola', nombre + '!')
    return

nombre = input('Ingrese su nombre: ')
bienvenida(nombre)
help(bienvenida)

