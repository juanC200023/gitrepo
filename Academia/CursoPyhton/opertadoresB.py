#!/usr/bin/env python3

first_number = 8 
second_number = 6


print(first_number + second_number)
print(first_number - second_number)
print(first_number * second_number)
print(first_number / second_number)
#potencia
print(first_number ** second_number)

#formatear una cadena

print("{:,}".format(first_number ** second_number).replace(",", "."))

#Operatorias con cadenas

first_str = "Hola"
second_str = " "
third_str = "Mundo"
 
print(first_str + second_str + third_str)


print(first_str*3)


print(first_str[0]*8)


print(third_str[0:3]*5)


odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]
result = list(map(sum, zip(odd_numbers, even_numbers)))

print(result)



