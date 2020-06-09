from random import choice
player_name=""
player_marker=""
computer_marker=""

def display_board(board):
    print()
    for i in range(9):
        if board[i]==0:
            print(" ",end="")
        else:
            print(board[i],end="")
        if i==2 or i==5:
            print("\n--------\n")
        elif i==8:
            pass
        else:
            print(" |",end="")

def choose_spot(turn,board_places,board):
    if turn == player_marker:
        spot=int(input("\nChoose Your Spot In Range 1 to 9 :")) - 1
        while spot not in board_places:
            spot=int(input("Invalid Choice\nChoose Vacant Spot In Range 1 to 9 :")) - 1
        board[spot]=turn
        board_places.remove(spot)
        turn = computer_marker
    else:
        spot=choice(board_places)
        board[spot]=turn
        board_places.remove(spot)
        turn = player_marker
        print("\nComputer Chose Spot",spot+1)
    
    display_board(board)
    return turn
        
def check_win(turn,board):
    if ((turn==board[0] and turn==board[1] and turn==board[2]) or (turn==board[3] and turn==board[4] and turn==board[5]) or
        (turn==board[6] and turn==board[7] and turn==board[8]) or (turn==board[0] and turn==board[3] and turn==board[6]) or
        (turn==board[1] and turn==board[4] and turn==board[7]) or (turn==board[2] and turn==board[5] and turn==board[8]) or
        (turn==board[0] and turn==board[4] and turn==board[8]) or (turn==board[2] and turn==board[4] and turn==board[6])):
        return True
    else:
        return False

        
def check_tie(board_places):
    return False if board_places else True

def play_game():
    ch=input("\nWould You Like To Play First: [y] or [n] :")
    if ch=="y":
        turn = player_marker
    else:
        turn = computer_marker
    board_places=[0,1,2,3,4,5,6,7,8]
    board=[0]*9
    
    while True:
        temp_turn = turn
        turn=choose_spot(turn,board_places,board)
        if check_win(temp_turn,board):
            if temp_turn == player_marker:
                print("\n",player_name,"WON")
            else:
                print("\nComputer WON")
            break
        if check_tie(board_places):
            print("\nGame TIE")
            break
            



if __name__=="__main__":
    print("      Welcome To The Game\n         Tic Tac Toe")
    player_name=input("\nEnter Your Name: ")
    player_marker=input("Choose Your Marker: [X] or [O] :")
    while player_marker not in "XO":
        player_marker=input("Invalid Choice\nChoose Your Marker: [X] or [O] :")
    if player_marker=="X":
        computer_marker="O"
    else:
        computer_marker="X"
    print("Computer Marker:",computer_marker)

    replay="y"
    while replay != "n":
        play_game()
        replay=input("Do You Want To Play Again [y] or [n] :")

    print("\n\nHappy Gaming")
    
    
    
    
    
