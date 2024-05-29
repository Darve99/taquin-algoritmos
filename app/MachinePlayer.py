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

# Clase auxiliar para priorizar los tableros en la cola de prioridad
class PrioritizedBoard:
    def __init__(self, priority, board, path):
        self.priority = priority
        self.board = board
        self.path = path

    def __lt__(self, other):
        return self.priority < other.priority

def greedy_best_first_solve(board):
    moves = ['left', 'right', 'down', 'up']
    visited = set()
    queue = []

    initial_distance = manhattan_distance(board)
    heapq.heappush(queue, PrioritizedBoard(initial_distance, board, []))

    start_time = time.time()  # Captura el tiempo de inicio

    while queue:
        current = heapq.heappop(queue)
        current_board = current.board
        current_path = current.path

        if current_board.is_solved():
            end_time = time.time()  # Captura el tiempo de finalización
            elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
            return current_path, elapsed_time

        visited.add(tuple(current_board.m_Board))

        for move in moves:
            new_board = Taquin(*current_board.m_Size)
            new_board.m_Board = current_board.m_Board[:]
            if new_board.move(move) and tuple(new_board.m_Board) not in visited:
                new_path = current_path + [move]
                heapq.heappush(queue, PrioritizedBoard(manhattan_distance(new_board), new_board, new_path))

    return [], 0

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

    solution, elapsed_time = greedy_best_first_solve(b)
    for move in solution:
        b.move(move)
        print('***********************')
        print(b)
    print("Puzzle solved!")
    print("Tiempo de ejecución:", elapsed_time, "segundos")
