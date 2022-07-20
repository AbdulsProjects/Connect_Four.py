import numpy as np

#Function used to display the board
def display():
    #Creates the empty string used to represent the board
    output = '\n'
    #Iterates through each row
    for row in board:
        #Iterates through each element in the row    
        for element in row:
            #Adds the element to the output
            output += element + '  '
        output += '\n'
    
    #Numbers columns
    output += '-------------------\n1  2  3  4  5  6  7'
    return output


#Function used to add a piece to the board, and returns the row that the piece was added in
def move(column, symbol):
    global board
    #Iterates through each row
    for i in reversed(range(len(board))):
        #Checks if the element is empty
        if board[i][column] == '-':
            #Replaces the empty element with the desired symbol
            board[i][column] = symbol
            return True, i
    
    return False, i, "\nColumn full, no move made"


#Function used to check if win condition has been met
def win_check(row, column):
    current_symbol = board[row][column]
    counter = 0
    #Checks if the win condition has been met on the x-axis
    #Iterates through the selected row
    for i in range(len(board[row]) - 1):
        #Checks if there is multiple of the same symbol next to each other 
        if board[row][i] != '-':
            #Next element is the same as current
            if board[row][i] == board[row][i + 1]:
                counter += 1
            #Next element isn't the same as current
            else: 
                counter = 0
        #Checks if win condition has been met
        if counter >= 3:
            return True, f"\nThe {current_symbol}'s have won!"

    
    #Resetting the counter
    counter = 0
    
    #Checks if the win condition has been met on the y-axis
    #Iterates through the length of the column
    for i in range(len(board[:]) - 1):
        #Checks if there is multiple of the same symbol next to each other
        if board[i][column] != '-':
            #Next element is same as current
            if board[i][column] == board[i + 1][column]:
                counter += 1
            #Next element isn't the same as current
            else:
                counter = 0
        #Checks if win condition has been met
        if counter >= 3:
            return True, f"\nThe {current_symbol}'s have won!"
    
    
    #Resetting the counter
    counter = 0
    
    #Checks if the win condition has been met diagonally
    #Identifying how much space there is in each cardinal direction from the selected element
    space_up = row
    space_down = 5 - row
    space_left = column
    space_right = 6 - column
    
    
    #Identifying how much space there is in each diagonal direction from the selected element
    if space_left < space_up:
        up_left = space_left
    else:
        up_left = space_up
    
    if space_down < space_right:
        down_right = space_down
    else:
        down_right = space_right
        
    if space_left < space_down:
        down_left = space_left
    else:
        down_left = space_down
        
    if space_right < space_up:
        up_right = space_right
    else:
        up_right = space_up

        
    
    #Checks down right / up left
    #Checks up left
    for i in range(1, up_left + 1):
        #Match
        if board[row - i][column - i] == board[row][column] and board[row][column] != '-':
            counter += 1
        #Missmatch
        else:
            break
    
    #Checks down right
    for i in range(1, down_right + 1):
        #Match
        if board[row + i][column + i] == board[row][column] and board[row][column] != '-':
            counter += 1
        #Missmatch
        else:
            break
        
    #Checks if the win condition was met
    if counter >= 3:
        return True, f"\nThe {current_symbol}'s have won!"
    
    
    #Resetting the counter
    counter = 0

    #Checks down left / up right
    #Checks down left
    for i in range(1, down_left + 1):
        #Match
        if board[row + i][column - i] == board[row][column] and board[row][column] != '-':
            counter += 1
        #Missmatch
        else:
            break
    
    #Checks up right 
    for i in range(1, up_right + 1):
        #Match
        if board[row - i][column + i] == board[row][column] and board[row][column] != '-':
            counter += 1
        #Missmatch
        else:
            break
    
    #Checks if the win condition was met
    if counter >= 3:
        return True, f"The {current_symbol}'s have won!"
    
    #No win conditions met
    return False, "No win condition met"


#Function used to play a game
def play():
    #Creating board
    global board
    board = np.full((6,7), '-') 
    
    #Defining player 1's symbol
    while True:
        p1_symb = input("Please input a single letter / number to represent player 1:\n")
        #Symbol isn't alphanumeric
        if p1_symb.isalnum() == False:
            print("\nInvalid character")
            continue
        #Symbol is too long
        if len(p1_symb) > 1:
            print("\nPlease only use a single character")
            continue
        break 
    
    
    #Defining player 2's symbol
    while True:
        p2_symb = input("Please input a single letter / number to represent player 2:\n")
        #Symbol isn't alphanumeric
        if p2_symb.isalnum() == False:
            print("\nInvalid character")
            continue
        #Symbol is too long
        if len(p2_symb) > 1:
            print("\nPlease only use a single character")
            continue
        #Symbol is the same as player 1
        if p2_symb == p1_symb:
            print("\nChosen symbol is used by player 1, please chose a distinct symbol")
            continue
        break
    
        
    #Taking turns until a player wins
    #Displays the board
    print("")
    print(display())
    
    #Repeats turns until a player wins
    win = False
    while win == False:
        
        #Player 1 move
        while True:
            try:
                p1_move = int(input(f"{p1_symb}'s turn, pick a column (1 - 7)\n"))
                #Move isn't a valid column
                if p1_move > 7 or p1_move < 1:
                    print("\nInvalid column")
                    continue
            #Move isn't an int
            except ValueError:
                print("\nInvalid column")
                continue
            
            #Move is a valid column
            current_move = move(p1_move - 1, p1_symb)
            #Column isn't full
            if current_move[0]:
                #Extracts the co-ordinates of the added symbol
                row = current_move[1]
                print(display())
                #Checks if player has won
                p1_win = win_check(row, p1_move - 1)
                #Player has won, terminates game
                if p1_win[0]:
                    print(p1_win[1])
                    win = True
                break
            #column is full, chose another column
            else:
                print(current_move[2])
                continue
       
        if win == False:
            #Player 2 move
            while True:
                try:
                    p2_move = int(input(f"{p2_symb}'s turn, pick a column (1 - 7)\n"))
                    #Move isn't a valid column
                    if p2_move > 7 or p2_move < 1:
                        print("\nInvalid column")
                        continue
                #Move isn't an int
                except ValueError:
                    print("\nInvalid column")
                    continue
                
                #Move is a valid column
                current_move = move(p2_move - 1, p2_symb)
                #Column isn't full
                if current_move[0]:
                    #Extracts the co-ordinates of the added symbol
                    row = current_move[1]
                    print(display())
                    #Checks if player has won
                    p2_win = win_check(row, p2_move - 1)
                    #Player has won, terminates game
                    if p2_win[0]:
                        print(p2_win[1])
                        win = True
                    break
                #column is full, chose another column
                else:
                    print(current_move[2])
                    continue

                    
#Runs the game if the program is ran
play()
