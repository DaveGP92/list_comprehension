# A partir de 2 listas de números enteros (a y b) Ejemplo:

# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]

#crea una lista con los elementos que están en ambas listas a y b.

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

c = [num for num in a + b]

print(c)