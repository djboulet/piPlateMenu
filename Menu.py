'''
This class creates a menu system for LCD displays with pushbutton switches on
Raspberry PI.


'''

from LCD_Emulator import LCDe


class MenuItem:
    def __init__(self, menuLabel, menuObject):
        self.menuLabel = menuLabel
        self.menuObject = menuObject

    def getNoPointer(self):
        return ' ' + self.menuLabel

    def getWithPointer(self):
        return '>' + self.menuLabel


class Menu:
    # init class and define menu parameters
    def __init__(self, menuItems, aspectRatio):
        self.aspectRatio = aspectRatio
        self.bracketSize = aspectRatio[1]
        self.absPointer = 0
        self.relPointer = 0
        self.bracketPos = 0
        self.menuItems = menuItems
        self.menuLength = len(self.menuItems)
        self.lcd = LCDe(aspectRatio)

    # select previous item in list

    def previousItem(self):
        if (self.relPointer == 0):
            self.bracketPos -= 1
            self.bracketPos %= self.menuLength
        else:
            self.relPointer -= 1
        self.absPointer = (self.bracketPos + self.relPointer) % self.menuLength
        self.showItems()

    # select next item in list
    def nextItem(self):
        if (self.relPointer == self.bracketSize - 1):
            self.bracketPos += 1
            self.bracketPos %= self.menuLength
        else:
            self.relPointer += 1
        self.absPointer = (self.bracketPos + self.relPointer) % self.menuLength
        self.showItems()

    # activate item at current position
    def selectItem(self):
        if hasattr(self.menuItems[self.absPointer].menuObject, '__call__'):
            print('its a function')
            self.menuItems[self.absPointer].menuObject()
        if isinstance(self.menuItems[self.absPointer].menuObject, Menu):
            print('its a menu')
            self.menuItems[self.absPointer].menuObject.processMenu()

    # update display
    def showItems(self):
        self.lcd.clear()

        for y in range(self.bracketSize):
            if y == self.relPointer:
                s = self.menuItems[(self.bracketPos + y) %
                                   self.menuLength].getWithPointer()
            else:
                s = self.menuItems[(self.bracketPos + y) %
                                   self.menuLength].getNoPointer()

            self.lcd.setCursor(0, y)
            self.lcd.writeString(s)

        self.lcd.updateDisplay()

    def processMenu(self):
        valInput = ''
        while (valInput != 'l'):
            # print menu items available
            valInput = input("press a key (u,d,l,r,s): ")
            if (valInput == 'd'):
                self.nextItem()
            if (valInput == 'u'):
                self.previousItem()
            if (valInput == 'r'):
                self.selectItem()
