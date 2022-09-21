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

INFORMATION_TEXT = """
 _____ _   _ ______ ______________  ___  ___ _____ _____ _____ _   _ 
|_   _| \ | ||  ___|  _  | ___ \  \/  | / _ \_   _|_   _|  _  | \ | |
  | | |  \| || |_  | | | | |_/ / .  . |/ /_\ \| |   | | | | | |  \| |
  | | | . ` ||  _| | | | |    /| |\/| ||  _  || |   | | | | | | . ` |
 _| |_| |\  || |   \ \_/ / |\ \| |  | || | | || |  _| |_\ \_/ / |\  |
 \___/\_| \_/\_|    \___/\_| \_\_|  |_/\_| |_/\_/  \___/ \___/\_| \_/

Do you wish to know more about the game Sudoku? Do you want to know how to use
correctly the App?
"""

GAME_TEXT = """
 _____ _   _  _____   _____   ___  ___  ___ _____ 
|_   _| | | ||  ___| |  __ \ / _ \ |  \/  ||  ___|
  | | | |_| || |__   | |  \// /_\ \| .  . || |__  
  | | |  _  ||  __|  | | __ |  _  || |\/| ||  __| 
  | | | | | || |___  | |_\ \| | | || |  | || |___ 
  \_/ \_| |_/\____/   \____/\_| |_/\_|  |_/\____/ 

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
|_   _| | | ||  ___|  / _ \ | ___ \ ___ |
  | | | |_| || |__   / /_\ \| |_/ / |_/ /
  | | |  _  ||  __|  |  _  ||  __/|  __/ 
  | | | | | || |___  | | | || |   | |    
  \_/ \_| |_/\____/  \_| |_/\_|   \_|   
"""

APP_TEXT = (
    'To use the App is pretty simple. Once in the Main Menu write '
    f'{Fore.BLUE}start{Fore.WHITE}, this will show you a 9x9 grid all '
    'completed by zeros, this number represents an unknown number. Use the  '
    f'guiding numbers colored in {Fore.BLUE}blue{Fore.WHITE} to locate a '
    'square where you have a number that was given by you in the game and '
    f'insert it. The way you do this is by entering 3 numbers separated by a '
    f'{Fore.BLUE}comma{Fore.WHITE}, a {Fore.BLUE}hyphen{Fore.WHITE}, or a '
    f'{Fore.BLUE}space{Fore.WHITE}. The first one being the {Fore.BLUE}row '
    f'{Fore.WHITE}position, the second being the {Fore.BLUE}column '
    f'{Fore.WHITE}position and the third one the {Fore.BLUE}value{Fore.WHITE}.'
    f'\nThis means that {Fore.BLUE}4,2,9{Fore.WHITE} would be that in the '
    f'fourth{Fore.BLUE} row{Fore.WHITE} and second {Fore.BLUE}column'
    f'{Fore.WHITE} is a {Fore.BLUE}nine{Fore.WHITE}, entering {Fore.BLUE}7-3-5'
    f'{Fore.WHITE} would add in the seventh {Fore.BLUE}row{Fore.WHITE} and '
    f'third {Fore.BLUE}column{Fore.WHITE} a {Fore.BLUE}five{Fore.WHITE}, and '
    f'writing {Fore.BLUE}3 8 4{Fore.WHITE} would add in the third {Fore.BLUE}'
    f'row {Fore.WHITE} and eighth {Fore.BLUE}column{Fore.WHITE} a {Fore.BLUE}'
    f'four {Fore.WHITE}Once you write all the numbers given by you by the game'
    f', write {Fore.BLUE}solve{Fore.WHITE} to get the solution to the puzzle.')


EXAMPLE_BOARD = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 4, 0],
  [0, 9, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 5, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


APP_TEXT2 = (
    f'If you made a {Fore.RED}mistake{Fore.WHITE}, and you misplaced a given '
    'number you can always replace that position with an unknown number by '
    f'entering {Fore.BLUE}0{Fore.WHITE} in the {Fore.BLUE}third{Fore.WHITE} '
    f'value: Entering {Fore.BLUE}7,3,0{Fore.WHITE}, {Fore.BLUE}7-3-0'
    f'{Fore.WHITE} or {Fore.BLUE}7 3 0{Fore.WHITE} would make again the '
    f'seventh {Fore.BLUE}row{Fore.WHITE} and third {Fore.BLUE}column '
    f'{Fore.WHITE}an unknown number.\n You can also write {Fore.BLUE}reset'
    f'{Fore.WHITE} to delete all values on the puzzle, starting all over '
    'again.')

START_APP_TEXT = (
    'Write all your given numbers using one of the following paramethers: ba'
    f'{Fore.BLUE}2,9,4{Fore.WHITE}, {Fore.BLUE}2-9-4{Fore.WHITE} or{Fore.BLUE}'
    f' 2 9 4{Fore.WHITE}. Remember the first number represents the {Fore.BLUE}'
    f'row {Fore.WHITE}, the second the {Fore.BLUE}column{Fore.WHITE} and the '
    f'third the {Fore.BLUE}given number{Fore.WHITE}.\nAlso remember the number'
    f'{Fore.BLUE} 0{Fore.WHITE} represents an unknown number.\n Your puzzle so'
    ' far:')
