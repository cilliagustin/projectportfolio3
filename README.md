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

### Structure
The app runs with a easy to follow structure. Most of the big texts are stored in the text.py file and the run.py contains allk the functions used. There are Three "Menu functions" The main menu function, the information menu function and the start app functions. The first one works as a "Main screen" that lets you access the other two functions, the second one displays necesray information to the user and the thirs is the one where the user adds the information to get the anser to the sudoku.
In any point of the app the user can exit the application by entering exit.

    Add structure diagram
## Features
This application has many features. A large number of these were implemented just to give the user a better experience while using a terminal-based application.

### Existing Features
#### Modules
Many modules had to be imported in order to add certain functionalities to the application.
* Os: is used to create a function that clears the terminal. This checks if the operating system is either Windows or Linux and triggers the necessary command to delete everything visible in the terminal screen.
* Sys: is used only in the typewriter function to print every character of the string individually.
* Time: this is also used in the typewriter function to create a delay between each character and also a delay after the function prints the whole message.
* Copy: in the solve sudoku function, a nested list has to be copied and modified without changing the original. In order to do this, this module had to be imported in order to be able to use deepcopy.
* Colorama: this module is used throughout the whole application. Every single input uses this to indicate what the user can enter. In functions like style board, many colors are used to indicate what they do. The wrong input function uses this to show the invalid input entered and many of the text impoorted also uses this in certain words.

#### Puzzle
A nested list represents the sudoku board. This list contains 9 lists each with 9 numbers, all zeroes when starting the app.

This list is modified by the user entering the values they know of the sudoku. The original values, zeroes, represent an unknown number and this will be replaced by the values that the user already have.

#### Titles
The application uses titles created in ASCII code in order to attract the attention of the user. The main title, "Sudoku Solver", is used in the main menu and when the user is entering the puzzle to be solved. The other titles are "Information", "The App", and "The Game", which are used in the information menu to indicate what information is being shown.
These titles were created using the ASCII text generator provided by [coolgenerator](https://www.coolgenerator.com/ascii-text-generator) and stored as variables in the text.py file in order to be called in the different functions of the run.py file.

#### Text.py
The file [text.py](text.py) is where most of the texts are stored. This was created in order to have a better and easier to understand structure for the application. Many of the texts here are f-strings because the colorama module was also used here. This was used to emphasize certain words when explaining how to use the application: which command starts the app and how to correctly introduce the numbers.

#### Main menu function
This function is the first triggered when the user opens the application. Since this is also triggered when going back from different sections of the application, the first thing to activate is the clear function (how this works will be explained later on). Once the screen is cleared, it prints the "Sudoku Solver" title and the "Main menu text", imported from the text.py file.

After printing this text, it prints an input asking the user what they want to do. They can either write "information" to go to the information menu, "start" to go to the section where they can enter a puzzle and get the solution, or "exit" to trigger the exit app function.

If the user enters an invalid input, it will trigger the wrong input function and ask again for an input.

#### Information menu function
When triggering this function, the first thing to do is clear the screen with the clear function. After that, it prints a text called "Information text" that contains the information title and a brief introductory text of what information the user can get here.

Following that, an input asks the user to select the information they want to get. If the user enters "game," a text with all the information regarding the history of the sudoku and how to play the game will be printed. If they write "app", a description of how to use the app will be printed. Here, colorama is used to highlight certain parts of the text, and the style board function is triggered using an example puzzle located in the text.py file to print a sudoku in order to show the user how the numbers are entered.

The user can also write back to send them back to the main menu or exit to trigger the exit app function. The wrong input function is triggered if the entered input is invalid.

#### Start app function
This function is triggered when the user enters "start" in the main menu function. The first thing to do is use a helper function called run app screen. After that, it prints an input where the user has a lot of options to enter. The first thing that happens with the input answer is a try/except block.

In the try block, a function called is number format valid checks if the number entered is in a valid format. If that is the case, it will get the row col and value from the answer with the get values function and will place those values in the puzzle using the code "puzzle[row][col] = value". After that, the run app screen is triggered again.

In the except block, it will validate the input answer if it is not a valid answer. If the input value is "reset", it will trigger the reset puzzle function that turns all the puzzle values into zeros. If the answer is "format", it will simply display a text explaining how to correctly format the numbers. If the input written is "solve", it will trigger the solve sudoku function that will try to get the correct answer (if there is one). Just like in the information menu function, if the input is "exit" the exit app function is triggered, and it will go back to the main menu if the input is "back" (this will maintain the entered values if the user goes back to the main menu and then writes "start" again).

The wrong input function is triggered if the entered input is invalid.

#### Clear function
The clear function is used thoughout the whole application to clear the screen. This uses the os imported module and checks if the operating system is Windows or Lynus and triggers the correct command.

#### Exit app function
This function can be triggered at any point in the application. In any input, the user can enter "exit" to activate this function. When this happens, it displays an inpout that asks the user to confirm they want to exit.

If they write "yes", a text (using the typewriter function) will inform the user that the app is closing and then the app is closed. In this case, the get salutations function is triggered to salute the user according to the time of the day.

On the other hand, if the user enters "no," a break will be executed and the user will be taken back to the previous input they were.

#### Wrong input function
This function is triggered whenever a user writes an invalid input. When this happens, this function will take that answer as a parameter and print: "Wrong command:" (in red using colorama), the wrong input (in yellow), and it will ask the user to enter a valid command.

#### Reset puzzle function
This function is activated not only when the user enters "rese"t on the start app function input, but also when the sudoku is solved (more on this later).

This function loops through all the puzzle and replaces every single value with a zero.

#### Style board function
This function takes a puzzle as a parameter and prints it in a way that it represents the puzzle in a more familiar way to the user.

Instead of representing the puzzle as a nested list, it will divide the rows and columns each 3  numbers to create a more understandable grid. It also prints some guide numbers (in cyan) so the user can see easily the row and column value for the number they have to enter and makes sure to print all zeroes in red and non-zero numbers in green so the user can easily differentiate between known and unknown numbers.

#### Typewriter function
This function takes a string as a parameter and prints it character by character so the user can read it as it is being written. This uses the modules "sys" and "time" to get each character at a time and prints them every 0.1 seconds. Once the message is printed, it has another delay of two seconds before continuing.

The function is used when closing the application and when solving the sudoku.

#### Get salutation function
This function is used when closing the application. Using the "datetime" module, it gets the hour that the user is using the app and returns a salutation according to the current hour.


### Features Left to Implement
    have ideas on what you'd like to add in the future? add them here!! assessors LOVE seeing future concepts!
## Technologies Used
    explain various tech used, such as HTML, CSS, Gitpod, GitHub, Git, etc. - add a link to each respective site as well, if possible
## Testing
For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment
Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser. This is to improve the accessibility of the project to others.

The live deployed application can be found [here](https://sudoku-solver-agustin-cilli.herokuapp.com/).

### Local Deployment

*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/cilliagustin/projectportfolio3.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/cilliagustin/projectportfolio3)

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select *Add Buildpack*.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

## Credits
    explain about any particular places you took inspiration from
### Content
    list out any URLs or links where you might've borrowed a snippet of code, or element
### Media
    list out any URLs for images/videos/audios you've borrowed from online (Markdown Table works best here!)
### Acknowledgements
    list out any acknowledgements you have, if any... tutor support? fellow Slack student help? spouse, loved one, family member, etc.
​