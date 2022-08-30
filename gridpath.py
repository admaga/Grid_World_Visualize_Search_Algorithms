
from queue import PriorityQueue

START_CHARACTER = 8
END_CHARACTER = 9
OBSTACLE_CHARACTER = 1
NON_OBSTACLE_CHARACTER = 0

class World(object):
    def __init__(self, world, start, end):
        self.world = world
        self.start = start
        # Set the end character in the world
        self.world[start[0]][start[1]] = START_CHARACTER
        self.end = end
        # Set the end character in the world
        self.world[end[0]][end[1]] = END_CHARACTER
        self.rows = len(world)
        self.cols = len(world[0])
        self.painted = False
     
    def getNeighbors(self, current):
        currentRow, currentCol = current
        # Possible direction of agent: up, down, right, left
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        for direction in directions:
            # Apply movement to current position
            neighborRow, neighborCol = currentRow + direction[0], currentCol + direction[1]
            # If the neighbor is out of the world or if there is an obstacle
            if (neighborRow < 0 or neighborRow >= self.rows or neighborCol < 0 or neighborCol >= self.cols or self.world[neighborRow][neighborCol] == OBSTACLE_CHARACTER):
                continue
            yield (neighborRow, neighborCol)
    
    def reachedGoal(self, cell):
        return self.world[cell[0]][cell[1]] == 9

    def backtrack(self, current, movements):
        path = []
        while current != self.start:
            path.append(current)
            current = movements[current]
        path.reverse()
        return path[:-1]

    def g(self):
        # Cost of one step is 1, not diagonal movement
        return 1

    def h(self, currentCell):
        # Heuristic of manhattan distance on square grid
        return abs(currentCell[0] - self.end[0]) + abs(currentCell[1] - self.end[1])
        
    def breadthFirstSearch(self):
        # Create frontier
        frontier = []
        frontier.append(self.start)

        # Create path tracker
        movements = {}
        movements[self.start] = None
        
        while (len(frontier) != 0):
            currentCell = frontier.pop()

            if self.reachedGoal(currentCell):
                # Backtrack and print path
                return self.backtrack(currentCell, movements)

            # Iterate over each possible neighbor
            for neighbor in self.getNeighbors(currentCell):
                # Add the neighbor that we have not seen to the frontier
                if neighbor not in movements:
                    # Add breadcrumb in dictionary key:toCell value:fromCell
                    movements[neighbor] = currentCell
                    frontier.append(neighbor)
    
    def uniformCostSearch(self):
        # Create frontier
        frontier = PriorityQueue()
        # Priority by g(n)
        frontier.put((0, self.start))

        # Create path tracker, KEY=toCell VALUE=fromCell
        movements = {}
        movements[self.start] = None

        # Create cost tracker, KEY=celL VALUE=cost of reaching this cell
        cellCost = {}
        cellCost[self.start] = 0
        
        while (not frontier.empty()):
            frontierCell = frontier.get()
            currentCell = frontierCell[1]
            
            if self.reachedGoal(currentCell):
                # Backtrack and print path
                return self.backtrack(currentCell, movements)

            # Iterate over each possible neighbor
            for neighbor in self.getNeighbors(currentCell):
                # Calculate the cost of move
                g = cellCost[currentCell] + self.g()
                # Expand the node with lowest path cost
                if neighbor not in movements or g < cellCost[neighbor]:
                    # Add breadcrumb in dictionary
                    movements[neighbor] = currentCell
                    # Add the neighbor to sort by cost
                    frontier.put((g, neighbor))
                    cellCost[neighbor] = g
    
    def greedyBestFirstSearch(self):
        # Create frontier
        frontier = PriorityQueue()
        # Priority by h(n)
        frontier.put((0, self.start))

        # Create path tracker, KEY=toCell VALUE=fromCell
        movements = {}
        movements[self.start] = None
        
        while (not frontier.empty()):
            frontierCell = frontier.get()
            currentCell = frontierCell[1]
            
            if self.reachedGoal(currentCell):
                # Backtrack and print path
                return self.backtrack(currentCell, movements)

            # Iterate over each possible neighbor
            for neighbor in self.getNeighbors(currentCell):
                # Calculate the cost of move
                h = self.h(currentCell)
                # Expand the node not seen 
                if neighbor not in movements:
                    # Add breadcrumb in dictionary
                    movements[neighbor] = currentCell
                    # Add the neighbor to sort by heuristic
                    frontier.put((h, neighbor))
    
    def aStarSearch(self):
        # Create frontier
        frontier = PriorityQueue()
        # Priority by f(n) = g(n) + h(n)
        frontier.put((0, self.start))

        # Create path tracker, KEY=toCell VALUE=fromCell
        movements = {}
        movements[self.start] = None

        # Create cost tracker, KEY=celL VALUE=cost of reaching this cell
        cellCost = {}
        cellCost[self.start] = 0
        
        while (not frontier.empty()):
            frontierCell = frontier.get()
            currentCell = frontierCell[1]
            
            if self.reachedGoal(currentCell):
                # Backtrack and print path
                return self.backtrack(currentCell, movements)

            # Iterate over each possible neighbor
            for neighbor in self.getNeighbors(currentCell):
                # Calculate the cost of move
                g = cellCost[currentCell] + self.g()
                # Expand the node with lowest path cost
                if neighbor not in movements or g < cellCost[neighbor]:
                    # Add breadcrumb in dictionary
                    movements[neighbor] = currentCell
                    f = g + self.h(currentCell)
                    # Add the neighbor to sort by cost
                    frontier.put((f, neighbor))
                    cellCost[neighbor] = g
                
    def printWorld(self):
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.world[x][y], end="")
            print()
        print()

# world = [[0,0,0,0,1],
#          [0,1,1,0,1],
#          [0,0,0,0,1],
#          [0,1,0,1,1],
#          [0,0,0,0,9]]

# myWorld = World(world)
# myWorld.printWorld()

# myWorld.breadthFirstSearch()
# myWorld.uniformCostSearch()
# myWorld.greedyBestFirstSearch()
# myWorld.aStarSearch()