from random import randint

board = []

# Create a 5x5 board filled with "O"
for x in range(0, 5):
  board.append(["O"] * 5)

# Function to print the board
def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

# Function to generate a random row index
def random_row(board):
  return randint(0, len(board) - 1)

# Function to generate a random column index
def random_col(board):
  return randint(0, len(board[0]) - 1)

# Generate random positions for the ship
ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

# Main game loop
for turn in range(4):
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  # Check if the guess matches the ship's position
  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break
  else:
    # Check if the guess is within the board boundaries
    if guess_row not in range(5) or guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    # Check if the position has already been guessed
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      # Mark the missed guess on the board
      board[guess_row][guess_col] = "X"
    # Check if it's the last turn
    if turn == 3:
      print("Game Over")
    # Print the updated board
    print_board(board)
