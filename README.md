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