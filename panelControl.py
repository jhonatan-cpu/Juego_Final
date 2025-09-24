def cargarPanel(posicion, direccion, movimientos, corazones, bonus):
    fila, columna = posicion
    print("[ Posición ]  [ Dirección ]  [ Movs ]  [ Corazones ]  [ Bonus ]")
    print(f"  ({fila:02d}, {columna:02d})      {direccion}         {movimientos:03d}         {corazones}            {bonus}\n")
