from gridpath import END_CHARACTER, NON_OBSTACLE_CHARACTER, START_CHARACTER, OBSTACLE_CHARACTER
from tkinter import messagebox
import gridpath
import tkinter as tk
import copy
import random

NUM_COLS = 20
NUM_ROWS = 20
START_POSITION = (0,0)
END_POSITION = (NUM_COLS - 1, NUM_ROWS  -1)

# Create grid data structure
gridButtons = [[0 for i in range(NUM_COLS)] for j in range(NUM_ROWS)]

# Create the world object
myWorld = gridpath.World(copy.deepcopy(gridButtons), START_POSITION, END_POSITION)
myWorld.printWorld()

# Functions of buttons pressed
def paintCell(cell):
    gridButtons[cell[0]][cell[1]]["bg"] = "yellow"

# Paint the world with the search path
def paintSearchAgorithm(pathList):
    if not pathList:
        messagebox.showinfo(message="No solution with current obstacles.", title="Alert")
        return
    clearPathButtonPressed()
    for cell in pathList:
        paintCell(cell)

def breadthFirstSearchButtonPressed():
    paintSearchAgorithm(myWorld.breadthFirstSearch())

def uniformCostSearchButtonPressed():
    paintSearchAgorithm(myWorld.uniformCostSearch())

def greedySearchButtonPressed():
    paintSearchAgorithm(myWorld.greedyBestFirstSearch())

def aStarButtonPressed():
    paintSearchAgorithm(myWorld.aStarSearch())

def resetWorldButtonPressed():
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            # If cell is START or END
            if i == START_POSITION[0] and j == START_POSITION[1]:
                bgColor = "red"
                myWorld.world[i][j] = START_CHARACTER
                myWorld.start = START_POSITION
            elif i == END_POSITION[0] and j == END_POSITION[1]:
                bgColor = "blue"
                myWorld.world[i][j] = END_CHARACTER
                myWorld.end = END_POSITION
            else:
                bgColor = "white"
                myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
            # Change background color
            gridButtons[i][j]["bg"] = bgColor

def clearPathButtonPressed():
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            currentBG = gridButtons[i][j]["bg"]
            if currentBG == "black":
                continue
            bgColor = "white"
            # If cell is START or END
            if i == myWorld.start[0] and j == myWorld.start[1]:
                bgColor = "red"
            if i == myWorld.end[0] and j == myWorld.end[1]:
                bgColor = "blue"
            gridButtons[i][j]["bg"] = bgColor

def randomizeObstaclesButtonPressed():
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            # Dont change START and END
            if (i == myWorld.start[0] and j == myWorld.start[1]) or (i == myWorld.end[0] and j == myWorld.end[1]):
                continue

            currentBG = gridButtons[i][j]["bg"]
            # Reset the path cell
            if currentBG == "yellow":
                gridButtons[i][j]["bg"] = "white"
                myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
                continue
            
            # Randomly toggle the obstacle 
            if random.randint(0,5) == 1:
                if currentBG == "black":
                    gridButtons[i][j]["bg"] = "white"
                    myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
                else:
                    gridButtons[i][j]["bg"] = "black"
                    myWorld.world[i][j] = OBSTACLE_CHARACTER

# Create main window
mainWindow = tk.Tk()
mainWindow.title("GRID WORLD SEARCH ALGORITHMS")

# Frame for search buttons
frameButtons = tk.Frame(mainWindow,relief=tk.RAISED, bd=2)
breadthFirstSearchButton = tk.Button(frameButtons, text="Breadth First Search", command=lambda:breadthFirstSearchButtonPressed())
uniformCostSearchButton = tk.Button(frameButtons, text="Uniform Cost Search", command=lambda:uniformCostSearchButtonPressed())
greedySearchButton = tk.Button(frameButtons, text="Greedy Cost Search", command=lambda:greedySearchButtonPressed())
aStartButton = tk.Button(frameButtons, text="A*", command=lambda:aStarButtonPressed())
randomizeObstaclesButton = tk.Button(frameButtons, text="Randomize Obstacles", command=lambda:randomizeObstaclesButtonPressed())
clearPathButton = tk.Button(frameButtons, text="Clear Path", command=lambda:clearPathButtonPressed())
resetWorldButton = tk.Button(frameButtons, text="Reset World", command=lambda:resetWorldButtonPressed())

# Set the position of the buttons
breadthFirstSearchButton.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
uniformCostSearchButton.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
greedySearchButton.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
aStartButton.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
randomizeObstaclesButton.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
clearPathButton.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
resetWorldButton.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
frameButtons.grid(row=0, column=0, sticky="ns")

# Create world frame
frameWorld=tk.Frame(mainWindow)
frameWorld.grid(row=0, column=1, sticky="nsew")

# Function when a button is pressed
def buttonPressed(i, j):
    currentBG = gridButtons[i][j]["bg"]
    if myWorld.start == None:
        # Set this button to be the START and update world
        newBG = "red"
        myWorld.start = (i, j)
        myWorld.world[i][j] = START_CHARACTER
    elif myWorld.end == None:
        # Set this button to be the END and update world
        newBG = "blue"
        myWorld.end = (i, j)
        myWorld.world[i][j] = END_CHARACTER
    elif currentBG == "white":
        # Toggle background color
        newBG = "black"
        myWorld.world[i][j] = OBSTACLE_CHARACTER
    elif currentBG == "black":
        # Toggle background color
        newBG = "white"
        myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
    elif currentBG == "red":
        # Flag the red button and reset current to white
        newBG = "white"
        myWorld.start = None
        myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
    elif currentBG == "blue":
        # Flag the blue button and reset current to white
        newBG = "white"
        myWorld.end = None
        myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
    else:
        # Toggle background color for other cases
        newBG = "black"
        myWorld.world[i][j] = OBSTACLE_CHARACTER
    # Change the background color
    gridButtons[i][j]["bg"] = newBG

# Create all the button objects and save them in data structure
for i in range(NUM_COLS):
    for j in range(NUM_ROWS):
        bgColor = "white"
        # If cell is START or END
        if i == START_POSITION[0] and j == START_POSITION[1]:
            bgColor = "red"
        if i == END_POSITION[0] and j == END_POSITION[1]:
            bgColor = "blue"
        currentButton = tk.Button(frameWorld,
            text="",
            fg="red",
            bg=bgColor, 
            width=1, 
            height=1,
            command=lambda i=i,j=j:buttonPressed(i,j))
        currentButton.grid(row=i+1, column=j+1)
        gridButtons[i][j] = currentButton
        
# Run GUI
mainWindow.mainloop()