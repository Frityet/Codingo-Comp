"""
This function takes in a sudoku board (represented by a 2D array)
and returns the same board with a suitable answer.

Arguments:
    board (List[List[int]] 2D Array of integers): A 2D array representing the sudoku board
Returns:
    board: A 2D array representing the solved sudoku board with all tiles filled in.
Examples:
    [
        [2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]
    ]
    passed into the function =>
    [
        [2, 5, 8, 7, 3, 6, 9, 4, 1],
        [6, 1, 9, 8, 2, 4, 3, 5, 7],
        [4, 3, 7, 9, 1, 5, 2, 6, 8],
        [3, 9, 5, 2, 7, 1, 4, 8, 6],
        [7, 6, 2, 4, 9, 8, 1, 3, 5],
        [8, 4, 1, 6, 5, 3, 7, 2, 9],
        [1, 8, 4, 3, 6, 9, 5, 7, 2],
        [5, 7, 6, 1, 4, 2, 8, 9, 3],
        [9, 2, 3, 5, 8, 7, 6, 1, 4],
    ]
"""

true = True
false = False

def boardtosquarenum(row, col):
    # I AM BODGE INCARNITE!
    if row > 5:
        if col > 5:
            return 8
        if col > 2:
            return 7
        return 6
    if row > 2:
        if col > 5:
            return 5
        if col > 2:
            return 4
        return 3
    if col > 5:
        return 2
    if col > 2:
        return 1
    return 0

def coladd(square):
    #can't be bothered to make it a mathy one liner. Too bad!
    col = 0
    if square > 5:
        return 6
    if square > 2:
        return 3
    return 0

def sudoku_assemble_squaredata(board):
    squaredata = [[] * 9] * 9
    
    #oh this is terrible. this literally jsut converts the regular board to an array of 9 squares, each of which is an array of numbers, all in Z pattern.
    square = 0
    row = 0
    column = 0
    while square < 9:
        data = []
        while column < 3:
            while row < 3:
                data.append(board[column + coladd(square)][row + int((square * 3) % 9)])
                row = row + 1
            row = 0
            column = column + 1
        squaredata[square] = data
        square = square + 1
        row = 0
        column = 0
    return squaredata

def concat_AND(list1, list2):
    finallist = []
    for x in list1:
        if x in list2:
            finallist.append(x)
    return finallist


def sudoku_possibility_calc(board):
    possibilities = [[[] * 1024] * 1024] * 1024

    #calculation of rows
    row = 0
    pos = 0
    while row < 9:
        while pos < 9:
            if board[row][pos] == 0:
                #takes every number it cannot be
                nums = []
                for num in board[row]:
                    if num != 0:
                        nums.append(num)
                #convert to every number it can be
                posnums = []
                for x in range(1, 10):
                    if x not in nums:
                        posnums.append(x)
                possibilities[row][pos].append(posnums)
            pos += 1
        row += 1

    #calculation of columns
    col = 0
    pos = 0
    while col < 9:
        while pos < 9:
            if board[col][pos] == 0:
                #takes every number it cannot be
                nums = []
                for num in board[col]:
                    if num != 0:
                        nums.append(num)
                #convert to every number it can be
                posnums = []
                for x in range(1, 10):
                    if x not in nums:
                        posnums.append(x)
                possibilities[row][pos] = concat_AND(possibilities[row][pos], posnums)
            pos += 1
        col += 1
    
    #calculation of squares
    squaredata = sudoku_assemble_squaredata(board)
    col = 0
    row = 0

    while col < 9:
        while row < 9:
            sqnum = boardtosquarenum(row, col)
            nums = []
            # get every num it cant be
            for x in range(1, 10):
                if x in squaredata[sqnum]:
                    nums.append(x)
            # convert to every number it can be
            posnums = []
            for x in range(1, 10):
                if x not in nums:
                    posnums.append(x)
                possibilities[row][col] = concat_AND(possibilities[row][col], posnums)
            row = row + 1
        col = col + 1

    return possibilities


def sudoku_solver(board):
    possibilities = sudoku_possibility_calc(board)
    print(possibilities)
    return board
