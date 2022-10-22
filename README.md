# _Search Algorithm Visualizer_
#### Find shortest path in a grid world with different search algorithms.

Have fun visualizing various search algorithms such as Breadth First Search, Uniform Cost Search, Greedy Best First Search and A* in a grid placing the initial and goal destinations as well as obstacles through the world. The shortest path found by the selected algorithm will be marked in the grid. 

## Motivation
Part of an online assessment for a software development position was to program the shortest path given an agent and a goal state with obstacles. After having a hard time programming the code, this project is a redemption to the unacheived opportunity.

## Tech Used
-[Python 3.9](https://www.python.org/download/releases/3.0/)

-[Tkinter](https://docs.python.org/3/library/tkinter.html) for GUI


## Project Explanation

The program will create a world of 20x20 buttons. Red button is initial state, blue button is goal state and black buttons are obstacles. After selecting an algorithm, if a path is found, it will be highlighted yellow in the world in order to visualize it. The initial and goal states can be moved around the world. The application allows to place obstacles around the grid on demand by clicking non-terminal states or also you can choose to automatically place obstacles in random locations.

![Image text](https://github.com/admaga/Search_Algorithm_Visualizer/blob/93f1f08624f6d3aee100e4cccb11a6917e54cb8a/img/pathfinder.jpg)

## Usage
Run ``gridpath_gui.py`` to start the GUI

![Image text](https://github.com/admaga/Search_Algorithm_Visualizer/blob/7061af9cd079c8759de787caadab21b86b07c782/img/Mainscreen.jpg)

Select the initial state, click on randomize obstacles and select the algorithm you want to visualize!

![Image text](https://github.com/admaga/Search_Algorithm_Visualizer/blob/93f1f08624f6d3aee100e4cccb11a6917e54cb8a/img/astargif.gif)

## License
MIT
