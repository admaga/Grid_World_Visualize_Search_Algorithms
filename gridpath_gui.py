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

gridButtons = [[0 for i in range(NUM_COLS)] for j in range(NUM_ROWS)]
myWorld = gridpath.World(copy.deepcopy(gridButtons), START_POSITION, END_POSITION)

def paintCell(cell):
    gridButtons[cell[0]][cell[1]]["bg"] = "yellow"

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
            if (i,j) == START_POSITION:
                bgColor = "red"
                myWorld.world[i][j] = START_CHARACTER
                myWorld.start = START_POSITION
            elif (i,j) == END_POSITION:
                bgColor = "blue"
                myWorld.world[i][j] = END_CHARACTER
                myWorld.end = END_POSITION
            else:
                bgColor = "white"
                myWorld.world[i][j] = NON_OBSTACLE_CHARACTER

            gridButtons[i][j]["bg"] = bgColor

def clearPathButtonPressed():
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            currentBG = gridButtons[i][j]["bg"]
            if currentBG == "black":
                continue
            bgColor = "white"
            if (i,j) == myWorld.start:
                bgColor = "red"
            if (i,j) == myWorld.end:
                bgColor = "blue"
            gridButtons[i][j]["bg"] = bgColor

def randomizeObstaclesButtonPressed():
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if ((i,j) == myWorld.start) or ((i,j) == myWorld.end):
                continue
            currentBG = gridButtons[i][j]["bg"]
            if currentBG == "yellow":
                gridButtons[i][j]["bg"] = "white"
                myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
                continue
            if random.randint(0,5) == 1:    # Randomly toggle the obstacle 
                if currentBG == "black":
                    gridButtons[i][j]["bg"] = "white"
                    myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
                else:
                    gridButtons[i][j]["bg"] = "black"
                    myWorld.world[i][j] = OBSTACLE_CHARACTER

# Create main window
mainWindow = tk.Tk()
mainWindow.title("GRID WORLD SEARCH ALGORITHMS")

# Set frame for buttons
frameButtons = tk.Frame(mainWindow,relief=tk.RAISED, bd=2)
breadthFirstSearchButton = tk.Button(frameButtons, text="Breadth First Search", command=lambda:breadthFirstSearchButtonPressed())
uniformCostSearchButton = tk.Button(frameButtons, text="Uniform Cost Search", command=lambda:uniformCostSearchButtonPressed())
greedySearchButton = tk.Button(frameButtons, text="Greedy Cost Search", command=lambda:greedySearchButtonPressed())
aStartButton = tk.Button(frameButtons, text="A*", command=lambda:aStarButtonPressed())
randomizeObstaclesButton = tk.Button(frameButtons, text="Randomize Obstacles", command=lambda:randomizeObstaclesButtonPressed())
clearPathButton = tk.Button(frameButtons, text="Clear Path", command=lambda:clearPathButtonPressed())
resetWorldButton = tk.Button(frameButtons, text="Reset World", command=lambda:resetWorldButtonPressed())

# Set position of the buttons
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

def buttonPressed(i, j):
    currentBG = gridButtons[i][j]["bg"]
    if myWorld.start == None:
        newBG = "red"
        myWorld.start = (i, j)
        myWorld.world[i][j] = START_CHARACTER
    elif myWorld.end == None:
        newBG = "blue"
        myWorld.end = (i, j)
        myWorld.world[i][j] = END_CHARACTER
    elif currentBG == "white":
        newBG = "black"
        myWorld.world[i][j] = OBSTACLE_CHARACTER
    elif currentBG == "black":
        newBG = "white"
        myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
    elif currentBG == "red":
        newBG = "white"
        myWorld.start = None
        myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
    elif currentBG == "blue":
        newBG = "white"
        myWorld.end = None
        myWorld.world[i][j] = NON_OBSTACLE_CHARACTER
    else:
        newBG = "black"
        myWorld.world[i][j] = OBSTACLE_CHARACTER

    gridButtons[i][j]["bg"] = newBG

# Create button objects
for i in range(NUM_COLS):
    for j in range(NUM_ROWS):
        bgColor = "white"
        if (i,j) == START_POSITION:
            bgColor = "red"
        if (i,j) == END_POSITION:
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