import pygame
import copy
from cell import *

vec = pygame.math.Vector2

class board:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x, y)
        self.width = 300
        self.height = 300
        self.image = pygame.Surface((self.width,self.height))
        self.rect = self.image.get_rect()
        self.rows = 30
        self.cols = 30
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)]for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)

    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()

    def draw(self):
        self.image.fill((102,102,102))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x,self.pos.y))

    def reset_grid(self):
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)]for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)
   
    def evaluate(self):
        new_grid = copy.copy(self.grid)
        #get alive neighbours from cells
        for row in self.grid:
            for cell in row:
                cell.live_neighbours()
        #update cells state
        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_neighbours < 2:
                        new_grid[yidx][xidx].alive = False
                    if cell.alive_neighbours > 3:
                        new_grid[yidx][xidx].alive = False
                    if cell.alive_neighbours == 2 or cell.alive_neighbours == 3:
                        new_grid[yidx][xidx].alive = True
                if not cell.alive:
                    if cell.alive_neighbours == 3:
                        new_grid[yidx][xidx].alive = True
        self.grid = new_grid