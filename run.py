import colorama
from colorama import Fore
colorama.init()


puzzle = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
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
    # Last line to close the board
    print(" - - - - - - - - - - - - - - - -")


def find_unknown_number(puzzle):
    """
    Looks for next unknown number and returns that location,
    loops through every row and then through each column in every row
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                # Returns the location with a 0 value
                return row, col

    # Returns this when all spaces are compleated            
    return None, None


def option_is_valid(puzzle, option, row, col):
    """
    Check if a option is a valid option. Return True or False
    The number must not be used on the same row, column or 3x3 square
    """
    # Check if number is in row
    selected_row = puzzle[row]
    if option in selected_row:
        return False

    # Check if number is in column
    selected_column = []
    for i in range(9):
        selected_column.append(puzzle[i][col])
    if option in selected_column:
        return False

    """
    # Check in which 3x3 square is the number. Using the // operator
    we get the result of the division ignoring the reminder. Multiplying
    this by 3 we get the first number for the 3x3 square the number is located in
    """
    first_row = (row // 3) * 3
    first_col = (col // 3) * 3

    # Loop in 3x3 square and check if number is there
    for r in range(first_row, first_row + 3):
        for c in range(first_col, first_col + 3):
            if puzzle[r][c] == option:
                return False
    
    # If number is not on row, col or square return True
    return True


def solveSudoku(puzzle):
    """
    Gets a sudoku as parameter and returns the correct solution
    """
    # Find an empty space (first 0 element in puzzle)
    row, col = find_unknown_number(puzzle)

    """
    If row and column = None, None there are no unknown numbers,
    This means the puzzle is resolved, else keep going
    """
    if row is None and col is None:
        return True
    
    # Check all options to fill the unknown number (1 to 9)
    for option in range(1, 10):
        # Check if option could be a possible number
        if option_is_valid(puzzle, option, row, col):
            # Put option in unkown number and mutate list
            puzzle[row][col] = option

            """
            Call again the function to check the next number over
            and over again
            """
            if solveSudoku(puzzle):
                return True
        
        """
        If there are no valid numbers reset the number (Re-establish as 0)
        and go to the prevoius number and loop to the next number. Eventually
        this will try all possible combinations until the sudoku is solved
        """
        puzzle[row][col] = 0
    
    # If no option is valid then the dusoku is unsolvable
    return False


solveSudoku(puzzle)
print(puzzle)