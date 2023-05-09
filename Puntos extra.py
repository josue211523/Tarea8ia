import math
import time

# Función para mostrar el tablero actual
def mostrar_tablero(tablero):
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end=" ")
        print()

# Función para verificar si hay un ganador
def hay_ganador(tablero, jugador):
    # Verificar filas
    for i in range(3):
        if all(cell == jugador for cell in tablero[i]):
            return True

    # Verificar columnas
    for i in range(3):
        if all(tablero[j][i] == jugador for j in range(3)):
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True

    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

# Función para evaluar el estado actual del tablero
def evaluar(tablero):
    if hay_ganador(tablero, 'X'):
        return 1
    elif hay_ganador(tablero, 'O'):
        return -1
    else:
        return 0

# Función para generar los movimientos posibles
def movimientos_posibles(tablero):
    movimientos = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == '-':
                movimientos.append((i, j))
    return movimientos

# Función Minimax con poda alfa-beta
def minimax(tablero, profundidad, jugador, alpha, beta):
    if profundidad == 0 or hay_ganador(tablero, 'X') or hay_ganador(tablero, 'O'):
        return evaluar(tablero)

    if jugador == 'X':
        mejor_valor = -math.inf
        for movimiento in movimientos_posibles(tablero):
            i, j = movimiento
            tablero[i][j] = jugador
            valor = minimax(tablero, profundidad - 1, 'O', alpha, beta)
            tablero[i][j] = '-'
            mejor_valor = max(mejor_valor, valor)
            alpha = max(alpha, mejor_valor)
            if beta <= alpha:
                break
        return mejor_valor

    else:
        mejor_valor = math.inf
        for movimiento in movimientos_posibles(tablero):
            i, j = movimiento
            tablero[i][j] = jugador
            valor = minimax(tablero, profundidad - 1, 'X', alpha, beta)
            tablero[i][j] = '-'
            mejor_valor = min(mejor_valor, valor)
            beta = min(beta, mejor_valor)
            if beta <= alpha:
                break
        return mejor_valor

# Función para realizar el movimiento óptimo usando Minimax
def mover_optimo(tablero, profundidad):
    mejor_valor = -math.inf
    mejor_movimiento = None
    for movimiento in movimientos_posibles(tablero):
        i, j = movimiento
        tablero[i][j] = 'X'
        valor = minimax(tablero, profundidad - 1, 'O', -math.inf, math.inf)
        tablero[i][j] = '-'
        if valor > mejor_valor:
            mejor_valor
            mejor_valor = valor
            mejor_movimiento = movimiento

    i, j = mejor_movimiento
    tablero[i][j] = 'X'

# Función para que el jugador humano realice un movimiento
def mover_jugador(tablero):
    movimientos = movimientos_posibles(tablero)
    print("Movimientos disponibles:")
    for i, movimiento in enumerate(movimientos):
        print(f"{i + 1}. {movimiento}")
    indice = int(input("Selecciona el número del movimiento: ")) - 1
    i, j = movimientos[indice]
    tablero[i][j] = 'O'

# Función para jugar una partida completa
def jugar(profundidad):
    tablero = [['-' for _ in range(3)] for _ in range(3)]
    turno = 'O'
    while not hay_ganador(tablero, 'X') and not hay_ganador(tablero, 'O') and len(movimientos_posibles(tablero)) > 0:
        if turno == 'X':
            start_time = time.time()
            mover_optimo(tablero, profundidad)
            elapsed_time = time.time() - start_time
            print(f"La computadora tardó {elapsed_time} segundos en hacer su movimiento:")
            mostrar_tablero(tablero)
            turno = 'O'
        else:
            mover_jugador(tablero)
            mostrar_tablero(tablero)
            turno = 'X'

    if hay_ganador(tablero, 'X'):
        print("¡La computadora ha ganado!")
    elif hay_ganador(tablero, 'O'):
        print("¡Has ganado!")
    else:
        print("¡Es un empate!")

# Obtener la profundidad de búsqueda deseada
profundidad_deseada = int(input("Ingrese la profundidad de búsqueda deseada: "))

# Iniciar el juego con la profundidad especificada
jugar(profundidad_deseada)
