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

APP_TEXT = """
 _____ _   _  _____    ___  ____________ 
|_   _| | | ||  ___|  / _ \ | ___ \ ___ |
  | | | |_| || |__   / /_\ \| |_/ / |_/ /
  | | |  _  ||  __|  |  _  ||  __/|  __/ 
  | | | | | || |___  | | | || |   | |    
  \_/ \_| |_/\____/  \_| |_/\_|   \_|   

To use the App is pretty simple. Once in the Main Menu write "Start", this
will show you a 9x9 grid all completed by zeros, this number represents an
unknown number. Use the guiding numbers colored in blue to locate a square
where you have a number that was given by you in the game and insert it.
The way you do this is by entering 3 numbers separated by a comma, a
hyphen, or a space. The first one being the row position, the second being
the column position and the third one the value.
This means that "4,2,9" would be that in the fourth row and second column
is a nine, entering "7-3-5" would add in the seventh row and third column
a five, and writing "3 8 4" would add in the third row and eighth column
a four.
Once you write all the numbers given by you by the game, write solve to
get the solution to the puzzle.
"""


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


APP_TEXT2 = """
If you made a mistake, and you misplaced a given number you can always replace
that position with an unknown number by entering 0 in the third value:
Entering "7,3,0", "7-3-0" or "7 3 0" would make again the seventh row and
third column an unknown number.
You can also write "Reset" to delete all values on the puzzle, starting all
over again.
"""
