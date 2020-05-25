from Menu import *

aspectRatio = (16, 2)


def printA():
    print('the letter a')


def printA1():
    print('the letter a1')


def printA2():
    print('the letter a2')


def printB():
    print('the letter b')


def printC():
    print('the letter c')


# create a menu
subMenu = Menu(
    [
        MenuItem('Print A1', printA1),
        MenuItem('Print A2', printA2)
    ],
    aspectRatio
)

mainMenu = Menu(
    [
        MenuItem('Print A', subMenu),
        MenuItem('Print B', printB),
        MenuItem('Print C', printC)
    ],
    aspectRatio
)

mainMenu.processMenu()

# print(printA.__class__)
# if type(printA) is function:
#     print('obeject is function')
# exit()

# create menu
# myMainMenu.processMenu()
