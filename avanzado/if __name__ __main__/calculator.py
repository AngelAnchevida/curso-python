def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    return a / b


if __name__ == "__main__":
    print('Operaciones')
    res_1 = add(3,4)
    print(f"Suma: {res_1}")
    print(divide(10,7))

