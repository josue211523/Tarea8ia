import time

# Representación del tablero de juego
board = ['-'] * 9

# Jugadores
player = 'X'
computer = 'O'

# Definir los movimientos ganadores
winning_moves = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
    [0, 4, 8], [2, 4, 6]              # Diagonales
]

# Función para imprimir el tablero
def print_board(board):
    print('---------')
    for i in range(0, 9, 3):
        print('|', board[i], board[i + 1], board[i + 2], '|')
    print('---------')

# Función para verificar si hay un ganador
def check_winner(board):
    for move in winning_moves:
        if board[move[0]] == board[move[1]] == board[move[2]] != '-':
            return board[move[0]]
    return None

# Función para verificar si el tablero está lleno
def is_board_full(board):
    return '-' not in board

# Función Minimax con poda alfa-beta
def minimax(board, depth, is_maximizing_player, alpha, beta):
    winner = check_winner(board)

    if winner is not None:
        return 1 if winner == computer else -1 if winner == player else 0

    if is_board_full(board):
        return 0

    if is_maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = computer
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = '-'
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = player
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = '-'
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Función para que la computadora realice su movimiento
def make_computer_move(board):
    start_time = time.time()
    best_eval = float('-inf')
    best_move = -1
    for i in range(9):
        if board[i] == '-':
            board[i] = computer
            eval = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = '-'
            if eval > best_eval:
                best_eval = eval
                best_move = i
    board[best_move] = computer
    end_time = time.time()
    print(f"La computadora realizó su movimiento en {end_time - start_time} segundos.")
    print_board(board)

# Función para que el jugador realice su movimiento
def make_player_move(board):
    while True:
        move = input("Ingresa tu movimiento (0-8): ")
        if move.isdigit() and int(move) in range(9) and board[int(move)] == '-':
            board[int(move)] = player
            break
        else:
            print("Movimiento inválido. Intenta nuevamente.")
    print_board(board)

# Función principal del juego
def play_game():
    print("¡Bienvenido al juego Tic-Tac-Toe!")
    print_board(board)

    while True:
        make_player_move(board)
        if check_winner(board) == player:
            print("¡Ganaste!")
            break
        elif is_board_full(board):
            print("Empate.")
            break

        make_computer_move(board)
        if check_winner(board) == computer:
            print("¡Perdiste!")
            break
        elif is_board_full(board):
            print("Empate.")
            break

# Iniciar el juego
play_game()
