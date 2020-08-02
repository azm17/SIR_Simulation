# -*- coding: utf-8 -*-
import random as rnd
import matplotlib.pyplot as plt
from agent import Agent

class Simulation:
    def __init__(self, width, height, N, beta, gamma):
        self.agents = []
        self.width = width
        self.height = height
        self.N = N
        self.beta = beta   #感染確率
        self.gamma = gamma #回復率
        self.t = 0
        self.__generate_agent()# エージェント生成
        agent = rnd.choice(self.agents)
        agent.eta = 'I'
        agent.eta_next = 'I'
        
    def __generate_agent(self): # エージェントを生成
        position = [(i, j) for i in range(self.width) for j in range(self.height)]
        rnd.shuffle(position)
        for n in range(self.N):
            self.agents.append(Agent(position[n][0], position[n][1]))
        
    def update(self): # シミュレーションを更新
        self.t += 1
        for agent_i in self.agents:
            if agent_i.eta == 'S':
                for agent_j in self.agents:
                    if agent_j.eta == 'I':
                        if rnd.random() < self.beta and (agent_i.x - agent_j.x) ** 2 + (agent_i.y - agent_j.y) ** 2 <= 1:
                            agent_i.eta_next = 'I'
            elif agent_i.eta == 'I':
                if rnd.random() < self.gamma:
                    agent_i.eta_next = 'R'
        
        for agent in self.agents:
            agent.update()
        
    def count(self):
        s, i, r = 0, 0, 0
        for agent in self.agents:
            if agent.eta == 'S':
                s += 1
            elif agent.eta == 'I':
                i += 1
            elif agent.eta == 'R':
                r += 1
        
        print(f't={self.t} S: {s}, I: {i}, R: {r}')
        
    def draw(self): # 図を作成
        plt.figure(figsize=(4,4))
        plt.xlim(0, self.width)
        plt.ylim(0, self.height)
        plt.title(r'$t={}$'.format(self.t))
        color_dict = {'S':'blue', 'I': 'red', 'R': 'orange'}
        for i in range(self.N):
            plt.plot([self.agents[i].x + 0.5],
                     [self.agents[i].y + 0.5], 
                     marker='.', 
                     markersize=20,
                     color= color_dict[self.agents[i].eta])
