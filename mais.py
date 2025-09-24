def cargar_mapa(Movimiento_personaje):
    global movimientos
    os.system("clear")

    if Movimiento_personaje == "w":
        coordenada_personaje[0] = (coordenada_personaje[0] - 1) % HEIGHT_MAPA
        personaje = "↑"
    elif Movimiento_personaje == "s":
        coordenada_personaje[0] = (coordenada_personaje[0] + 1) % HEIGHT_MAPA
        personaje = "↓"
    elif Movimiento_personaje == "a":
        coordenada_personaje[1] = (coordenada_personaje[1] - 1) % WIDTH_MAPA
        personaje = "←"
    elif Movimiento_personaje == "d":
        coordenada_personaje[1] = (coordenada_personaje[1] + 1) % WIDTH_MAPA
        personaje = "→"

    # Movimientos
    movimientos -= 1

    # Cargar panel de control
    cargarPanel(coordenada_personaje, personaje, movimientos, len(lista_objetos))

    # Cargar mapa
    print("┌" + ("─" * (WIDTH_MAPA * 3 - 1)) + "┐")
    for fila in range(HEIGHT_MAPA):
        print("│", end="")
        for columna in range(WIDTH_MAPA):
            print(" . ", end="")  # aquí puedes imprimir personaje, objetos, bonus, etc.
        print("│")
    print("└" + ("─" * (WIDTH_MAPA * 3 - 1)) + "┘")
