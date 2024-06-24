#Ejercicio 3
# A partir de 2 listas de números enteros (a y b) Ejemplo:

# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]

#crea una lista con los elementos que están en ambas listas a y b.

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

c = [num for num in a + b]

print(c)

#Ejercicio 2
#Utilizando las 2 listas del ejercicio anterior, crea una lista con los elementos que están en la lista a pero no en la lista b.

nueva_lista = [num for num in a if num not in b]

print(nueva_lista)

