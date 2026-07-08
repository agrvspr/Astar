
from files.RJM import RookJumpingMaze, EXAMPLE_MAZE
class PriorityQueue:
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list) == 0 
    def push(self, p, v):
        self.list.append((p,v))
        self.list.sort(key=lambda n: n[0], reverse=False)

    
    def pop(self):
        return self.list.pop(0)[1]

class Node:
    def __init__(self, state, cost, maze:RookJumpingMaze, path =[]):
        self.state = state 
        self.maze = maze 
        self.path = path 
        self.cost = cost  
    
    def is_goal(self):
        return self.maze.is_goal(self.state)
    
    def get_neighbors(self):

        return self.maze.get_moves(self.state)
    

def dummy_heuristic(node):
    return 0 

def heuristic(node):
    """
    Enter your heuristic function here 
    
    Node has both the state (node.state) 
    and the maze (node.maze) that you 
    can use 
    """
    pass 


def ASTAR(maze: RookJumpingMaze, heuristic):
    pq = PriorityQueue()
    visited = [] # add nodes that you expand here 
    start = Node(maze.get_start(), 0, maze)
    pq.push(heuristic(start), start)  # add the starting node to your priority queue  

    while not pq.is_empty():
        """
        Complete the function 

        Remember that when you find the goal 
        you will need to return both the 
        path (list of states) and the total number 
        of nodes you expanded 

        e.g your return function should look 
        something like:

        return node.path, len(visited)
        """
        node = pq.pop()

            
if __name__ == "__main__":
    print(ASTAR(EXAMPLE_MAZE, dummy_heuristic)) 
    print(ASTAR(EXAMPLE_MAZE, heuristic)) 

    