"""
PROG::pathFind.py
AUTHOR::Kevin.P.Barnett
DATE::Nov.18.2015
"""
import time

class Space:
    def __init__(self, name, dir):
        if isinstance(name, str):
            self.name = name
        else:
            raise Exception("In Class Space: Valid Must Be Bool")
        if isinstance(dir, list):
            self.dir = dir
        else:
            raise Exception("In Class Space: Dir Must Be List")

    def appendDir(self, char):
        if isinstance(char, str) and len(char) == 1:
            self.dir.append(char)
        else:
            raise Exception("In Class Space: Char Must Be Character")

    def removeDir(self, char):
        if isinstance(char, str) and len(char) == 1 and self.dir != []:
            self.dir.remove(self.dir.index(char))
        else:
            raise Exception("In Class Space: Char Must Be Character")

class Board:
    def __init__(self):
        self.board = []
        self.height = 0
        self.width = 0

    def getBoardFromFile(self, fileName):
        file = open(fileName)
        tempList = []
        for line in file:
            for char in line.strip().split():
                tempList.append(char)
            self.board += [tempList[:]]
            tempList.clear()
        for line in self.board:
            self.height += 1
            for space in range(len(line)):
                self.width += 1
                if line[space] == '-':
                    line[space] = Space(' ', [])
                elif line[space] == 'X' or line[space] == 'S' or line[space] == 'E':
                    line[space] = Space(line[space], [])
                else:
                    raise Exception("Invalid Character in File:", fileName)
        self.width //= self.height

    def get3DBoardFromFile(self, fileName):
        tempBoard = []
        tempList = []
        for line in open(fileName):
            if line == '\n':
                self.board.append(tempBoard[:])
                tempBoard.clear()
            else:
                for char in line.strip().split():
                    tempList.append(char)
                tempBoard += [tempList[:]]
                tempList.clear()

    def print(self):
        for line in self.board:
            for space in line:
                print("Space:(Name:", space.name, " Dir:", space.dir, ')', end='')
            print()

    def printBoard(self):
        for line in self.board:
            for space in line:
                print(space.name, ' ', end='')
            print()
        print()

    def sideCheck(self):
        for line in range(len(self.board)):
            for space in range(len(self.board[line])):
                if not self.board[line][space].name == 'X':
                    if space > 0 and not(self.board[line][space-1].name == 'X'):
                        self.board[line][space].appendDir('L')

                    if space < self.width-1 and not(self.board[line][space+1].name == 'X'):
                        self.board[line][space].appendDir('R')

                    if line > 0 and not(self.board[line-1][space].name == 'X'):
                        self.board[line][space].appendDir('U')

                    if line < self.height-1 and not(self.board[line+1][space].name == 'X'):
                        self.board[line][space].appendDir('D')

    def findIndexOfS(self):
        for line in range(len(self.board)):
            for space in range(len(self.board[line])):
                if self.board[line][space].name == 'S':
                    return space, line

def findPath(board, x, y):
    height = len(board.board)
    width = len(board.board[0])
    for many in range((height+width)*2):
            for by in range(height):
                for bx in range(len(board.board[by])):
                    dir = board.board[by][bx].dir
                    if len(dir) <= 1 and board.board[by][bx].name == ' ':
                        board.board[by][bx].name = 'X'
                        if len(dir):
                            if dir[0] == 'L':
                                board.board[by][bx-1].dir.remove('R')
                            elif dir[0] == 'U':
                                board.board[by-1][bx].dir.remove('D')
                            elif dir[0] == 'R':
                                board.board[by][bx+1].dir.remove('L')
                            else:
                                board.board[by+1][bx].dir.remove('U')
    pathList = []
    while True:
        pathList.append((x, y))
        dir = board.board[y][x].dir
        if board.board[y][x].name == 'E':
            return pathList
        if dir[0] == 'L':
            board.board[y][x-1].dir.remove('R')
            x, y = x-1, y
        elif dir[0] == 'U':
            board.board[y-1][x].dir.remove('D')
            x, y = x, y-1
        elif dir[0] == 'R':
            board.board[y][x+1].dir.remove('L')
            x, y = x+1, y
        else:
            board.board[y+1][x].dir.remove('U')
            x, y = x, y+1

def main():
    c = Board()
    c.get3DBoardFromFile("3d.txt")
    for z in c.board:
        for y in z:
            for x in y:
                print(x, end='')
            print()
        print()
    #c.getBoardFromFile("big.txt")
    #c.sideCheck()
    #c.printBoard()
    #x, y = c.findIndexOfS()
    #tempS = time.clock()
    #print(findPath(c, x, y))
    #tempE = time.clock()
    #print("Elapsed Time: ", tempE-tempS)

if __name__ == "__main__":
    main()
