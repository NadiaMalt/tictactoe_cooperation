# board
# display board
# play game
# handle turn
# check win
  # check rows
# check tie
  # if the board is full and there is no winner



# board
print("lets start this game")

# --Global variables--
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

  # while the game_still_going is true the play_game function calls the players_move ,pc_move and evaluate_game
  while game_still_going: 

    players_move()
    pc_move()
    evaluate_game()
    
# the game has ended
  if winner == "X" or winner == "O":
    print(winner, "has won and is great")
  elif winner == None:
    print("it is a tie")

#single turn of the player
def players_move():
    global board
    position_player = int(input("Chose a position between 1-20:"))
    # while one of the three conditions are happening i want the player to input again
    while position_player < 1 or position_player > 20 or board[position_player-1] != "_":
      # if these two conditions are happening i want the following message
      if position_player < 1 or position_player > 20:
        print("can you please give a position in the correct range? ;)")
      # the position of the player is alredy taken i want the following message
      elif board[position_player-1] != "_":
        print("position already taken")
      # i want the player to input again all the time we are in the while
      position_player = int(input("Chose a position between 1-20:"))
    else:
      board=board[:position_player-1]+board[position_player-1].replace('_','X')+board[position_player:] 
    print(board)
    
#single turn of the computer
from random import randrange

def pc_move():
    global board
    position_pc = randrange(1,20)     
    while board[position_pc-1] != "_":
        print("pc must give position again")
        position_pc = randrange(1,20)                
    if board[position_pc-1] == "_":
        board=board[:position_pc-1]+board[position_pc-1].replace('_','O')+board[position_pc:]
    print(board)

def evaluate_game():
  check_if_win()
  check_if_tie()

def check_if_win():
    # set up global variable in the function
    global winner
    global game_still_going
  #check rows
    for i in range (1,19):
      if board[i-1] == board[i] == board[i+1] == "X":
        winner = "X"
        game_still_going = False
        return winner, game_still_going
      elif board[i-1] == board[i] == board[i+1] == "O":
        winner = "O"
        game_still_going = False
        return winner, game_still_going
      else:
        winner = None
        game_still_going = True
    return winner, game_still_going
    
def check_if_tie():
  global game_still_going
  if "_" not in board:
    game_still_going = False
    return

# this is the first function i call in orde to start the game  
play_game()