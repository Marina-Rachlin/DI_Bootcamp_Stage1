# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.


# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above

board = ['   ','   ','   ',
         '   ','   ','   ',
         '   ','   ','   ' 
        ]
player = 'X'


def display_board():
    print(f'{board[0]}|{board[1]}|{board[2]}\n___________\n{board[3]}|{board[4]}|{board[5]}\n___________\n{board[6]}|{board[7]}|{board[8]}')
  

def player_input(player):
    turn = int(input('Make your turn! Enter a number from 1-9 '))
    if 1<= turn <= 9:
      if board[turn - 1] == '   ':
         board[turn - 1] = player
        
# display_board()
# player_input(player)
# # check_win():

def play():
    while True:
     display_board()
     player_input(player)

# while True:
#    display_board()
#    def player_input(player):
#     turn = int(input('Make your turn! Enter a number from 1-9 '))
#     if 1<= turn <= 9:
#       if board[turn - 1] == '   ':
#          board[turn - 1] = player
   
   
play()




