import sys
import time
import heapq

sys.path.append('../lib/python3')
from Taquin import Taquin


# Función para calcular la distancia de Manhattan
def manhattan_distance(board):
    size = board.m_Size
    distance = 0
    for i in range(size[0] * size[1]):
        value = board.m_Board[i]
        if value != size[0] * size[1] - 1:  # Ignorar el espacio vacío
            target_x = value % size[0]
            target_y = value // size[0]
            current_x = i % size[0]
            current_y = i // size[0]
            distance += abs(target_x - current_x) + abs(target_y - current_y)
    return distance


def greedy_best_first_solve(board):
    moves = ['left', 'right', 'down', 'up']
    visited = set()
    queue = []

    # Inicializa la cola con el tablero inicial
    heapq.heappush(queue, (manhattan_distance(board), board, []))

    while queue:
        _, current_board, path = heapq.heappop(queue)

        # Si el tablero está resuelto, devuelve el camino y termina
        if current_board.is_solved():
            return path

        visited.add(tuple(current_board.m_Board))

        # Prueba todos los movimientos posibles
        for move in moves:
            new_board = current_board.copy()
            if new_board.move(move) and tuple(new_board.m_Board) not in visited:
                new_path = path + [move]
                heapq.heappush(queue, (manhattan_distance(new_board), new_board, new_path))

    # Si no se encuentra ninguna solución, devuelve una lista vacía
    return []


if __name__ == "__main__":
    w, h = [int(v) for v in sys.argv[1:3]]
    b = Taquin(w, h)

    print(b)
    print(b.is_solved())
    b.shuffle()
    print('***********************')
    print(b)
    print(b.is_solved())
    print('***********************')

    start_time = time.time()
    solution = greedy_best_first_solve(b)

    for move in solution:
        b.move(move)
        print('***********************')
        print(b)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Puzzle solved!")
    print("Tiempo de ejecución:", elapsed_time, "segundos")
