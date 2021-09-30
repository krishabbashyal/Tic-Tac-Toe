
#Figure out who is who, who is X and who is O

def get_player_values():

    playerOneName = input("Player one, enter your name: ")
    playerOneLetter = "X"
    
    playerTwoName = input("Player two, enter your name: ")
    playerTwoLetter = "O"

    return playerOneLetter, playerTwoLetter, playerOneName, playerTwoName # It is possible to return multiple values from a function if they are on same line

def gameInfo():
    print(f'''\n{playerOneName} will be "{playerOneLetter}" and {playerTwoName} will be "{playerTwoLetter}"''' )




    #Printing the board

def printBoard():

    print("")
    print(boardLocations[6] +  " | " + boardLocations[7] + " | " + boardLocations[8] + "                    7 | 8 | 9" )
    print("---------                    ----------")
    print(boardLocations[3] + " | " + boardLocations[4] + " | " + boardLocations[5] + "                    4 | 5 | 6" )
    print("---------                    ----------")
    print(boardLocations[0] + " | " + boardLocations[1] + " | " + boardLocations[2] + "                    1 | 2 | 3")


    #Ask each player to put their mark on the board

def playerOnePrompt():
    playerOneInput = int(input(f'''\n{playerOneName} where would you like to place your "{playerOneLetter}": '''))
    return playerOneInput
    

def playerTwoPrompt():
    playerTwoInput = int(input(f'''\n{playerTwoName} where would you like to place your "{playerTwoLetter}": '''))
    return playerTwoInput

#Update the board

def playerOneUpdate(index):
    boardLocations[index - 1] = playerOneLetter
    return boardLocations

def playerTwoUpdate(index):
    boardLocations[index - 1] = playerTwoLetter
    return boardLocations


#Check for win condition or endgame condition

def checkWin(letter, board):

    if boardLocations[7 - 1] == letter and boardLocations[8 - 1] == letter and boardLocations[9 - 1] == letter:
        return True
        
    if boardLocations[4 - 1] == letter and boardLocations[5 - 1] == letter and boardLocations[6 - 1] == letter:
        return True
        
    if boardLocations[1 - 1] == letter and boardLocations[2 - 1] == letter and boardLocations[3 - 1] == letter:
        return True

    if boardLocations[7 - 1] == letter and boardLocations[4 - 1] == letter and boardLocations[1 - 1] == letter:
        return True

    if boardLocations[8 - 1] == letter and boardLocations[5 - 1] == letter and boardLocations[2 - 1] == letter:
        return True
    
    if boardLocations[9 - 1] == letter and boardLocations[6 - 1] == letter and boardLocations[3 - 1] == letter:
        return True
    
    if boardLocations[7 - 1] == letter and boardLocations[5 - 1] == letter and boardLocations[3 - 1] == letter:
        return True

    if boardLocations[9 - 1] == letter and boardLocations[5 - 1] == letter and boardLocations[1 - 1] == letter:
        return True

    else:
        return False
    

def checkOutOfSpaces(board):
    return " " not in board
    
    
# End the game when one condition in met       

# Main Function --------------------------------------------------------------------------------

gameOver = False
outOfSpaces = False

boardLocations = [" "," "," "
                 ," "," "," "
                 ," "," "," "]

playerOneLetter, playerTwoLetter, playerOneName, playerTwoName = get_player_values()
gameInfo()
printBoard()

while gameOver == False and outOfSpaces == False:

    
    
    playerOneInput = playerOnePrompt()
    boardLocations = playerOneUpdate(playerOneInput)
    outOfSpaces = checkOutOfSpaces(boardLocations)
    gameOver = checkWin(playerOneLetter, boardLocations)
    printBoard()

    if gameOver:
        print(f"\nThe game is over, {playerOneName} has won!")
        break

    if outOfSpaces == True:
        break
    
    playerTwoInput = playerTwoPrompt()
    boardLocations = playerTwoUpdate(playerTwoInput)
    outOfSpaces = checkOutOfSpaces(boardLocations)
    gameOver = checkWin(playerTwoLetter, boardLocations)
    printBoard()

    if gameOver:
        print(f"\nThe game is over, {playerTwoName} has won!")
        break

 
if outOfSpaces:
    print("Out of spaces, there is no winner")

