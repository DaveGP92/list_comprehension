# Sets comprehension
# A partir del siguiente listado de números:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Crea un conjunto con los elementos que sean múltiplos de 3.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

multiplos_3 = tuple([num for num in numbers if num % 3 == 0])

print(multiplos_3)