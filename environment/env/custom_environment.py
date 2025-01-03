import random
from pettingzoo import ParallelEnv
from .player import Player
from copy import copy


class parallel_env(ParallelEnv):
    metadata = {
        "name": "custom_environment_v0",
    }

    def __init__(self, render_mode=None):
        self.agents = [];
        self.player1 = Player();
        self.player2 = Player();

    def reset(self, seed=None, options=None):
        total = 9
        
        for x in range(7):
            self.player1.virtues[x] = 0
            self.player2.virtues[x] = 0
        
        for x in range(9):
            p1 = random.randint(0, 7)
            p2 = random.randint(0, 7)
            
            self.player1.virtues[p1] = self.player1.virtues[p1] + 1
            self.player2.virtues[p2] = self.player2.virtues[p2] + 1
        observations = {}
        infos = {}
        
        return observations, infos

    def step(self, actions):
        pass

    def render(self):
        pass

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]