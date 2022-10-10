import colorama
from colorama import Fore
colorama.init()

TITLE = """
                    ██╗   ██╗██████╗  ██████╗ ██╗  ██╗██╗   ██╗
    ██████████████╗ ██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║
    ██████████████║ ██║   ██║██║  ██║██║   ██║█████╔╝ ██║   ██║
    ████╔═════════╝ ██║   ██║██║  ██║██║   ██║██╔═██╗ ██║   ██║
    ████║           ╚██████╔╝██████╔╝╚██████╔╝██║  ██╗╚██████╔╝
    ██████████████╗  ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝
    ██████████████║   ██████╗ ██╗     ██╗   ██╗███████╗██████╗
    ╚═════════████║  ██╔═══██╗██║     ██║   ██║██╔════╝██╔══██╗
              ████║  ██║   ██║██║     ██║   ██║█████╗  ██████╔╝
    ██████████████║  ██║   ██║██║     ╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ██████████████║  ██║   ██║██║     ╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚═════════════╝  ╚██████╔╝███████╗ ╚████╔╝ ███████╗██║  ██║
                      ╚═════╝ ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝

"""

MAIN_MENU_TEXT = """
Hello, and welcome to the Sudoku Solver App. Here you will be able finally to
get the correct answer for the puzzle you have been trying all morning or just
check if you complete it correctly.
"""

INFORMATION_TEXT = (
  " _____ _   _ ______ ______________  ___  ___ _____ _____ _____ _   _"
  "\n|_   _| \\ | ||  ___|  _  | ___ \\  \\/  | / _ \\_   _|_   _|  _  | \\ |"
  " |"
  "\n  | | |  \\| || |_  | | | | |_/ / .  . |/ /_\\ \\| |   | | | | | |  \\| |"
  "\n  | | | . ` ||  _| | | | |    /| |\\/| ||  _  || |   | | | | | | . ` |"
  "\n _| |_| |\\  || |   \\ \\_/ / |\\ \\| |  | || | | || |  _| |_\\ \\_/ / |"
  "\\  |"
  "\n \\___/\\_| \\_/\\_|    \\___/\\_| \\_\\_|  |_/\\_| |_/\\_/  \\___/ \\__"
  "_/\\_| \\_/"
  "\n\nDo you wish to know more about the game Sudoku? Do you want to know how"
  " to use\ncorrectly the App?"
)

GAME_TEXT = """
 _____ _   _  _____   _____   ___  ___  ___ _____
|_   _| | | ||  ___| |  __ \\ / _ \\ |  \\/  ||  ___|
  | | | |_| || |__   | |  \\// /_\\ \\| .  . || |__
  | | |  _  ||  __|  | | __ |  _  || |\\/| ||  __|
  | | | | | || |___  | |_\\ \\| | | || |  | || |___
  \\_/ \\_| |_/\\____/   \\____/\\_| |_/\\_|  |_/\\____/

Although the name "Sudoku" comes from Japan, the earliest versions of this
game came from France in the late 19th century, when some newspapers
started experimenting with mathematical games that were displayed in 9x9
grids.
The earliest versions of the modern puzzle were created in Connersville,
Indiana in the late 1970s, where Dell Magazine started publishing
"NumberPlace", but it wasn’t until 1984 that Monthly Nikolist, a Japanese
magazine, started publishing the puzzle under the name Sudoku. This name
comes as an abbreviation of Suji wa dokushin ni kagiru (The digits must be
single) and in the following years they polished the game: added a maximum
of 32 of the given numbers and distributed them more evenly though the
board.
"""

GAME_TEXT_2 = """
In 1997 Wayne Gould, a judge of Hong Kong, developed a computer program that
could easily develop new puzzles. He brought that to The Time Magazine in
England that started publishing them, and quickly it spread through the rest
of the world under the "Sudoku" name.
The rules are fairly simple, The user is given a 9x9 grid with certain amount
of numbers already written (The less amount of numbers given the hardest is
the game) and the goal of the player is to complete all the grid with numbers
from 1 to 9 without repeating any number in a row, a column or a 3x3 square.
"""

APP_TITLE = """
 _____ _   _  _____    ___  ____________
|_   _| | | ||  ___|  / _ \\ | ___ \\ ___ |
  | | | |_| || |__   / /_\\ \\| |_/ / |_/ /
  | | |  _  ||  __|  |  _  ||  __/|  __/
  | | | | | || |___  | | | || |   | |
  \\_/ \\_| |_/\\____/  \\_| |_/\\_|   \\_|
"""

APP_TEXT = (
    'To use the App is pretty simple. Once in the Main Menu write '
    f'{Fore.BLUE}start{Fore.WHITE}, this will\nshow you a 9x9 grid all '
    'completed by zeros, this number represents an unknown\nnumber. Use the '
    f'guiding numbers colored in {Fore.BLUE}blue{Fore.WHITE} to locate a '
    'square where you \nhave a number that was given by you in the game and '
    f'insert it. The way you do\nthis is by entering 3 numbers separated by a '
    f'{Fore.BLUE}comma{Fore.WHITE}, a {Fore.BLUE}hyphen{Fore.WHITE}, a '
    f'{Fore.BLUE}space{Fore.WHITE} or just\nwrite them all together with '
    f'{Fore.BLUE}no separation{Fore.WHITE} at all. \nThe first one being the '
    f'{Fore.BLUE}row {Fore.WHITE}position, the second being the {Fore.BLUE}'
    f'column {Fore.WHITE}position and\nthe third one the {Fore.BLUE}value'
    f'{Fore.WHITE}.\nThis means that {Fore.BLUE}4,2,9{Fore.WHITE} would be '
    f'that in the fourth{Fore.BLUE} row{Fore.WHITE} and second {Fore.BLUE}'
    f'column{Fore.WHITE} is a {Fore.BLUE}\nnine{Fore.WHITE}, entering '
    f'{Fore.BLUE}7-3-5{Fore.WHITE} would add in the seventh {Fore.BLUE}row'
    f'{Fore.WHITE} and third {Fore.BLUE}column{Fore.WHITE} a {Fore.BLUE}five'
    f'{Fore.WHITE},\nwriting {Fore.BLUE}3 8 4{Fore.WHITE} would add in the '
    f'third {Fore.BLUE}row {Fore.WHITE} and eighth {Fore.BLUE}column'
    f'{Fore.WHITE} a {Fore.BLUE}four{Fore.WHITE}, and adding{Fore.BLUE}\n872'
    f'{Fore.WHITE} would add in the eighth {Fore.BLUE}row {Fore.WHITE} and the'
    f' seventh {Fore.BLUE}column{Fore.WHITE} a {Fore.BLUE}two{Fore.WHITE}.'
    f'\nOnce you write all the numbers given by you by the game, write '
    f'{Fore.BLUE}solve{Fore.WHITE} to get the solution to the puzzle.')


EXAMPLE_BOARD = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 4, 0],
  [0, 9, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 5, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


APP_TEXT2 = (
    f'If you made a {Fore.RED}mistake{Fore.WHITE}, and you misplaced a given '
    'number you can always replace\nthat position with an unknown number by '
    f'entering {Fore.BLUE}0{Fore.WHITE} in the {Fore.BLUE}third{Fore.WHITE} '
    f'value: Entering {Fore.BLUE}7,3,0{Fore.WHITE}, {Fore.BLUE}7-3-0'
    f'{Fore.WHITE}, {Fore.BLUE}7 3 0{Fore.WHITE} or {Fore.BLUE}730{Fore.WHITE}'
    f' would make again the seventh {Fore.BLUE}row{Fore.WHITE} and third '
    f'{Fore.BLUE}column {Fore.WHITE}an unknown number.\nYou can also write '
    f'{Fore.BLUE}reset{Fore.WHITE} to delete all values on the puzzle, '
    'starting all over\nagain.\n\n')

START_APP_TEXT = (
    'Write all your given numbers using one of the following parameters: '
    f'{Fore.BLUE}2,9,4{Fore.WHITE},\n{Fore.BLUE}2-9-4{Fore.WHITE},{Fore.BLUE}'
    f' 2 9 4{Fore.WHITE} or {Fore.BLUE}294{Fore.WHITE}. Remember the first '
    f'number represents the {Fore.BLUE} row {Fore.WHITE}, the second the '
    f'{Fore.BLUE}column{Fore.WHITE} and the third the {Fore.BLUE}given number'
    f'{Fore.WHITE}.\nAlso remember the number{Fore.BLUE} 0{Fore.WHITE} '
    'represents an unknown number.\nYour puzzle so far:')

VALID_FORMAT = (
  f'\nRemember all your given values must be entered all together{Fore.BLUE} '
  f'without spaces{Fore.WHITE} or\nseparated by either {Fore.BLUE}commas'
  f'{Fore.WHITE}, {Fore.BLUE}hyphens{Fore.WHITE} or {Fore.BLUE}spaces'
  f'{Fore.WHITE}.\nThe {Fore.BLUE}first{Fore.WHITE} number represents the '
  f'{Fore.BLUE}row{Fore.WHITE}, the {Fore.BLUE}second{Fore.WHITE} the '
  f'{Fore.BLUE}column{Fore.WHITE} and the {Fore.BLUE}third{Fore.WHITE} the '
  f'{Fore.BLUE}\nvalue{Fore.WHITE} ({Fore.BLUE}zero{Fore.WHITE} being an '
  f'{Fore.BLUE}unknown number{Fore.WHITE}) e.g.:\n{Fore.BLUE}4 8 2'
  f'{Fore.WHITE}, {Fore.BLUE}4-8-2{Fore.WHITE}, {Fore.BLUE}4,8,2{Fore.WHITE} '
  f'or {Fore.BLUE}482{Fore.WHITE} would be equal to add in the {Fore.BLUE}'
  f'fourth row{Fore.WHITE} and{Fore.BLUE} eighth\ncolumn {Fore.WHITE}a '
  f'{Fore.BLUE}2{Fore.WHITE}.\n')
