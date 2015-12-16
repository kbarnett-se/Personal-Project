"""
PROG::tictactoe.py
AUTHOR::Kevin.P.Barnett
DATE::Dec.14.2015
"""
import turtle, math, random

class TicB:
    def __init__(self):
        self.board = [[], [], []]
        self.board = self.createBoard(self.board, '-')
        self.conflictResolution = [[], [], []]
        self.conflictResReset()

    def createBoard(self, valList, val):
        for y in range(3):
            for x in range(3):
                valList[y].append(val)
        return valList

    def conflictResReset(self):
        it = [3, 2, 3, 2, 4, 2, 3, 2, 3]
        for y in range(3):
            for x in range(3):
                self.conflictResolution[y].append(it[x+(y*3)])

    def printB(self):
        for y in range(3):
            for x in range(3):
                print(self.board[y][x], ' ', end='')
            print()
        print()

    def placeX(self, x, y):
        self.board[y][x] = 'X'

    def placeO(self, x, y):
        self.board[y][x] = 'O'

    def checkWin(self):
        if self.check('X'):
            return 'X'
        elif self.check('O'):
            return 'O'
        else:
            for y in self.board:
                if '-' in y:
                    return '-'
            return 'C'

    def check(self, char):
        #Right
        for y in self.board:
            line = True
            for x in y:
                if not(char == x):
                    line = False
            if line:
                return True
            line = False
        #Down
        for x in range(3):
            line = True
            for y in range(3):
                if not(char == self.board[y][x]):
                    line = False
            if line:
                return True
            line = False
        #Diags
        if self.board[0][0] == char and self.board[1][1] == char and self.board[2][2] == char:
            return True
        elif self.board[0][2] == char and self.board[1][1] == char and self.board[2][0] == char:
            return True
        else:
            return False


    def AI(self, ch):
        posList, negList = [[], [], []], [[], [], []]
        posList, negList = self.createBoard(posList, 0), self.createBoard(negList, 0)
        if ch == 'X':
            antiCh = 'O'
        else:
            antiCh = 'X'
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == '-':
                    if (x > 0 and self.board[y][x-1] == ch):
                        posList[y][x] += 1
                    if (x > 1 and self.board[y][x-2] == ch):
                        posList[y][x] += 1
                    if (y > 0 and self.board[y-1][x] == ch):
                        posList[y][x] += 1
                    if (y > 1 and self.board[y-2][x] == ch):
                        posList[y][x] += 1
                    if (x < 2 and self.board[y][x+1] == ch):
                        posList[y][x] += 1
                    if (x < 1 and self.board[y][x+2] == ch):
                        posList[y][x] += 1
                    if (y < 2 and self.board[y+1][x] == ch):
                        posList[y][x] += 1
                    if (y < 1 and self.board[y+2][x] == ch):
                        posList[y][x] += 1
                    if (x < 2 and y < 2 and self.board[y+1][x+1] == ch):
                        posList[y][x] += 1
                    if (x < 1 and y < 1 and self.board[y+2][x+2] == ch):
                        posList[y][x] += 1
                    if (x > 0 and y < 2 and self.board[y+1][x-1] == ch):
                        posList[y][x] += 1
                    if (x > 1 and y < 1 and self.board[y+2][x-2] == ch):
                        posList[y][x] += 1
                    if (x < 2 and y > 0 and self.board[y-1][x+1] == ch):
                        posList[y][x] += 1
                    if (x < 1 and y > 1 and self.board[y-2][x+2] == ch):
                        posList[y][x] += 1
                    if (x > 0 and y > 0 and self.board[y-1][x-1] == ch):
                        posList[y][x] += 1
                    if (x > 1 and y > 1 and self.board[y-2][x-2] == ch):
                        posList[y][x] += 1
                    if (x > 0 and self.board[y][x-1] == antiCh):
                        posList[y][x] -= 1
                    if (x > 1 and self.board[y][x-2] == antiCh):
                        posList[y][x] -= 1
                    if (y > 0 and self.board[y-1][x] == antiCh):
                        posList[y][x] -= 1
                    if (y > 1 and self.board[y-2][x] == antiCh):
                        posList[y][x] -= 1
                    if (x < 2 and self.board[y][x+1] == antiCh):
                        posList[y][x] -= 1
                    if (x < 1 and self.board[y][x+2] == antiCh):
                        posList[y][x] -= 1
                    if (y < 2 and self.board[y+1][x] == antiCh):
                        posList[y][x] -= 1
                    if (y < 1 and self.board[y+2][x] == antiCh):
                        posList[y][x] -= 1
                    if (x < 2 and y < 2 and self.board[y+1][x+1] == antiCh):
                        posList[y][x] -= 1
                    if (x < 1 and y < 1 and self.board[y+2][x+2] == antiCh):
                        posList[y][x] -= 1
                    if (x > 0 and y < 2 and self.board[y+1][x-1] == antiCh):
                        posList[y][x] -= 1
                    if (x > 1 and y < 1 and self.board[y+2][x-2] == antiCh):
                        posList[y][x] -= 1
                    if (x < 2 and y > 0 and self.board[y-1][x+1] == antiCh):
                        posList[y][x] -= 1
                    if (x < 1 and y > 1 and self.board[y-2][x+2] == antiCh):
                        posList[y][x] -= 1
                    if (x > 0 and y > 0 and self.board[y-1][x-1] == antiCh):
                        posList[y][x] -= 1
                    if (x > 1 and y > 1 and self.board[y-2][x-2] == antiCh):
                        posList[y][x] -= 1
                else:
                    posList[y][x], negList[y][x] = 0, 0
        sx, sy = 0, 0
        for y in range(3):
            for x in range(3):
                if abs(posList[y][x]) > abs(posList[sy][sx]):
                    sx, sy = x, y
        positionList = []
        for y in range(3):
            for x in range(3):
                if abs(posList[sy][sx]) == abs(posList[y][x]):
                    positionList.append((x, y))
        high = 0
        decideList =[]
        for run2 in range(2):
            for xy in positionList:
                if (not run2) and high < self.conflictResolution[xy[1]][xy[0]]:
                    high = self.conflictResolution[xy[1]][xy[0]]
                if run2 and high == self.conflictResolution[xy[1]][xy[0]]:
                    decideList.append(xy)

        return decideList[random.randint(0, len(decideList)-1)]

    def inputMove(self):
        while True:
            move = input("Enter Move Such as \"0 1\": ").split()
            move = int(move[0]), int(move[1])
            if self.board[move[1]][move[0]] == '-':
                return move[0], move[1]
            else:
                print("Invalid Move")

class Screen:
    def __init__(self, b):
        turtle.up()
        turtle.hideturtle()
        turtle.speed(0)
        self.drawCross()
        self.drawCross()
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        if isinstance(b, TicB):
            self.b = b
        else:
            raise Exception("b Must be Type: TicB")

    def update(self, b):
        if isinstance(b, TicB):
            self.b = b
        else:
            raise Exception("b Must be Type: TicB")

    def drawCross(self):
        turtle.forward(50)
        turtle.right(90)
        turtle.down()
        turtle.forward(150)
        turtle.back(150)
        turtle.up()
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.down()
        turtle.forward(150)
        turtle.back(150)
        turtle.up()
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)

    def drawBoard(self):
        for y in range(3):
            for x in range(3):
                self.moveToPos(x, y)
                if self.b.board[y][x] == 'X':
                    self.drawX()
                elif self.b.board[y][x] == 'O':
                    self.drawO()
                turtle.home()

    def drawX(self):
        turtle.right(45)
        turtle.down()
        turtle.forward(math.sqrt(5000))
        turtle.right(135)
        turtle.up()
        turtle.forward(50)
        turtle.right(135)
        turtle.down()
        turtle.forward(math.sqrt(5000))
        turtle.left(135)
        turtle.up()
        turtle.forward(50)
        turtle.right(180)

    def drawO(self):
        turtle.forward(25)
        turtle.right(180)
        turtle.down()
        turtle.circle(25)
        turtle.up()
        turtle.left(180)
        turtle.back(25)

    def moveToPos(self, x, y):
        turtle.forward(x*50)
        turtle.right(90)
        turtle.forward(y*50)
        turtle.left(90)

def playHuman(hum, xo):
    player = xo
    b = TicB()
    s = Screen(b)
    if hum:
        print("Player One: Is X, Enter a Coordinates [0,2] Origin at Top Left")
    while True:
        if player:
            x, y = b.inputMove()
            b.placeX(x, y)
            s.update(b)
            s.drawBoard()
            if b.checkWin() == 'X':
                return 'X'
            elif b.checkWin() == 'C':
                return 'C'
        else:
            if hum:
                x, y = b.inputMove()
            else:
                x, y = b.AI('X')
            b.placeO(x, y)
            s.update(b)
            s.drawBoard()
            if b.checkWin() == 'O':
                return 'O'
            elif b.checkWin() == 'C':
                return 'C'

        player = not player

def main():
    win = playHuman(bool(int(input("Against AI or Human(0, 1): "))), bool(input("First Player O's or X's(0, 1): ")))
    if win == 'X':
        print("X's Win!!!")
    elif win == 'O':
        print("O's Win!!!")
    else:
        print("Cats Game...")

if __name__ == "__main__":
  main()
