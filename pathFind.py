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

class PathFind:
    def __init__(self):
        self.board = []
        self.height = 0
        self.width = 0
        self.depth = 0

    def getBoardFromFile(self, fileName):
        file = open(fileName)
        tempList = []
        for y in file:
            for char in y.strip().split():
                tempList.append(char)
            self.board += [tempList[:]]
            tempList.clear()
        for y in self.board:
            self.height += 1
            for x in range(len(y)):
                self.width += 1
                if y[x] == '-':
                    y[x] = Space(' ', [])
                elif y[x] == 'X' or y[x] == 'S' or y[x] == 'E':
                    y[x] = Space(y[x], [])
                else:
                    raise Exception("Invalid Character in File:", fileName)
        self.width //= self.height

    def get3DBoardFromFile(self, fileName):
        tempBoard = []
        tempList = []
        for y in open(fileName):
            self.height += 1
            if y == '\n':
                self.board.append(tempBoard[:])
                tempBoard.clear()
                self.depth += 1
            else:
                for char in y.strip().split():
                    self.width += 1
                    tempList.append(char)
                tempBoard += [tempList[:]]
                tempList.clear()
        for z in self.board:
            for y in z:
                for x in range(len(y)):
                    if y[x] == '-':
                        y[x] = Space(' ', [])
                    elif y[x] == 'X' or y[x] == 'S' or y[x] == 'E':
                        y[x] = Space(y[x], [])
                    else:
                        raise Exception("Invalid Character in File:", fileName)

    def print(self):
        for y in self.board:
            for x in y:
                print("x:(Name:", x.name, " Dir:", x.dir, ')', end='')
            print()

    def print3d(self):
        for z in self.board:
            for y in z:
                for x in y:
                    print("x:(Name:", x.name, " Dir:", x.dir, ')', end='')
                print()
            print()

    def printBoard(self):
        for y in self.board:
            for x in y:
                print(x.name, ' ', end='')
            print()
        print()

    def print3dBoard(self):
        for z in self.board:
            for y in z:
                for x in y:
                    print(x.name, ' ', end='')
                print()
            print()
        print()

    def sideCheck(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if not self.board[y][x].name == 'X':
                    if x > 0 and not(self.board[y][x-1].name == 'X'):
                        self.board[y][x].appendDir('W')

                    if x < self.width-1 and not(self.board[y][x+1].name == 'X'):
                        self.board[y][x].appendDir('E')

                    if y > 0 and not(self.board[y-1][x].name == 'X'):
                        self.board[y][x].appendDir('N')

                    if y < self.height-1 and not(self.board[y+1][x].name == 'X'):
                        self.board[y][x].appendDir('S')

    def sideCheck3d(self):
        for z in range(len(self.board)):
            for y in range(len(self.board[z])):
                for x in range(len(self.board[z][y])):
                    if not self.board[z][y][x].name == 'X':
                        if x > 0 and not(self.board[z][y][x-1].name == 'X'):
                            self.board[z][y][x].appendDir('W')

                        if x < self.width-1 and not(self.board[z][y][x+1].name == 'X'):
                            self.board[z][y][x].appendDir('E')

                        if y > 0 and not(self.board[z][y-1][x].name == 'X'):
                            self.board[z][y][x].appendDir('N')

                        if y < self.height-1 and not(self.board[z][y+1][x].name == 'X'):
                            self.board[z][y][x].appendDir('S')

                        if z > 0 and not(self.board[z-1][y][x].name == 'X'):
                            self.board[z][y][x].appendDir('D')

                        if z < self.depth-1 and not(self.board[z+1][y][x].name == 'X'):
                            self.board[z][y][x].appendDir('U')

    def findIndexOfS(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].name == 'S':
                    return x, y

    def findIndexOfS3d(self):
        for z in range(len(self.board)):
            for y in range(len(self.board[z])):
                for x in range(len(self.board[z][y])):
                    if self.board[z][y][x].name == 'S':
                        return x, y, z

    def findPath(self):
        height = len(self.board)
        width = len(self.board[0])
        for many in range((height+width)*2):
                for by in range(height):
                    for bx in range(len(self.board[by])):
                        dir = self.board[by][bx].dir
                        if len(dir) <= 1 and self.board[by][bx].name == ' ':
                            self.board[by][bx].name = 'X'
                            if len(dir):
                                if dir[0] == 'W':
                                    self.board[by][bx-1].dir.remove('E')
                                elif dir[0] == 'N':
                                    self.board[by-1][bx].dir.remove('S')
                                elif dir[0] == 'E':
                                    self.board[by][bx+1].dir.remove('W')
                                else:
                                    self.board[by+1][bx].dir.remove('N')
        pathList = []
        x, y = self.findIndexOfS()
        while True:
            pathList.append((x, y))
            dir = self.board[y][x].dir
            if self.board[y][x].name == 'E':
                return pathList
            if dir[0] == 'W':
                self.board[y][x-1].dir.remove('E')
                x, y = x-1, y
            elif dir[0] == 'N':
                self.board[y-1][x].dir.remove('S')
                x, y = x, y-1
            elif dir[0] == 'E':
                self.board[y][x+1].dir.remove('W')
                x, y = x+1, y
            else:
                self.board[y+1][x].dir.remove('N')
                x, y = x, y+1

    def findPath3d(self):
        depth = len(self.board)
        height = len(self.board[0])
        width = len(self.board[0][0])
        for many in range((height+width+depth)*2):
            for bz in range(depth):
                for by in range(height):
                    for bx in range(len(self.board[by])):
                        dir = self.board[bz][by][bx].dir
                        if len(dir) <= 1 and self.board[bz][by][bx].name == ' ':
                            self.board[bz][by][bx].name = 'X'
                            if len(dir):
                                if dir[0] == 'W':
                                    self.board[bz][by][bx-1].dir.remove('E')
                                elif dir[0] == 'N':
                                    self.board[bz][by-1][bx].dir.remove('S')
                                elif dir[0] == 'D':
                                    self.board[bz-1][by][bx].dir.remove('U')
                                elif dir[0] == 'E':
                                    self.board[bz][by][bx+1].dir.remove('W')
                                elif dir[0] == 'U':
                                    self.board[bz+1][by][bx].dir.remove('D')
                                else:
                                    self.board[bz][by+1][bx].dir.remove('N')
        pathList = []
        x, y, z = self.findIndexOfS3d()
        while True:
            pathList.append((x, y, z))
            dir = self.board[z][y][x].dir
            if self.board[z][y][x].name == 'E':
                return pathList
            if dir[0] == 'W':
                self.board[z][y][x-1].dir.remove('E')
                x, y, z = x-1, y, z
            elif dir[0] == 'N':
                self.board[z][y-1][x].dir.remove('S')
                x, y, z = x, y-1, z
            elif dir[0] == 'E':
                self.board[z][y][x+1].dir.remove('W')
                x, y, z = x+1, y, z
            elif dir[0] == 'U':
                self.board[z+1][y][x].dir.remove('D')
                x, y, z = x, y, z+1
            elif dir[0] == 'D':
                self.board[z-1][y][x].dir.remove('U')
                x, y, z = x, y, z-1
            else:
                self.board[z][y+1][x].dir.remove('N')
                x, y, z = x, y+1, z


def main():
    c = PathFind()
    c.get3DBoardFromFile("3d.txt")
    c.sideCheck3d()
    c.print3d()
    #c.getBoardFromFile("big.txt")
    #c.sideCheck()
    #c.printBoard()
    tempS = time.clock()
    print(c.findPath3d())
    tempE = time.clock()
    print("Elapsed Time: ", tempE-tempS)

if __name__ == "__main__":
    main()
