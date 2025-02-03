def factorial(n):
    if n == 0: #caso base N=0
        return 1
    else:
        return n * factorial(n-1) #caso recursivo n > 0
        #Se vuelve a llamar a si mismo pero un numero anterior hasta que llegue a 0


factorial_5 = print(factorial(10))


def fibonacci(n):
    if n == 0: #caso base F(0) = 0
        return 0
    elif n == 1: #caso base F(1) = 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))


def naturales(n):
    if n == 0:
        return 0
    else:
        return n + naturales(n-1)

print(naturales(6))