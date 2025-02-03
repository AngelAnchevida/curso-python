class Calculator:
    def add_numbers(self, first_number, second_number):
        result = first_number + second_number
        return result


#Creamos una instancia de Calculator
calc = Calculator()

print(calc.add_numbers(5, 3))