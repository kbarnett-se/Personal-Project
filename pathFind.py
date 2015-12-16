"""
PROG::pathFind.py
AUTHOR::Kevin.P.Barnett
DATE::Nov.18.2015
"""

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
    space  = board.board[y][x]
    nm = space.name
    tree = Tree(space)
    if nm == 'E':

    elif not(space.dir == []):
        if 'L' in nm:
            space.removeDir('L')
            board.board[y][x-1].removeDir('R')
            findPath(board, x-1, y))
        if 'U' in nm:
            space.removeDir('U')
            board.board[y-1][x].removeDir('D')
            findPath(board, x, y-1)
        if 'R' in nm:
            space.removeDir('R')
            board.board[y][x+1].removeDir('L')
            findPath(board, x+1, y)
        if 'D' in nm:
            space.removeDir('D')
            board.board[y+1][x].removeDir('U')
            findPath(board, x, y+1)
    else:
        return tree

def main():
    c = Board()
    c.getBoardFromFile("small.txt")
    c.sideCheck()
    c.printBoard()
    x, y = c.findIndexOfS()
    print(findPath(c, x, y))

if __name__ == "__main__":
    main()
