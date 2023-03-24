# Esto es un comentario
print ("Hola Python")
print ('Hola Python') #cadenas de texto

"""
Este es un comentario 
en varias líneas.

Datos y tipos de datos:

Texto:
Las comillas tanto para las strings como para los comentarios en varias lineas pueden ser dobles o simples.
Strings > texto ej "python" "i love teaching" (una coleccion de uno o mas caracteres bajo una simple o doble comilla)

Numeros:
Enteros > (positivos, negativos y 0) ej: -1, 0, 1, 2, 3, 4...
Flotantes > (Numeros con decimales) ej: -3.0,  -2.5, 0.0, 1,5, 2.0, 2.5, 3.0
Complejos > 1+j, 2+4j

Booleanos:
Es un valor Verdadero(True) o Falso(False) > T o F deben estar siempre en Mayúscula """
True # está la luz prendida? si está prendia, entonces el valor es T
False # está la luz apagada? si está apagada, entonces el valor es F

# Listas > La lista de Python es una colección ordenada que permite almacenar diferentes tipos de elementos de datos.
[0, 1, 2, 3, 4, 5] # todos son el mismo tipo de datos > una lista de numeros
["Banana", "Naranja", "Mango"] # todos son el mismo tipo de datos > una lista de frutas (strings)
["Finlandia", "Estonia", "Noruega"] # todos son el mismo tipo de datos > una lista de paises (strings)
["Banana", "10", False, 9.81] # diferentes tipos de datos en la lista > string, entero, booleano, flotante

"""
Diccionario:
Python nos permiten almacenar una serie de mapeos entre dos conjuntos de elementos, llamados keys and values (Claves y Valores).
"""
first_name = "Luisina"
last_name = "Pascarelli"
age = "29"
country = "Argentina"

#Type: Consultar el tipo de dato - type se suele usar para asegurar que tipo de dato es uno
print (type("Soy un dato STR")) #dato de tipo  str: string
print (type(5)) #dato de tipo int: entero # LOS DATOS NÚMERICOS SIEMPRE VAN SIN COMILLAS
print (type(0.5)) #dato de tipo float: flotante: con decimales
print (type(True)) #dato de tipo bool: booleano: T o F
print (type(3 + 2j)) #dato de tipo complex: complejo

#Operaciones
print(2 + 3)             # SUMA (+)
print(3 - 1)             # RESTA (-)
print(2 * 3)             # MULTIPLICACIÓN (*)
print(3 / 2)             # DIVISION CON DECIMALES (/)
print(3 ** 2)            # POTENCIA (**)
print(3 % 2)             # PORCENTAJE (%)
print(3 // 2)            # DIVISION ENTERA (//)
