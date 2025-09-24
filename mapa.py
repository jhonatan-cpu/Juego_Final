def cargar_mapa():
    os.system("cls" if os.name == "nt" else "clear")

    # Panel superior (puedes ajustar según necesites)
    print("┌───────────────┬────────────┬───────┐")
    print("│ Posición      │ Dirección  │ Movs  │")
    print(f"│ [{coordenada_personaje[0]:02d}, {coordenada_personaje[1]:02d}]   │     {direccion}      │ {movimientos:03d}  │")
    print("└───────────────┴────────────┴───────┘")

    # Borde superior del mapa
    print("┌" + "───" * WIDHT_MAPA + "┐")

    # Contenido del mapa
    for fila in range(HEIGHT_MAPA):
        print("│", end="")  # Borde izquierdo

        for columna in range(WIDHT_MAPA):
            if coordenada_personaje[0] == fila and coordenada_personaje[1] == columna:
                print(f"[{personaje}]", end="")
            else:
                dibujado = False
                for obj in lista_objetos:
                    if obj[0] == fila and obj[1] == columna:
                        print(f"[{obj[2]}]", end="")
                        dibujado = True
                        break
                if not dibujado:
                    print("[ ]", end="")

        print("│")  # Borde derecho

    # Borde inferior del mapa
    print("└" + "───" * WIDHT_MAPA + "┘")

    print("\nUsa W A S D para mover, Q para salir.")

