import pygame
from board import board
from button import Button

#---set the game window constants
width = 400
height = 400
background = (199, 199, 199)
FPS = 5

#---functions:

#----operating functions
def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def update():
    board.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def draw():
    window.fill(background)
    for button in buttons:
        button.draw()
    board.draw()

#---general functions:
def mouse_on_grid(pos):
    #check if mouse on the board
    if pos[0] > 50 and pos[0] < width-50:
        if pos[1] > 90 and pos[1] < height-10:
            return True
    return False

#set cells alive by mouse click
def click_cell(pos):
    #get the mouse position
    grid_pos = [pos[0]-50,pos[1]-90]
    #get the index for the cell
    grid_pos[0] = grid_pos[0]//10
    grid_pos[1] = grid_pos[1]//10
    #set the cell alive or dead from the user
    if board.grid[grid_pos[1]][grid_pos[0]].alive:
        board.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        board.grid[grid_pos[1]][grid_pos[0]].alive = True

def make_buttons():
    buttons = []
    #make run button
    buttons.append(Button(window, width//2-32, 25, 70, 30, text ='RUN', colour=(33, 207, 68), hover=(43, 255, 86), bold_text=True, function=run_game, state='setting'))
    #make puase button
    buttons.append(Button(window, width//2-32, 25, 70, 30, text ='PAUSE', colour=(18, 104, 135), hover=(51, 168, 212), bold_text=True, function=pause_game, state='running'))
    #make reset button
    buttons.append(Button(window, width//4-32, 25, 70, 30, text ='RESET', colour=(212, 40, 75), hover=(217, 54, 54), bold_text=True, function=reset_game, state='pause'))
    #make resume button
    buttons.append(Button(window, width//1.35-32, 25, 70, 30, text ='RESUME', colour=(33, 207, 68), hover=(43, 255, 86), bold_text=True, function=run_game, state='pause'))
    return buttons

#----buttons functions 
def run_game():
    global state
    state = 'running'

def pause_game():
    global state
    state = 'pause'

def reset_game():
    global state
    state = 'setting'
    board.reset_grid()


#---initiate the game
pygame.init()
window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
board = board(window, 50, 90)
buttons = make_buttons()
state = 'setting'

#---run the game
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting' or state == 'pause' :
        get_events()
        update()
        draw()
    if state == 'running':
        get_events()
        update()
        board.evaluate()
        draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
