# Function to check if the queen can be placed at the given position
import random

N = 8
solution = []
STEP_COUNTER = 1

# As per the algorithm taught in the class, solution by PG

def is_safe(board, cell):
    # Check if column is already occupied
    if cell in board: 
        return False
    # Check if diagonal is already occupied
    for row, col in enumerate(board):
        if abs(row - len(board)) == abs(col - cell): 
            return False
    return True

# main function to find all possible states using backtracking
def n_queen(board):
    global STEP_COUNTER
    if len(board) == N:
        STEP_COUNTER += 1
        solution.append([STEP_COUNTER, board.copy()])
        return
    found_safe = False
    for cell in range(N):
        if is_safe(board, cell):
            found_safe = True
            n_queen(board + [cell])
    if not found_safe:
        STEP_COUNTER += 1

# Main function of PG to call the n_queen function
n_queen([])
print()
print("Total Possible Cases: ", STEP_COUNTER)
print("Total Solutions: ", len(solution))
print("\n\nSolutions: ")
for s in solution:
    print(s[0], ":", s[1])


input("Press Enter to exit...")