piedra = "piedra"
papel = "papel"
tijeras = "tijeras"

movimientos = ["piedra", "papel", "tijeras"]

#Validar

jugador1 = input("Jugador 1 \npiedra, papel o tijeras: ").lower()
jugador2 = input("Jugador 2 \npiedra, papel o tijeras: ").lower()

if jugador1 not in movimientos:
    print("Jugador 1 ingresa un movimiento válido")
elif jugador2 not in movimientos:
    print("Jugador 2 ingresa un movimiento válido")
else:

    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == piedra and jugador2 == tijeras) or (jugador1 == papel and jugador2 == piedra) or (jugador1 == tijeras and jugador2 == papel):
        print("jugador 1 gana")
    else:
        print("Jugador 2 gana")

