# Hit-Me-Baby-One-More-Time
A Battleship inspired text based game created for the third project of Code Institute Fullstack developer program

### Visit the deployed website: ********************************

## CONTENTS

* [Happy Path Through Game](#happy-path-through-game)

* [User Stories](#user-stories)
   * [MVP](#mvp)
   * [Add-ons](#add-ons)

* [Design](#design)
  * [Flowchart](#flowchart)
  * [Features](#features)

* [Technologies Used](#technologies-used)
  * [Language Used](#language-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Iteration over starting code](#iteration-over-starting-code)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)
* [Bug Fixes](#bug-fixes)
  
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Acknowledgments](#acknowledgments)

- - -

## Happy Path Through Game
For testing purposes, one of the paths for succeeding is simply by inputting 1 for each option. To get to the unsuccessful ending, input 1, 1, 2 in that order.

# User Stories
MVP
The users should be able to:

## Start the game when typing "Start".
Not have to worry about capitalizing or lowercase when typing.
Receive the next part in the story depending on the input choices.
Reach the end of the game through one of the paths chosen, by either succeeding or failing in the quest.
## Add-ons
After the essentials are covered I would like the user to be able to:

Have more options/alternate endings to the game.
Have in-game items to interact with.
Print out the choices made onto a Google doc/sheet so that the user can see their choices of play.
Enjoy a more visually exciting experience by adding some styling and images. 
## Design
The design is structural in nature as opposed to visual, as although I know the Python terminal can be styled, the time I have to implement this project requires full focus on the functionality only.

## Flowchart
Since the game changes depending on the users' choices, I wanted to lay out the step-by-step logic needed to reach each ending of the game. Although there are only two outcomes there are multiple ways to get there.

## Input/step check

For each step, the user receives a prompt, writes their input, and the input is cross-checked against the code for validation. If the user input is invalid, they are prompted again to input on the same step. Once valid input is received, the user goes on to the next step.

The flow of the game has 8 possible outcomes, 4 successful adventures, and 4 unsuccessful. Below is a basic map of the journey which can be followed to see all alternatives and their outcomes. A link to the Lucidchart can be found here The screenshot is below:

****** SCREENSHOT **********

# pp3_game_step_flow_3

## Features
The user can add a name of their choosing to give them a personalised welcome to the game:

********* game screenshot ********************

The user is then taken through a journey with explanation texts and requests for the user to choose which path they want to take. Choosing different paths can lead to different outcomes.

## game choices
******** screenshot **********
At the end of the user's journey, they are presented with a final text depending on their success or not in catching the required object to "win".

At the end of the game, the users are offered to run through the game from the start if they choose.

## Not succeeding:

game not successful

## Succeeding:

game successful

# Technologies Used
Language Used
Python

# Frameworks, Libraries & Programs Used
Github - For online storage of code and deployment.

Picresize - Used to resize images for Readme/Testing docs.

Gitpod - For writing my code.

******* Heroku - For deploying my program.


# Iteration over starting code
Being fairly new to coding I have my two previous projects from Code Insitute, one HTML CSS and one HTML, CSS and JavaScript to reference from. Now this project is entirely different allthough has the same structure. So I applied the same structure in the READme, based on those two. 

## Here is the commit from my trialling of the function:



This process of iteration worked best for my brain to see what steps I need to take and solidify my understanding of not passing immutable data.

# Deployment & Local Development
## Deployment
This project was deployed at Heroku

The numbers on the screenshots represent the numbers on the steps of my deployment process.

To deploy this project after creating my account, I:

Went to my dashboard and clicked on the New App dropdown menu
Clicked Create new app from the options
heroku_deployment_step_1-2

Named my app in the App name box
Chose a region from the dropdown menu (and accidentally chose the United States for this one)
Clicked Create app
heroku_deployment_step_2-5

Once the app was made I went to my dashboard where I can see my apps.

Clicked on the relevant app
heroku_deployment_step_6

7-8. From here, I went to settings, then to the Config Vars. I added the PORT key and a value of 8000. This was a requirement by Code Institute to ensure there were no issues caused by not having it.

I then went to Buildpacks and added Python, and then NodeJS.
heroku_deployment_step_7-9

Then I clicked the Deploy tab. Here I connected my GitHub account with the repository the deployment is to select.
After that, I chose to manually deploy my project as needed, but it's possible to set up automatic deployments if preferred.
heroku_deployment_step_10-11

Local Development
How to Fork
Should you wish to fork this repo, here is a guide on how to do that:

Firstly, go to https://github.com/emmy-codes/cat-adventures-python

On the main repo page, click the Fork button near the top right corner
fork-cat-adventures

On the create a fork page, check the Owner of the repo is set to the GitHub org you wish to use, and change the name of the repo if you wish. 2a: Add a description if you want to
Check the box here if you want to make a copy of the main branch or multiple branches (main is selected by default)
Create the fork
Screenshot from an old project as I cannot fork my Python project due to not having any organizations connected to my account, and presumably because this repo is already a fork of the CI template
fork-screenshot

How to Clone
For cloning the repo you will need:

The repo open
Your IDE of choice
On the repo page, click on the green "Code" button
On the dropdown from the Code button, click on your chosen key (pictured here is SSH)
Click the copy button (shown as two squares on top of one another)
clone_step

Open your IDE of choice and open the Terminal, or in my case, open the Terminal on your computer (I run Linux on Windows so may be slightly different for Mac/Windows users)
Check that you're in the right folder (shown here by checking my current folder by using the input: ls
Change as needed to reach your desired folder.
Type (without quotation marks): "git clone" followed by your copied link from GitHub.
You can now access the repo in your IDE if cloned directly there, or by typing (without quotation marks) "code ." in your Terminal.
Have fun!
git_clone_pp3

Testing
Please refer to the TESTING.md file for all testing carried out.

Bug Fixes
The majority of the issues in my code have been due to my not completing the logic adequately. For example, when I created the start_game function I added the usual input requests and set an else to print an error message requesting the user input 1 or 2 to continue, but did not set the game to run again. I solved this by offering the input field again after printing a message to the user.

I had a huge challenge after adding user input to my game due to having a "game window" with a $ on char 79. I was trying to put together an if statement to cover all name-length eventualities without impacting the position of the final game window char. After many, many iterations my first breakthrough was getting the print to show the start of the game screen (game_screen_start) followed by the name that the user input.

error_solving_progress

The next iteration turned on its head: I was having too hard of a time removing spaces from the end of the string, so I decided to add space up to 77 characters and added the $ to the beginning and end.

I checked the length of the name input, the length of the game screen start text, and the length of the middle text. I then deducted that length from the allowed length of 77. Or so I thought. Upon printing the alignment was completely off and I had way more white space than intended. To find out what went wrong, I printed the "calculating" variable which was over 100! I then printed "len(name)+len(game_screen_start)+len(middle_text))" and it returned around 53. The issue was precedence . I had set the calculating variable to follow the code step by step, which was throwing the result off.

I solved the issue by adding extra parentheses around the calculation to gather the total length of characters to print, which could then be deducted from the allotted 77 characters.

error_solving_step_3

Credits
To my classmate Ben who shared his code for review on Slack, and upon reading it gave me the idea to use just number 1 or 2 as input to help simplify and speed up my MVP.

Code Used
ASCII art is taken from ASCII art but it's unclear who the actual owner is as it's displayed identically on multiple sites. I adjusted it to have two cats for the purpose of my story.

Content
I have used OpenAI to create most of the text for me so I can focus my time on practising with the code. "We" had a little chat and went over some iterations and I'm happy that it was able to work out the structure for continuing the game, and then I was able to build the flow chart and thus work on the code structure from there.

Acknowledgments
I would like to acknowledge the following people:

My partner for his extra help looking after our little one so I could focus on getting as much learning in as possible, and for providing his insight into logical thinking and good practices for breaking down a problem into manageable chunks. 🥰

Family and friends on Facebook for user testing my game and providing feedback!