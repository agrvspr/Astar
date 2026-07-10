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
    goal = node.maze.get_goal()
    row, col = node.state
    goal_row, goal_col = goal

    mDist= abs(row - goal_row) + abs(col - goal_col)
    
    grid = node.maze.get_grid()
    max_jump = grid[0][0]
    for line in grid:
        for cell in line:
            if cell > max_jump:
                max_jump = cell

    return mDist / max_jump



def ASTAR(maze: RookJumpingMaze, heuristic):
    pq = PriorityQueue()
    visited = [] # add nodes that you expand here 
    start_state = tuple(maze.get_start())
    start = Node(start_state, 0, maze, [start_state])
    pq.push(heuristic(start), start)  # add the starting node to your priority queue  
    i = 1
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
        
        if node.state in visited:
            continue
        
        visited.append(node.state)

        if node.is_goal():
            return node.path, len(visited)

        for neighbor_state in node.get_neighbors():
            if neighbor_state in visited:
                continue

            new_cost = node.cost + 1
            new_path = node.path + [neighbor_state] #make tuple a list for append
            neighbor_node = Node(neighbor_state, new_cost, maze, new_path)

            priority = new_cost + heuristic(neighbor_node) # Manhattan / Max Jump Is MINE
            pq.push(priority, neighbor_node)
    
    return None, len(visited)

if __name__ == "__main__":
    print(ASTAR(EXAMPLE_MAZE, dummy_heuristic)) 
    print(ASTAR(EXAMPLE_MAZE, heuristic)) 

    