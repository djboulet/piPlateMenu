from Menu import Menu,MenuItem

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


Menu(
    [
        MenuItem('A', [
            MenuItem('A1', printA1),
            MenuItem('A2', printA2),
        ]),
        MenuItem('B', printB),
        MenuItem('C', printC),
    ],
    aspectRatio
)
