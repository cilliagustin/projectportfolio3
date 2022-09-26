# Sudoku Solver
The Sudoku Solver is an interactive application run through the Heroku terminal. Using this, the user is able to get the solution to any sudoku puzzle.

Although Sudoku is a game mainly played by adults, anyone can run this program in order to get the solution or just check if they correctly completed the puzzle.

The app can be intuitively run. From the main menu the user can either go to the information menu, here they will find out more about how to run the app and also about the history and rules of the sudoku. From the main menu they can also go to the screen where they can fill the puzzle with all the given numbers and get the solution.

[Link to the live site](https://sudoku-solver-agustin-cilli.herokuapp.com/)
    
    Add image of main menu

## UX
The app runs in the Heroku terminal and consists of three menus:
* Main menu: The landing page and where the user can go to the other two menus.
* Information menu: Here the user can either get more information on the game (history and rules of the sudoku) or get more information on the app (How to enter a puzzle and get the correct solution).
* Solving menu: This is where the user enters the puzzle and gets the solution.

Although running the app on a terminal has certain limitations regarding the user experience, colors (imported via colorama), titles created with ascii code, and effects were used to engage the user and catch their attention.
### User Stories
* As a user, I want to intuitively navigate through the application.
* As a user, I want to understand the value the application gives me.
* As a user, I want to be explained how to use the application.
* As a user, I want to get information about the game Sudoku.
* As a user, I want to be able to exit the application at any step.
* As a user, I want to be able to correct the puzzle in case I made a miskate.
* As a user, I want to be able to restart the whole puzzle if I made a lot of mistakes.
* As a user, I want to be able to enter the sudoku using more than just one format.
* As a user, I want to have the numbers I enter easily differentiated from the others.
* As a user, I want to get the solution to the Sudoku puzzle.

### Colour Scheme and Typography
The colorama module was imported in order to be able to add colors to the app. These are used throughout the different parts of the website to enphasyse different things.
In the information menu, the color blue was used throughout the "App explanation" to emphasize how the numbers must be formatted in order to be accepted as valid.
When printing the puzzle with the style board function (more information about all functions will be given later on), the color red is used to express an unknown number in the puzzle (a zero), green is used for all the given (known) numbers, and cyan is used to show all the guide numbers on the top and the right side of the puzzle (used to orient the user to where the numbers should be entered).
In the app, many inputs are printed where they ask the user to enter a specific command. In these cases, the blue color is often used to highlight which commands are valid.
If the user enters an invalid command, the wrong input function will be triggered. This will display an error message using the colors red and yellow to indicate the invalid input.

    Add color images

The only customisation used for the typography in the app were the titles created with ascii code. The titles "Sudoku Solver", "Information", "The Game" and "The App" were created to attract the attention of the user when going through a specific part of the app.

    Add title images

### Wireframes
     include screenshots of your wireframes (consider the markdown table format)
## Features
    briefly explain the project
### Existing Features
    list out all of your project's features, and make sure to include a screenshot of each!!
### Features Left to Implement
    have ideas on what you'd like to add in the future? add them here!! assessors LOVE seeing future concepts!
## Technologies Used
    explain various tech used, such as HTML, CSS, Gitpod, GitHub, Git, etc. - add a link to each respective site as well, if possible
## Testing
    "For all testing, please refer to the [TESTING.md](TESTING.md) file."
## Deployment
    document all necessary steps you did in order to deploy this project (GitHub Pages, Heroku, etc.)
### Local Deployment
    document all the necessary steps someone else can take in order to make a local copy of your project, like cloning, forking, etc.
## Credits
    explain about any particular places you took inspiration from
### Content
    list out any URLs or links where you might've borrowed a snippet of code, or element
### Media
    list out any URLs for images/videos/audios you've borrowed from online (Markdown Table works best here!)
### Acknowledgements
    list out any acknowledgements you have, if any... tutor support? fellow Slack student help? spouse, loved one, family member, etc.
​