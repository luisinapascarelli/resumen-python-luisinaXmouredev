""" Funciones Built-in > ES UNA FUNCION CAPAZ DE HACER ALGO > OPERACIONES PRE-CARGADAS EN PYTHON
Lista:
abs()
delattr()
hash()
memoryview()
set()
all()
dict()
help()
min()
setattr()
any()
dir()
hex()
next()
slice()
ascii()
divmod()
id()
object()
sorted()
bin()
enumerate()
input()
oct()
staticmethod()
bool()
eval()
int()
open()
str()
breakpoint()
exec()
isinstance()
ord()
sum()
bytearray()
filter()
issubclass()
pow()
super()
bytes()
float()
iter()
print()
tuple()
callable()
format()
len()
property()
type()
chr()
frozenset()
list()
range()
vars()
classmethod()
getattr()
locals()
repr()
zip()
compile()
globals()
map()
reversed()
__import__()
complex()
hasattr()
max()
round()
"""

#Variables
mi_variable = "mi variable" # CON GUION BAJO PARA SEPARAR PALABRAS > snake case < NO SE PUEDE USAR GUIÓN MEDIO
print (mi_variable)

laVariable = "la variable" # con camel case, pero inicia en minúscula
print (laVariable)

EsaVariable = "esa variable" # con camel case, pero inicia en mayúscula
print (EsaVariable) 

print (mi_variable, laVariable, EsaVariable) # CONCATENACION DE VARIABLES EN UN PRINT

mi_variable_entera = 5 #variable entera
print (mi_variable_entera)

mi_variable_entera_a_str = (str(mi_variable_entera))
print (mi_variable_entera_a_str)

print (type(mi_variable_entera_a_str)) #una variable que era entera se transforma a STR/string - ya no puedo usarla como número

# El print es capaz de ir transformando las variables a algo que sea capaz de interpretar por consola

print (type(print("mi cadena de texto"))) # tipo NoneType > PRINT NO TIENE NINGUN TIPO DE DATO, ES UNA FUNCIÓN DEL SISTEMA.

# Algunas funciones del sistema
nombre = ("Luisina")
apellido = ("Pascarelli")
print (len(nombre)) #cuenta la cantidad de letras que tiene el dato

# Variables en una sola linea
name, surname, alias, age = "nicolas", "goñi", "nisho", 29
print (age,"es su edad -", surname,"es su apellido -", alias, "es su sobrenombre -", name, "es su nombre -") # pedi imprimir en otro orden
#CUIDADO CON ABUSAR DE ESTA SINTAXIS, PUEDE TRAER CONFUSION Y ERRORES

# Variable input
name = input("Cuál es tu nombre?")
age = input("Cuál es tu edad?")
print (name, age) # Una variable puede cambiar, antes le asigne que name era nicolas. Ahora le asigne el input que me pregunta: cuál es tu nombre? > OSEA LA VARIABLE - PUEDECAMBIAR

# Fuerzo el tipo
a = 35
b = "hola"
print (a, b)

a = "hola"
b = 35
print (a, b)

#################

direccion: str = "rivadavia esq italia"
print (type (direccion))

direccion = True
print (type(direccion))