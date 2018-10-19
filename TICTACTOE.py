import time
#import random
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1       
Win = 1    
Draw = -1    
Running = 0    
Stop = 1       
computer=[1,2,3,4,5,6,7,8,9]
Game = Running    
Mark = 'X'


def DrawBoard():    
    print(f" {board[1]} | {board[2]} | {board[3]} ")   
    print("___|___|___")    
    print(f" {board[4]} | {board[5]} | {board[6]} ")     
    print("___|___|___")    
    print(f" {board[7]} | {board[8]} | {board[9]} ")     
    print("   |   |   ")    


def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False        


def CheckWin():    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
    #Match Tie or Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running


Player1=input('Enter the name of player1-')
Player2=input('Enter the name of player2-')
while True:
    try:    
        print(f"{Player1} is [X] --- {Player2} is [O]\n")    
        print()    
        print()    
        print("Please Wait...")    
        time.sleep(3)    
        while(Game == Running):       
            DrawBoard()    
            if(player % 2 != 0):    
                print(f"{Player1}'s chance")    
                Mark = 'X'
            else:    
                print(f"{Player2}'s chance")    
                Mark = 'O'
            choice = int(input("Enter the position between [1-9] where you want to mark : "))
            if(CheckPosition(choice)):    
                board[choice] = Mark    
                player+=1    
                CheckWin()    

        DrawBoard()    
        if(Game==Draw):    
            print("Game Draw")    
        elif(Game==Win):    
            player-=1    
            if(player%2!=0):    
                print(f"{Player1} Won")    
            else:    
                print(f"{Player2} Won")
        break
    except Exception as e:
        print(e)
        print('you need to give the position instead')