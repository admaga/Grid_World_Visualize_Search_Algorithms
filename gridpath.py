
from queue import PriorityQueue

START_CHARACTER = 8
END_CHARACTER = 9
OBSTACLE_CHARACTER = 1
NON_OBSTACLE_CHARACTER = 0

class World(object):
    def __init__(self, world, start, end):
        self.world = world
        self.rows = len(world)
        self.cols = len(world[0])

        self.start = start
        self.world[start[0]][start[1]] = START_CHARACTER

        self.end = end
        self.world[end[0]][end[1]] = END_CHARACTER
     
    def getNeighbors(self, cell):
        currentRow, currentColumn = cell
        directions = [(-1,0), (1,0), (0,1), (0,-1)]    # Possible direction of agent: up, down, right, left
        for rowIncrement, columnIncrement in directions:
            futureCellRow, futureCellColumn = currentRow + rowIncrement, currentColumn + columnIncrement
            if ((futureCellRow < 0 or futureCellRow >= self.rows or futureCellColumn < 0 or futureCellColumn >= self.cols) 
            or self.world[futureCellRow][futureCellColumn] == OBSTACLE_CHARACTER):
                continue
            yield (futureCellRow, futureCellColumn)
    
    def reachedGoal(self, cell):
        return self.world[cell[0]][cell[1]] == 9

    def backtrack(self, cell, movements):
        path = []
        while cell != self.start:
            path.append(cell)
            cell = movements[cell]
        path.reverse()
        return path[:-1]

    def g(self):
        # Cost of one step is 1, no diagonal movement
        return 1

    def h(self, cell):
        # Heuristic of Manhattan's distance
        return abs(cell[0] - self.end[0]) + abs(cell[1] - self.end[1])
        
    def breadthFirstSearch(self):
        frontier = []
        frontier.append(self.start)
        movements = {}
        movements[self.start] = None
        while (len(frontier) != 0):
            currentCell = frontier.pop()
            if self.reachedGoal(currentCell):
                return self.backtrack(currentCell, movements)
            for neighbor in self.getNeighbors(currentCell):
                if neighbor not in movements:
                    movements[neighbor] = currentCell
                    frontier.append(neighbor)
    
    def uniformCostSearch(self):
        frontier = PriorityQueue()
        frontier.put((0, self.start))    # Priority by g(n)
        movements = {}
        movements[self.start] = None
        cellCost = {}    # Cost tracker, cost of reaching this cell
        cellCost[self.start] = 0
        while (not frontier.empty()):
            frontierCell = frontier.get()
            currentCell = frontierCell[1]
            if self.reachedGoal(currentCell):
                return self.backtrack(currentCell, movements)
            for neighbor in self.getNeighbors(currentCell):
                g = cellCost[currentCell] + self.g()
                if neighbor not in movements or g < cellCost[neighbor]:    # Expand the neighbor with lowest path cost
                    movements[neighbor] = currentCell
                    frontier.put((g, neighbor))
                    cellCost[neighbor] = g
    
    def greedyBestFirstSearch(self):
        frontier = PriorityQueue()
        frontier.put((0, self.start))    # Priority by h(n)
        movements = {}
        movements[self.start] = None
        while (not frontier.empty()):
            frontierCell = frontier.get()
            currentCell = frontierCell[1]
            if self.reachedGoal(currentCell):
                return self.backtrack(currentCell, movements)
            for neighbor in self.getNeighbors(currentCell):
                if neighbor not in movements:
                    movements[neighbor] = currentCell
                    frontier.put((self.h(currentCell), neighbor))
    
    def aStarSearch(self):
        frontier = PriorityQueue()
        frontier.put((0, self.start))    # Priority by f(n) = g(n) + h(n)
        movements = {}
        movements[self.start] = None
        cellCost = {}    # Cost tracker, cost of reaching this cell
        cellCost[self.start] = 0
        while (not frontier.empty()):
            frontierCell = frontier.get()
            currentCell = frontierCell[1]
            if self.reachedGoal(currentCell):
                return self.backtrack(currentCell, movements)
            for neighbor in self.getNeighbors(currentCell):
                g = cellCost[currentCell] + self.g()
                if neighbor not in movements or g < cellCost[neighbor]:
                    movements[neighbor] = currentCell
                    f = g + self.h(currentCell)
                    frontier.put((f, neighbor))
                    cellCost[neighbor] = g
                
    def printWorld(self):
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.world[x][y], end="")
            print()
        print()
