import math
import random



# Task: implement a four in a row game using the minimax algorithm WITH ALPHA BETA PRUNING in python 
#
# 💡💡💡 Song Recommendation : Grass Is Always Greener, Tosh Palmer
        
# 6 row by 7 column board
def createBoard():
        board = [[0 for _ in range(7)] for _ in range(6)]
        return board

#displays the board the same way it'd look in a game 
def displayBoard(board):
    for row in board:
        print(row)
    print("\n")


#inserts a piece onto the board at the given location
def insertPiece(board, row, col, piece):
      board[row][col] = piece


#finds the next open spot in a given column and returns the index of that spot
def nextOpenSpot(board, col):
      for row in range(5, -1, -1): #traverses the column in reverse order (from bottom to top)
            #return the index of the first available spot 
            if board[row][col] == 0:
                return row
            

def isWinningMove(board, piece):
    #check horizontally 
    for row in range(6):
          for col in range(4):
                if board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and board[row][col + 3] == piece:
                      return True

    #check vertically
    for row in range(3):
          for col in range(7):
                if board[row][col] == piece and board[row + 1][col] == piece and board[row + 2][col] == piece and board[row + 3][col] == piece:
                      return True

    #check diagnal (bottom left to top right)
    for row in range(3):
          for col in range(4):
                if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and board[row + 3][col + 3] == piece:
                      return True 

    # check diagnal (bottom right to top left)    
    for row in range(3, 6):
          for col in range(4):
                if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece:
                      return True
    return False

#evaluate the points derivable from an inputted section (assumed to be an array)
def evaluateSection(section, piece):
    score = 0
    opponentPiece = 0 
    
    #adjust the opponent piece based on the input
    if piece == 2:
        opponentPiece = 1
    else: 
        opponentPiece = 2

    #if theres 4 matches, alot of 10k points, if theres 3, 1k points, so on and so forth
    if section.count(piece) == 4:
          score += 10000
    elif section.count(piece) == 3:
          score += 1000
    elif section.count(piece) == 2:
          score += 100
    
    #if the opponent is about to win, decrease the score by an amount significant enough to affect the move
    if section.count(opponentPiece) == 3 and section.count(0) == 1:
          score -= 200
    
    return score

#scans the board and returns a score associated with the current board state and a specified piece 
def scorePosition(board, piece):
    score = 0

    #having pieces in the center of the board in connect four is strategically valuable 
    #so having more pieces there adds a significant value to the score 
    #with significance meaning it affects the AI's behavior 
    #(if results seem undesireable, experiment with different multipliers)
    centerArray = [board[row][3] for row in range(6)]
    score += centerArray.count(piece) * 1000

    #observe the board and get the score that results associated with the current board and selected piece
    #horizontal patterns     
    for row in range(6):
          rowArray = board[row]
          for col in range(4):
                section = rowArray[col : col + 4] #MAY CAUSE OUT OF BOUNDS EXCEPTION
                score += evaluateSection(section, piece)

    #vertical patterns 
    for col in range(7):
          colArray = [board[row][col] for row in range(6)]
          for row in range(3):
                section = colArray[row : row + 4]
                score += evaluateSection(section, piece)

    #diagnal patterns (top left to bottom right)
    for row in range(3):
          for col in range(4):
                section = [board[row + i][col + i] for i in range(4)]
                score += evaluateSection(section, piece)

    #diagnal patterns (top right to bottom left)
    for row in range(3, 6):
          for col in range(4):
                section = [board[row - i][col + i] for i in range(4)]
                score += evaluateSection(section, piece)
    
    return score


#helper method : checks if the inputted columnn is valid on the specified board
def isValidCol(board, column):
        if board[0][column] == 0: #observes the top layer of the first row
            return True
        else:
            return False 

#returns an array of valid columns for a specified board with helper method 'isValidCol'
def getValidCols(board):
    validColumns = []
    for col in range(7): #reads through the columns and stores them in the returned array if it's 'open'
        if isValidCol(board, col):
                validColumns.append(col)
    return validColumns

#checks to see if . . .
#1. player 1 has a winning combination (4 in a row)
#2. the same for player two 
#3. if the board is full (are there valid moves left)
# and returns true if any of the conditions reign true, false if none of them do
def isTerminal(board):
    if (isWinningMove(board, 1) or (isWinningMove(board, 2)) or len(getValidCols(board)) == 0):
        return True 
    return False
    
#performs a minimax implementation
#returns a tuple containing the best move and the points associated with said move
#REFRACTORED FOR ALPHA BETA PRUNING 
def miniMax_AlphaBetaPruning(alpha, beta, board, depth, maxPlayer):
    validCols = getValidCols(board)
    isTerminalVal = isTerminal(board)

    if depth == 0 or isTerminalVal:
        if isTerminalVal: #if the game is won or there are no valid moves to choose from return non and the corresponding score
            if isWinningMove(board, 2):
                    return(None, 1000000)
            elif isWinningMove(board, 1):
                    return(None, -1000000)
            else: 
                    return (None, 0)
        else:
            return (None, scorePosition(board, 2))
    
    #if we're dealing with the maximizing player
    if maxPlayer:
        scorePlaceHolder = -math.inf #initialize a place holder value to negative infinity
        bestColumn = random.choice(validCols)

        for col in validCols: #iterates over valid moves and calls miniMax_AlphaBeta for the minimizing player
            row = nextOpenSpot(board, col)
            boardCopy = [rw[:] for rw in board] #creates copies of the board to simulate moves without affecting the actual game board
            insertPiece(boardCopy, row, col, 2)
            resultingScore = miniMax_AlphaBetaPruning(alpha, beta, boardCopy, depth-1, False)[1] #💡💡💡

            if resultingScore > scorePlaceHolder:
                  scorePlaceHolder = resultingScore
                  bestColumn = col
 
            alpha = max(alpha, scorePlaceHolder) #💡💡💡updates the alpha value with the best fit (highest)
            if alpha >= beta: #💡💡💡prunes the branches (breaks) if alpha is greater than or equal to beta
                break

        return bestColumn, scorePlaceHolder
        
    #if we're not dealing with the maximizing player (same thing just switch the infinity sign, comparison operator, and miniMax boolean)
    else:
        scorePlaceHolder = math.inf # initializes a placeholder valuye to positive infinity
        bestColumn = random.choice(validCols) 

        for col in validCols:  #interates over valid moves and recursively calls miniMax_AlphaBeta for the maximizing player
            row = nextOpenSpot(board, col)
            boardCopy = [rw[:] for rw in board] #creates copies of the board to simulate moves without affecting the actual game board
            insertPiece(boardCopy, row, col, 1)
            resultingScore = miniMax_AlphaBetaPruning(alpha, beta, boardCopy, depth-1, True)[1] #💡💡💡

            if resultingScore < scorePlaceHolder:
                  scorePlaceHolder = resultingScore
                  bestColumn = col

            beta = min(beta, scorePlaceHolder) #💡💡💡updates beta with the best fit value (lowest)
            if alpha >= beta: #💡💡💡prunes (breaks) the branch at the point where alpha becomes greater than or equal to beta
                break

        return bestColumn, scorePlaceHolder
          
def playGame():
    board = createBoard()
    gameOver = False 
    playerTurn = 0 # player 1 is human, 2 is AI like in instructions

    displayBoard(board)

    while gameOver == False:
        if playerTurn == 0:
            column = int(input("Player 1, choose a column 0 to 6: "))
            if (column not in range(7)):
                print("Thats not what I said, try again")
                continue
            if column not in range(7) or not isValidCol(board, column):
                print("Still? Sir.  Please leave")
                continue
            row = nextOpenSpot(board, column)
            insertPiece(board, row, column, 1)
            if isWinningMove(board, 1):
                displayBoard(board)
                print("Player 1 Wins!")
                gameOver = True
        else:
             print("AI is pondering your demise . . . ")
             column = miniMax_AlphaBetaPruning(-math.inf, math.inf, board, 4, True)[0] # For Professor : if you're playing and want a harder version increaes the middle variable                                                                          #
             if isValidCol(board, column):                                             # 💡💡💡 add positive and negative infinity into the parameters 
                  row = nextOpenSpot(board, column)
                  insertPiece(board, row, column, 2)
                  print(f"AI chose column: {column}")
                  if isWinningMove(board, 2):
                       displayBoard(board)
                       print("AI Wins")
                       gameOver = True
                       
        displayBoard(board)
        playerTurn = (playerTurn + 1) % 2 #switch the turns

        #check for a draw
        if len(getValidCols(board)) == 0:
            print("Draw")
            gameOver = True

playGame()