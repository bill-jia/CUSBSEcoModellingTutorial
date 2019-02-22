import numpy as np
from mesa import Agent, Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation
import random

class SCGrower(Agent):
    def __init__(self, unique_id, model, clone):
        super().__init__(unique_id, model)
        self.clone = clone
    
    def step(self):
        neighbourhood = [pos for pos in self.model.grid.iter_neighborhood(self.pos, True)]
        random.shuffle(neighbourhood)
        for pos in neighbourhood:
            if self.model.grid.is_cell_empty(pos):
                A = SCGrower(self.model.num_agents, self.model, self.clone)
                self.model.num_agents += 1
                print(self.model.num_agents)
                self.model.grid.place_agent(A, pos)
                self.model.schedule.add(A)
                break
                
class SCGrowthModel(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = SingleGrid(height, width, False)
        self.schedule = RandomActivation(self)
        for i in range(self.num_agents):
            a = SCGrower(i, self, i)
            self.schedule.add(a)
            self.grid.position_agent(a)
        
        self.running = True

    def step(self):
        self.schedule.step()