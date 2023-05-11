board = [
    ['     ', '     ', '     '],
    ['     ', '     ', '     '],
    ['     ', '     ', '     ']
]

current_player = 'X'
count = 0
running_play = True

def display_board(board):
    LINE = "*******************"
    GRID = "*  ---|-----|---  *"
    print ("\n" + LINE)
    print("*" + board[0][0] + '|' + board[0][1] + '|' + board[0][2] + "*")
    print (GRID)
    print("*"  + board[1][0] + '|' + board[1][1]+ '|' + board[1][2] + "*")
    print (GRID)
    print("*"  + board[2][0] + '|' + board[2][1]+ '|' + board[2][2] + "*")
    print (LINE)

def switch_player():
     global current_player 
     if current_player == 'X':
        current_player = 'O'
     else:
        current_player = 'X' 

def play_won():
    global running_play
    display_board(board) 
    print(f"\nCongratulations!!! Player {current_player} won!!!")
    running_play = False


def player_input():
    print(f"\nPlayer {current_player}'s turn...")
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    #TODO:  check if the input is number (type(row)== init)

    #check if the input is in range 
    if not 1 <= row <= 3 or not 1 <= column <= 3:
        print("\nYou need to pick 1-3 ....")
        display_board(board)
        player_input()   

    #check if the spot is free   
    elif board[row-1][column-1] == '     ':
       board[row-1][column-1] = f'  {current_player}  '
       global count
       count += 1
    else:
        print("Oops player is already at that spot.")
        display_board(board)
        player_input()


def check_win():  # Now we will check if player X or O has won. We will check every move after 5 moves.
        global count 
        global running_play 
        if count >= 5:

        # check horizontal
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2] != '     ':
                      play_won() 
                      break  
                
            # check vertical
            for j in range(3):
                if board[0][j] == board[1][j] == board[2][j] != '     ':
                    play_won() 
                    break  
                
            # check diagonal
                if board[0][0] == board[1][1] == board[2][2] != '     ' or board[2][0] == board[1][1] == board[0][2] != '     ':
                    play_won() 
                    break  

            # check for  a tie 
            if count == 9:
              display_board(board)
              print("\nGame Over.\n")                
              print("It's a Tie!!") 
              running_play = False  


def play():
    print('\nWELCOME TO TIC TAC TOE!\n')
    print('TIC TAC TOE!')
    while running_play:
        display_board(board)
        player_input()
        check_win()
        switch_player()
        
play()



