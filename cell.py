import pygame

class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()
        self.neighbours = []
        self.alive_neighbours = 0
        
    def update(self):
        self.rect.topleft = (self.grid_x*10, self.grid_y*10)
        
    def draw(self):
        if self.alive:
            self.image.fill((0, 0, 0))
        else:
            self.image.fill((0, 0, 0))
            pygame.draw.rect(self.image, (255, 255, 255), (1, 1, 9, 9))
        self.surface.blit(self.image, (self.grid_x*10,self.grid_y*10))

    def get_neighbours(self, grid):
        neighbour_list = [[1,1],[-1,-1],[-1,1],[1,-1],[0,-1],[0,1],[1,0],[-1,0]]
        #set the correct index of the neighbours
        for neighbour in neighbour_list:
            neighbour[0] += self.grid_x
            neighbour[1] += self.grid_y
        #fix to continue on the other side of the board
        for neighbour in neighbour_list:
            if neighbour[0] < 0:
                neighbour[0] += 30
            if neighbour[1] < 0:
                neighbour[1] += 30
            if neighbour[0] > 29:
                neighbour[0] -= 30
            if neighbour[1] > 29:
                neighbour[1] -= 30
        # init the cell's neighbours
        for neighbour in neighbour_list:
            try:
                self.neighbours.append(grid[neighbour[1]][neighbour[0]])
            except: #if the calculation was wrong
                print(neighbour)
    
    def live_neighbours(self):
        count = 0
        for neighbour in self.neighbours:
            if neighbour.alive:
                count +=1
        self.alive_neighbours = count