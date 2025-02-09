import threading

#Variable compartida
saldo = 0
lock = threading.Lock() #Crear un lock

def depositar(dinero):
    global saldo
    for _ in range(10000):
        with lock: #Bloquear el acceso para evitar condiciones de carrera
            saldo += dinero

hilos = []
for _ in range(2):
    hilo = threading.Thread(target=depositar, args=(1,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"Saldo final: {saldo}") #Esperamos ver 200000

# Explicación:
# El uso de lock asegura que solo un hilo modifique la variable saldo 
# en un momento dado, evitando que el resultado final sea incorrecto.
