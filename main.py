board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' ',
}

player = 'X'
bot = 'O'


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')


printBoard(board)


def isFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def drawCheck():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def winningCheck():
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[5] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[3] != ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if (position >= 1 and position <= 9) and isFree(position):
        board[position] = letter
        printBoard(board)
        if drawCheck():
            print("Draw!")
            exit()
        if winningCheck():
            if letter == 'O':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position (1-9):  "))
        insertLetter(letter, position)
        return


def determineWinner(mark):
    if board[1] == board[2] and board[2] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[5] == board[9] and board[1] == mark:
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[3] == mark:
        return True
    else:
        return False


def playerMove():
    position = int(input("Enter a position for 'X'(1-9): "))
    insertLetter(player, position)
    return


def botMove():
    bestScore = -1000
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = miniMax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


def miniMax(board, isMaximizing):
    if determineWinner(bot):
        return 1
    elif determineWinner(player):
        return -1
    elif drawCheck():
        return 0
    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = miniMax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = miniMax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


while not winningCheck():
    playerMove()
    botMove()
