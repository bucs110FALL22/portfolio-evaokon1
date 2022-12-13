# CS110 Project Proposal
# Tic-Tac-Toe
## CS 110 Final Project
### << Fall, 2022 >>
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

[repl](https://replit.com/@ChristianPetrag/Final-Project-cs110)

[link to demo presentation slides](https://docs.google.com/presentation/d/1pEJ2ag2SkK9z5GAY4jk_BDEeS16grW8xDomgYbjS0do/edit)

Team: Christian and Eva

**Christian Petragnani and Eva Okon**
## Description of Project
A tic-tac-toe game. A main class that draws the board with 9 cells. When the user clicks the screeen, an X or O will appear in that cell. When a player has three in a row vertically, horizontally, or diagonally, they win.

# UI Design
Initial Concept
* A program that allows two players to play tic-tac-toe.

Final GUI
* Located in images folder

# Program Design
## Non-Standard Libraries Used
Pygame

## List of Classes
* Runner - Displays board on screen in folders
* Board - Checks events in the game and runs the game

## Project Structure and File List
The project is broken down into the following structure:
  * main.py
  * src
    * runner class
    * board class
  * assets
    * TTTBoard.png
    * X.png
    * O.png
    * Owins.png
    * Xwins.png
  * etc
    * README.md

# Tasks and Responsibilities
Eva Okon - Wrote the original code. Ran and tested it to be sure everything was working.

Christian Petragnani - Improvised the code into classes so that the code matched the rubric. Also desinged GUI pictures in a design software for gameplay.

# Testing
To test the code, we wrote a bit of code then ran it. We debugged errors and continued coding. To test the game, we made sure that two X's or O's couldn't be placed in the same cell. We then checked that the three combinations for winning worked.

# ATP
Step | Procedure | Expected Result
--- | --- | ---
1 | Run main.py | Board will appear on screen
2 | Click a cell on the screen | An "X" or "O" will appear in that cell
3 | Repeat step 2 until a player wins or there's a tie | A message will appear on screen saying which player won or there's a tie