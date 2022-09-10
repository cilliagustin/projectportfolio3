import colorama
from colorama import Fore
colorama.init()


puzzle = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def style_board(board):
    """
    Add style to the board to display correcly the sudoku
    """
    for x in range(len(board)):
        if x == 0:
            print(" - - - - - - - - - - - - - - - -")
            print(f" |{Fore.CYAN} 1 2 3  {Fore.WHITE}|{Fore.CYAN} 4 5 6  {Fore.WHITE}|{Fore.CYAN} 7 8 9 {Fore.WHITE}|   |")
            print(" - - - - - - - - - - - - - - - -")
        elif x % 3 == 0:
            print(" - - - - - - - - - - - - - - - -")
        for y in range(len(board[0])):
            currentVal = ""
            if board[x][y] == 0:
                currentVal = f"{Fore.RED}{str(board[x][y])}"
            else:
                currentVal = f"{Fore.GREEN}{str(board[x][y])}"
            if y % 3 == 0:
                print(f"{Fore.WHITE} | ", end="")
            if y == 8:
                print(currentVal + f"{Fore.WHITE} | {Fore.CYAN}{x + 1} {Fore.WHITE}|")
            else:
                print(currentVal + " ", end="")
    print(" - - - - - - - - - - - - - - - -")


style_board(puzzle)
