from collections import deque

def get_min_dice_throws(board, n):
    visited = [False] * n
    queue = deque([(0, 0)])
    visited[0] = True

    while queue:
        cell, dist = queue.popleft()
        if cell == n - 1:
            return dist

        for i in range(1, 7):
            next_cell = cell + i
            if next_cell < n:
                if not visited[next_cell]:
                    visited[next_cell] = True
                    actual_cell = board[next_cell] if board[next_cell] != -1 else next_cell
                    queue.append((actual_cell, dist + 1))
    return -1

if __name__ == "__main__":
    N = 30
    moves = [-1] * N
    
    # Ladders
    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28
    
    # Snakes
    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6

    print(get_min_dice_throws(moves, N))
