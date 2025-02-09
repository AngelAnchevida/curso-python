import multiprocessing

#Funcion que calcule el cuadrado de un numero
def calculate_square(n):
    return n*n

if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    #Crear un pool
    with multiprocessing.Pool() as pool:
        #Pool nos ayuda a que cada uno de los hilos pueda ejecutar la tarea mediante el map
        results = pool.map(calculate_square, numbers)

    print(f"Resultados: {results}")