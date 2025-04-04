#!/usr/bin/env python3

class Calculadora:

    @staticmethod
    def suma(num1, num2):
        return num1 + num2

    @staticmethod
    def resta(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplicacion(num1, num2):
        return num1 * num2

    @staticmethod 
    def division(num1, num2):
        return num1 / num2 if num2 != 0 else "\n[!] Error no se puede dividir por 0"


print(Calculadora.suma(2, 8))
print(Calculadora.resta(2, 9))
print(Calculadora.multiplicacion(4, 7))
print(Calculadora.division(3, 0))
