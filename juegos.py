import os
import random
import msvcrt

# Parámetros del mapa
WIDTH_MAPA = 50
HEIGHT_MAPA = 15
espacio_vacio = " "
personaje = "🠺"  
corazon = "♥"
bonus_ico = "+3"

# Estado del jugador
coordenada_personaje = [0, 0]
direccion = "inicio"
movimientos_restantes = 45  
objetos_recolectados = 0
puntos_bonus = 0

# Cantidad total de corazones y bonus
NUM_CORAZONES = 4
NUM_BONUS = 3

# Generar corazones aleatorios
total_objetos = []
while len(total_objetos) < NUM_CORAZONES:
    nuevo = [random.randint(0, HEIGHT_MAPA - 1), random.randint(0, WIDTH_MAPA - 1)]
    if nuevo != coordenada_personaje and nuevo not in total_objetos:
        total_objetos.append(nuevo)

# Generar bonus aleatorios
total_bonus = []
while len(total_bonus) < NUM_BONUS:
    nuevo = [random.randint(0, HEIGHT_MAPA - 1), random.randint(0, WIDTH_MAPA - 1)]
    if nuevo != coordenada_personaje and nuevo not in total_objetos and nuevo not in total_bonus:
        total_bonus.append(nuevo)

# Función para limpiar pantalla (compatible con Windows)
def limpiar_pantalla():
    os.system('cls')

# Panel de control
def panel_control():
    fila, columna = coordenada_personaje
    print("┌────────────┬────────────┬────────────┬────────────┬──────────┐")
    print("│ Posición   │ Dirección  │ Movs Rest. │ Corazones  │ Bonus    │")
    print(f"│ ({fila:02},{columna:02}) │ {direccion:^10} │ {movimientos_restantes:^11} │ {objetos_recolectados:^10} │ {puntos_bonus:^8} │")
    print("└────────────┴────────────┴────────────┴────────────┴──────────┘\n")

# Función para mostrar el mapa
def imprimir_mapa():
    panel_control()
    print("+" + "-" * (WIDTH_MAPA * 2) + "+")
    for fila in range(HEIGHT_MAPA):
        print("|", end="")
        columna = 0
        while columna < WIDTH_MAPA:
            pos = [fila, columna]
            if pos == coordenada_personaje:
                print(personaje + " ", end="")
                columna += 1
            elif pos in total_objetos:
                print(corazon + " ", end="")
                columna += 1
            elif pos in total_bonus:
                print(bonus_ico, end="")  
                columna += 2
            else:
                print("  ", end="")
                columna += 1
        print("|")
    print("+" + "-" * (WIDTH_MAPA * 2) + "+")
    print("\nUsa W A S D para mover, Q para salir.")

# Movimiento del personaje y detección de objetos
def cargar_mapa(tecla):
    global coordenada_personaje, direccion, movimientos_restantes, objetos_recolectados, puntos_bonus, personaje

    fila, columna = coordenada_personaje

    if tecla == "w":
        fila -= 1
        direccion = "arriba"
        personaje = "🠹"
    elif tecla == "s":
        fila += 1
        direccion = "abajo"
        personaje = "🠻"
    elif tecla == "a":
        columna -= 1
        direccion = "izquierda"
        personaje = "🠸"
    elif tecla == "d":
        columna += 1
        direccion = "derecha"
        personaje = "🠺"

    # Teletransportación por bordes
    fila %= HEIGHT_MAPA
    columna %= WIDTH_MAPA

    coordenada_personaje[:] = [fila, columna]
    movimientos_restantes -= 1  

    # Recolectar corazón
    if coordenada_personaje in total_objetos:
        total_objetos.remove(coordenada_personaje)
        objetos_recolectados += 1

    # Recolectar bonus
    if coordenada_personaje in total_bonus:
        total_bonus.remove(coordenada_personaje)
        puntos_bonus += 3

# Bucle principal
if __name__ == "__main__":
    while True:
        limpiar_pantalla()
        imprimir_mapa()

        # Fin del juego por victoria
        if objetos_recolectados == NUM_CORAZONES:
            print("🎉 ¡Felicidades! Has recogido todos los corazones. Fin del juego.")
            break

        # Fin del juego por movimientos agotados
        if movimientos_restantes <= 0:
            print("⏳ Te quedaste sin movimientos. Fin del juego.")
            break

        tecla = msvcrt.getch().decode("utf-8", errors="ignore").lower()

        if tecla == "q":
            break

        if tecla in ["w", "a", "s", "d"]:
            cargar_mapa(tecla)
