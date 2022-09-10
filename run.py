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
            """
            Create first lines to show the user each column,
            the numbers here are printed in cyan to differentiate 
            from the numbers inside the board
            """
            print(" - - - - - - - - - - - - - - - -")
            print(f" |{Fore.CYAN} 1 2 3  {Fore.WHITE}|{Fore.CYAN} 4 5 6  {Fore.WHITE}|{Fore.CYAN} 7 8 9 {Fore.WHITE}|   |")
            print(" - - - - - - - - - - - - - - - -")
        elif x % 3 == 0:
            # Add lines between rows to create a clear puzzle
            print(" - - - - - - - - - - - - - - - -")
        for y in range(len(board[0])):
            """
            Establish the colour of the number in the board,
            red for 0 (uknown number), green for known numbers
            """
            currentVal = ""
            if board[x][y] == 0:
                currentVal = f"{Fore.RED}{str(board[x][y])}"
            else:
                currentVal = f"{Fore.GREEN}{str(board[x][y])}"
            if y % 3 == 0:
                # Divide with a "|" each 3 columns to create a clear puzzle
                print(f"{Fore.WHITE} | ", end="")
            if y == 8:
                """
                Add the last number of each row and the guide numbers
                The numbers are apllied with the color indicating if is a 
                known or unknown number and the guide number is cyan.
                """
                print(currentVal + f"{Fore.WHITE} | {Fore.CYAN}{x + 1} {Fore.WHITE}|")
            else:
                # All other numbers are located here
                print(currentVal + " ", end="")
    #Last line to close the board
    print(" - - - - - - - - - - - - - - - -")


style_board(puzzle)
