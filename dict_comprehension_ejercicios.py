# Ejercicio 1 --> Dict comprehension
# A partir del siguiente listado de tuplas.
# tuples = [('a', 1), ('b', 2), ('c', 3)]
# Crea un diccionario utilizando una dictionary comprehension.

tuples = [('a', 1), ('b', 2), ('c', 3)]

nuevo_dict = dict([item for item in tuples])
print(nuevo_dict)




#Ejercicio 2 
# Crea un diccionario con las letras de una palabra y su frecuencia utilizando una dictionary comprehension.
# Ejemplo.

# >>> name  = 'example'
# >>> dict
# {
#     'e': 2,
#     'x'; 1,
#     'a'; 1,
#     'm'; 1,
#     'p'; 1,
#     'l'; 1,
# }