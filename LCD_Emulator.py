class LCDe:
    def __init__(self, aspectRatio):
        self.rows = aspectRatio[1]
        self.cols = aspectRatio[0]
        self.contents = '_' * self.rows * self.cols
        # self.contents = 'abcdefghijklmnopqrstuvwxyzABCDEF'
        self.cursorX = 0
        self.cursorY = 0
        self.size = self.rows*self.cols

    def home(self):
        self.cursorX = 0
        self.cursorY = 0

    def updateDisplay(self):
        for k in range(self.rows):
            startPos = k * self.cols
            endPos = k * self.cols + self.cols - 1
            print(self.contents[startPos:endPos])
        print()

    def setCursor(self, x, y):
        self.cursorX = x
        self.cursorY = y

    def writeString(self, s):
        insertPoint = self.cursorX + self.cursorY * self.cols
        part1 = self.contents[0:insertPoint]
        part2 = s
        part3 = self.contents[insertPoint + len(part2):self.size]
        self.contents = part1 + part2 + part3

    def clear(self):
        self.contents = '_' * self.rows * self.cols
