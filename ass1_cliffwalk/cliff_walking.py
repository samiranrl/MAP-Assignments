import numpy as np, random, copy

# defines the cliffworld environment

class cliff_walking():
    def __init__(self, stochasticity, size):
        self.stochasticity = stochasticity # The probability of an agent disobeying the action (modelling environment stochasticity)
        self.size = size # size of the gridworld
        self.reset()
    
    def reset(self):
        self.agent_loc_x = 0 # agent location
        self.agent_loc_y = 0
        self.done = False # is the episode finished?
        return (self.agent_loc_x, self.agent_loc_y)
        
    def render(self):
        if self.done == True:
            print("Can't render - Episode has finished, please use env.reset()")
            return
        
        grid = np.chararray((self.size,self.size), unicode=True)
        grid[:] = 'G' # Ground
        grid[0,1:-1] = 'H' # Holes
        grid[self.agent_loc_x, self.agent_loc_y] = 'M' # Mouse
        grid[0, self.size - 1] = 'C' # Cheese
        print (grid)
        return

        
    def step(self, action):
        if self.done:
            print ("Episode has finished, please use env.reset()")
            return None, None, None
        
        if random.random() < self.stochasticity:
            action = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
            
        agent_loc_next_x = self.agent_loc_x
        agent_loc_next_y = self.agent_loc_y
        
        if action == 'UP':
            agent_loc_next_x -= 1
        if action == 'DOWN':
            agent_loc_next_x += 1
        if action == 'LEFT':
            agent_loc_next_y -= 1
        if action == 'RIGHT':
            agent_loc_next_y += 1
        
        
        # Mouse gets the cheese
        
        if agent_loc_next_x == 0 and agent_loc_next_y == self.size-1:
            reward = 1
            self.done = True
            observation = None
            
        # Mouse goes out of bounds
        
        elif agent_loc_next_x < 0 or agent_loc_next_x > self.size - 1 or agent_loc_next_y < 0 or agent_loc_next_y > self.size - 1:
            reward = -100
            self.done = True
            observation = None
        
        # Mouse falls in hole
        
        elif agent_loc_next_x == 0 and agent_loc_next_y > 0 and agent_loc_next_y < self.size - 1:
            reward = -100
            self.done = True
            observation = None

        # Mouse moves on the ground
        
        else:
            reward = 0
            observation = (agent_loc_next_x, agent_loc_next_y)
            self.agent_loc_x = agent_loc_next_x
            self.agent_loc_y = agent_loc_next_y
        
        return observation, reward, self.done
