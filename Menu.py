'''
This class creates a menu system for LCD displays with pushbutton switches on
Raspberry PI.

'''

import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd


# class to define MenuItems and their properties (label,action)
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

        # initialize menu parameters
        self.aspectRatio = aspectRatio      # display dimensions
        self.lcd_columns = aspectRatio[0]   # columns
        self.lcd_rows = aspectRatio[1]      # rows
        self.absPointer = 0                 # absolute pointer to item in list
        self.relPointer = 0                 # pointer relative to start of bracket
        self.bracketPos = 0                 # start of bracket
        self.menuItems = menuItems          # list of menu items passed on init
        self.menuSize = len(self.menuItems)  # number of menu items

        # Initialise I2C bus.
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Initialise the LCD class
        self.lcd = character_lcd.Character_LCD_RGB_I2C(
            self.i2c, self.lcd_columns, self.lcd_rows)

        # start menu
        self.runMenu()

    # launch the menu and process button pushes
    def runMenu(self):
        # update the display
        self.showItems()

        # loop until left button pushed
        while True:
            if self.lcd.left_button:
                print("Left!")
                return

            # move to previous item
            elif self.lcd.up_button:
                print("Up!")
                self.previousItem()
                self.showItems()

            # move to next item in menu
            elif self.lcd.down_button:
                print("Down!")
                self.nextItem()
                self.showItems()

            # select item indicated by ">"
            elif self.lcd.right_button:
                print("Right!")
                self.selectItem()
                self.showItems()

            # exit the program
            elif self.lcd.select_button:
                print("Select!")
                exit()
            else:
                time.sleep(0.1)
                pass

    # select previous item in list
    def previousItem(self):
        if (self.relPointer == 0):
            self.bracketPos -= 1
            self.bracketPos %= self.menuSize
        else:
            self.relPointer -= 1
        self.absPointer = (self.bracketPos + self.relPointer) % self.menuSize

    # select next item in list
    def nextItem(self):
        if (self.relPointer == self.lcd_rows - 1):
            self.bracketPos += 1
            self.bracketPos %= self.menuSize
        else:
            self.relPointer += 1
        self.absPointer = (self.bracketPos + self.relPointer) % self.menuSize

    # activate item at current position
    def selectItem(self):
        menuObj = self.menuItems[self.absPointer].menuObject

        # if object is "callable" then it's a function and can be called
        if hasattr(menuObj, '__call__'):
            # call the object function
            menuObj()

        # if object is a list then it is assumed to be a submenu
        if type(menuObj) is list:
            # create a new menu object and launch it
            Menu(menuObj, self.aspectRatio)

    # update lcd display given position of bracket and relative pointer position
    def showItems(self):
        self.lcd.clear()
        for y in range(self.lcd_rows):
            # relative pointer is pointing to row 'y' so we add '>'
            if y == self.relPointer:
                s = self.menuItems[(self.bracketPos + y) %
                                   self.menuSize].getWithPointer()
            # else we don't
            else:
                s = self.menuItems[(self.bracketPos + y) %
                                   self.menuSize].getNoPointer()

            # set cursor to current row 'y' and print string 's'
            self.lcd.cursor_position(0, y)
            self.lcd.message = s
