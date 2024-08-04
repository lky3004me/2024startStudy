def is_bingo(board):
    bingo_count = 0

    # Check rows
    for row in board:
        if all(x == 0 for x in row):
            bingo_count += 1

    # Check columns
    for col in range(5):
        if all(board[row][col] == 0 for row in range(5)):
            bingo_count += 1

    # Check diagonals
    if all(board[i][i] == 0 for i in range(5)):
        bingo_count += 1
    if all(board[i][4-i] == 0 for i in range(5)):
        bingo_count += 1

    return bingo_count >= 3

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    board = []
    idx = 0

    # Read board
    for i in range(5):
        board.append(list(map(int, data[idx:idx+5])))
        idx += 5

    # Read called numbers
    called_numbers = list(map(int, data[idx:]))

    # Create a dictionary to quickly find the position of each number
    positions = {}
    for i in range(5):
        for j in range(5):
            positions[board[i][j]] = (i, j)

    # Mark the board as numbers are called and check for bingo
    for call_count, number in enumerate(called_numbers, 1):
        if number in positions:
            x, y = positions[number]
            board[x][y] = 0
            if is_bingo(board):
                print(call_count)
                return

if __name__ == "__main__":
    main()
