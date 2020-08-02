# -*- coding: utf-8 -*-
from sir import Simulation

width = 20; height = 20
beta = 0.4; gamma = 0.01
N = 250

simulation = Simulation(width, height, N, beta, gamma)
simulation.draw(); simulation.count()
for t in range(1, 601):
    simulation.update()
    if t % 200 == 0:
        simulation.draw(); simulation.count()