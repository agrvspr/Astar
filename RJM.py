
class RookJumpingMaze: 
    def __init__(self, grid, start, end):
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = grid 
        self.start = start 
        self.end = end 
    
    def get_start(self):
        return self.start
    
    def get_goal(self):
        return self.end 
    def get_grid(self):
        return self.grid 
    
    def print_grid(self):
        s = ""
        for li in self.grid:
            for num in li:
                s += num + " "
            s += "\n"
        
        print(s)
                
    def is_goal(self, state):
        return state[0] == self.end[0] and state[1] == self.end[1] 

    def get_moves(self, state):
        next_states = []
        num_moves = self.grid[state[0]][state[1]]

        up = (state[0] - num_moves, state[1])
        down = (state[0] + num_moves, state[1])
        left = (state[0], state[1] - num_moves)
        right = (state[0], state[1] + num_moves)

        if (up[0] >= 0):
            next_states.append(up)
        
        if (down[0] < self.height):
            next_states.append(down)
        
        if (left[1] >= 0):
            next_states.append(left)
        
        if (right[1] < self.width):
            next_states.append(right)
        
        return next_states 

example_grid = [[4,0,3,3,2], 
                [3,3,4,4,4], 
                [1,1,3,4,4], 
                [3,3,3,1,2], 
                [3,1,1,3,3]]
EXAMPLE_MAZE = RookJumpingMaze(example_grid, [3,0], [0,1])