import os  # To clear the console
import colorama
from colorama import Fore
from text import *
colorama.init()


puzzle = [
    [5, 0, 9, 0, 1, 0, 0, 8, 2],
    [8, 3, 1, 0, 5, 0, 0, 0, 0],
    [6, 0, 2, 9, 0, 0, 1, 0, 0],
    [4, 1, 0, 3, 0, 8, 2, 9, 0],
    [9, 2, 0, 5, 6, 1, 0, 0, 7],
    [0, 0, 0, 4, 2, 0, 0, 0, 8],
    [0, 8, 0, 0, 0, 6, 3, 0, 5],
    [0, 0, 7, 0, 3, 0, 6, 0, 0],
    [0, 9, 0, 0, 4, 5, 0, 0, 0]
]


def wrong_input(answer):
    print(
        f'\t{Fore.RED}Wrong command: {Fore.YELLOW}"{answer}"'
        f'{Fore.WHITE}. Please enter a valid command.')


def clear():
    """
    Clear terminal in windows or linux
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def exit_app():
    """
    Whenever the user writes exit as an input it triggers
    this function. This displays another input that asks the
    user if they are sure they want to exit and closes the app
    if they confirm this
    """
    print("\n\tAre you sure you want to close the app")
    while True:
        answer = input(
            f"\n\tType {Fore.BLUE}yes {Fore.WHITE}to close the App or "
            f"{Fore.BLUE}no {Fore.WHITE}to keep using it: ").lower()
        if answer == "yes":
            quit()
        elif answer == "no":
            break
        else:
            wrong_input(answer)


def main_menu():
    """
    This is the main menu from here the user decides whether
    they want to get information on the game or the app, if they
    want to run the program or if they want to close the app
    """
    clear()
    print(TITLE)
    print(MAIN_MENU_TEXT)
    while True:
        answer = input(
            f'Write {Fore.BLUE}start{Fore.WHITE} to run the App, '
            f'{Fore.BLUE}information{Fore.WHITE} to get more information about'
            f' the game and how to use the App or {Fore.BLUE}exit{Fore.WHITE} '
            'to close the aplication:\n\tWrite here your command: ').lower()
        if answer == "exit":
            exit_app()
        elif answer == "information":
            information_menu()
        elif answer == "start":
            start_app()
        else:
            wrong_input(answer)


def information_menu():
    """
    This is the menu where the user can see information on the
    history and rules of the game and also learn how to use correctly
    the App.
    """
    clear()
    print(INFORMATION_TEXT)
    while True:
        answer = input(
            f'Write {Fore.BLUE}game{Fore.WHITE} for more information on the '
            f'Puzzle, {Fore.BLUE}app{Fore.WHITE} for a tutorial on the App, '
            f'write {Fore.BLUE}back{Fore.WHITE} to go to the Main Menu or '
            f'{Fore.BLUE}exit{Fore.WHITE} to close the App.\n\tEnter your '
            'command: ').lower()
        if answer == "exit":
            exit_app()
        elif answer == "back":
            main_menu()
        elif answer == "game":
            clear()
            print(INFORMATION_TEXT)
            print(GAME_TEXT)
        elif answer == "app":
            clear()
            print(INFORMATION_TEXT)
            print(APP_TITLE)
            print(APP_TEXT)
            input(f"Press {Fore.BLUE}Enter{Fore.WHITE} to continue")
            style_board(EXAMPLE_BOARD)
            input(f"Press {Fore.BLUE}Enter{Fore.WHITE} to continue")
            print(APP_TEXT2)
        else:
            wrong_input(answer)


def start_app():
    """
    Gets the given values from the user and then solves the sudoku using the
    solve sudoku function.
    """
    run_app_screen()
    while True:
        answer = input(
            f'Write your {Fore.BLUE}numbers{Fore.WHITE} in a correct format to'
            f' add them to the puzzle, write {Fore.BLUE}solve{Fore.WHITE} when'
            f' you are done to get the solution, write {Fore.BLUE}reset'
            f'{Fore.WHITE} to restart the puzzle, write {Fore.BLUE}back'
            f'{Fore.WHITE} to go to the main menu or {Fore.BLUE}exit'
            f'{Fore.WHITE} to close the App: ').lower()
        try:
            if is_number_format_valid(answer):
                # get row col and value from answer
                row, col, value = get_values(answer)
                # updates puzzle with values
                puzzle[row][col] = value
                # Clear screen and display again all texts
                run_app_screen()
            else:
                wrong_input(answer)
        except:
            if answer == "exit":
                exit_app()
            elif answer == "back":
                main_menu()
            elif answer == "reset":
                # Reset puzzle
                reset_puzzle(puzzle)
                # Clear screen and display again all texts
                run_app_screen()
            elif answer == "solve":
                solve_sudoku(puzzle)
            else:
                wrong_input(answer)


def run_app_screen():
    clear()
    print(TITLE)
    print(START_APP_TEXT)
    style_board(puzzle)


def is_number_format_valid(answer):
    """
    Checks if the input has the correct format. 3 numbers divided by comma,
    hyphen or space. the first two numbers are between 1 and 9 and the thirs
    one between 0 and 9
    """
    if int(answer[0]) in range(1, 10) and int(answer[2]) in range(1, 10) and int(answer[4]) in range(10) and len(answer) == 5 and answer[1] == answer[3] and (answer[1] == "," or answer[1] == "-" or answer[1] == " "):  # noqa
        return True


def get_values(input):
    """
    Gets values from input (this will always be in possitions 0, 2, 4) and
    returns them as intergers. Since the first two values are positions in
    lists and this are 0 indexed the number is subtracted 1 to give an easier
    understanding for the user (when the user enters 3 in the position value
    this would equal to the fourth position, so 1 is subtracted so the value
    equals to the third position)
    """
    a = int(input[0]) - 1
    b = int(input[2]) - 1
    c = int(input[4])
    return a, b, c


def reset_puzzle(puzzle):
    """
    Turn all values back to zero (unknown numbers)
    """
    for row in range(9):
        for col in range(9):
            puzzle[row][col] = 0


def solve_sudoku(sudoku):
    """
    Makes a copy of the puzzle and uses the get answer function. if the sudoku
    has a solution displays the solution
    """
    answer = sudoku
    if get_answer(answer):
        print("yes")
    else:
        print("no")


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
            print(
                f" |{Fore.CYAN} 1 2 3  {Fore.WHITE}|{Fore.CYAN} 4 5 6  "
                f"{Fore.WHITE}|{Fore.CYAN} 7 8 9 {Fore.WHITE}|   |")
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
                print(
                    currentVal + f"{Fore.WHITE} | {Fore.CYAN}"
                    f"{x + 1} {Fore.WHITE}|")
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
    this by 3 we get the 1st num for the 3x3 square the number is located in
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


def get_answer(puzzle):
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
            if get_answer(puzzle):
                return True

        """
        If there are no valid numbers reset the number (Re-establish as 0)
        and go to the prevoius number and loop to the next number. Eventually
        this will try all possible combinations until the sudoku is solved
        """
        puzzle[row][col] = 0

    # If no option is valid then the sudoku is unsolvable
    return False


start_app()
