state = ["1","2","3","4","5","6","7","8","9"]

def checkwin():
    # a little hard coding never hurt nobody.

    #horizontal
    if state[0] == state[1] == state[2]:
        return state[0]
    if state[3] == state[4] == state[5]:
        return state[3]
    if state[6] == state[7] == state[8]:
        return state[6]

    #vertical
    if state[0] == state[3] == state[6]:
        return state[0]
    if state[1] == state[4] == state[7]:
        return state[1]
    if state[2] == state[5] == state[8]:
        return state[2]

    #diagonal
    if state[0] == state[4] == state[8]:
        return state[0]
    if state[2] == state[4] == state[6]:
        return state[2]
    return "weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"

def addpoint(char, pos):
    if state[pos] == "O" or state[pos] == "X":
        return False
    state[pos] = char
    return True

def drawscreen():
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])


isO = False

while True:
    chr = 'X'
    if isO:
        chr = 'O'

    drawscreen()
    plce = int(input(chr + " player, go!")) - 1
    if addpoint(chr, plce) == False:
        print("Hey! You can't play there! Try again.")
        continue
    winst = checkwin()
    if winst == "O" or winst == "X":
        print (winst, "player wins!")
        break
    if isO:
        isO = False
    else:
        isO = True