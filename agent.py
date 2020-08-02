# -*- coding: utf-8 -*-

class Agent:
    def __init__(self, x, y):
        self.eta = 'S'
        self.eta_next = 'S'
        self.x = x
        self.y = y
    
    def update(self):# 状態の更新
        self.eta = self.eta_next

