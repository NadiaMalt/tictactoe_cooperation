# board
# display board
# play game
# handle turn
# check win
  # check rows
# check tie
  # if the board is full and there is no winner
# flip the players

# --Global variables--

# board
print("lets start this game")
board = "____________________"

# If game is still going
game_still_going = True

# who won?
winner = None

# whenever i want to see the board i have to call this function
def display_board():
  print(board)

def play_game():
  # prints the initial board
  display_board()

  while game_still_going: 

    players_move()

    evaluate_game()

    flip_player()

# the game has ended
  if winner == "X" or winner == "O":
    print(winner) + "has won and is great"
  elif winner == None:
    print("it is a tie")

def players_move():
  position_player = int(input("Chose a position between 1-20:"))

  board_new=board[:position_player-1]+board[position_player-1].replace('_','X')+board[position_player:]
 
  print(board_new)

def evaluate_game():
  check_if_win()
  check_if_tie()

def check_if_win():
  #check rows
    return

def check_if_tie():
  return

def flip_player():
  return
  
play_game()