height = 6
width = 7

def init():
  board = [] #an array
  for i in range(height):
    board.append(["0"] * width)
  return board

def print_board(board):
 print("1 2 3 4 5 6 7")
 print("_" * 13)
 for row in board:
   print("|".join(row))

board = init()
print_board(board)

def get_move(board, player):
  column = int(input("Player {} enter a column".format(player)))
  if (column < 1 or column > width):
    print("sit down! Not on my watch. Enter a number between 1 and 7:")
    column = get_move(board, player)

  column -= 1
  column_full = True
  for i in range(height):
    if board in[i][column] == "0":
       column_full = False
       if column full:
      print("This column is full, try again please :)")
      column = get_move(board, player)
      return column