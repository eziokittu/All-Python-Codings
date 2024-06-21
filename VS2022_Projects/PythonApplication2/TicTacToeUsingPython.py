''' Beginner Python Project - Tic Tac Toe Game using URSINA'''
from ursina import *
from random import randint

app = Ursina()

window.title = "Tic Tac Toe - Made by Bodhisatta" # The window title
window.borderless = True                         # Show a border
window.fullscreen = False                         # Do not go Fullscreen
window.exit_button.visible = True                # Do not show the in-game red X that closes the window
window.fps_counter.enabled = True                 # Show the FPS (Frames per second) counter
#window.windowed_size = 1.6
#window.update_aspect_ratio()
#window.late_init()
window.color = color.rgb(102, 102, 153)

# Defining functions
def CreateSqrBtn(btn, r, c):
    btn.append(Button(radius = 0, color=color.rgba(30,30,30,30),
        scale=bth_scale, x = btn_base_x+btn_gap*r, y = btn_base_y+btn_gap*c))

def CreateCrossTorus(state, cross, torus, r, c):
    '''state = 0 for creating cross
    and state = 1 for creating torus'''
    if state==0:
        cross.append(Entity( model="cross.obj", scale=cross_scale, color=color.red,
        rotation=(0,90,90), position = (entity_base_x+entity_gap*r, entity_base_y+entity_gap*c, 0) ))
    elif state==1:
        torus.append(Entity( model="torus.obj", scale=torus_scale ,color=color.green,
        rotation=(90,0,0), position = (entity_base_x+entity_gap*r, entity_base_y+entity_gap*c, 0) ))

def CreateAllEntitiesAndButtons():
    for i in range(9):
        CreateSqrBtn(btn, int(i/3), i%3)
        CreateCrossTorus(0, cross, torus, int(i/3), i%3)
        CreateCrossTorus(1, cross, torus, int(i/3), i%3)
        torus[i].visible = False
        cross[i].visible = False

def EnableTheShapesOnButtonClick(pos, shape):
    '''shape = 0 : Cross
    and shape = 1 : Torus'''
    global game_turn

    btn[pos].visible = False
    btn[pos].disabled = True
    if shape==0: cross[pos].visible = True
    elif shape==1: torus[pos].visible = True

    if game_turn == 0:
        game_turn = 1
    elif game_turn == 1:
        game_turn = 0

def ResetGame():
    global game_turn

    for i in range(9):
        cross[i].visible = False
        torus[i].visible = False
        btn[i].disabled = False
        btn[i].visible = True
    game_turn = 1

def update():
    global game_turn
    global entity_player1
    global entity_player2

    btn[0].on_click = lambda:EnableTheShapesOnButtonClick(0,game_turn)
    btn[1].on_click = lambda:EnableTheShapesOnButtonClick(1,game_turn)
    btn[2].on_click = lambda:EnableTheShapesOnButtonClick(2,game_turn)
    btn[3].on_click = lambda:EnableTheShapesOnButtonClick(3,game_turn)
    btn[4].on_click = lambda:EnableTheShapesOnButtonClick(4,game_turn)
    btn[5].on_click = lambda:EnableTheShapesOnButtonClick(5,game_turn)
    btn[6].on_click = lambda:EnableTheShapesOnButtonClick(6,game_turn)
    btn[7].on_click = lambda:EnableTheShapesOnButtonClick(7,game_turn)
    btn[8].on_click = lambda:EnableTheShapesOnButtonClick(8,game_turn)

    if game_turn==1:
        #entity_player1.rotation_x += randint(1,200)*time.dt
        entity_player1.rotation_y += 250*time.dt
        #entity_player1.rotation_x += randint(1,200)*time.dt
        entity_player2.rotation=(90,0,0)
    elif game_turn==0:
        #entity_player2.rotation_x += randint(1,200)*time.dt
        #entity_player2.rotation_y += randint(1,200)*time.dt
        entity_player2.rotation_z += 250*time.dt
        entity_player1.rotation=(0,90,90)

# Defining variables
btn = []
btn_base_x = -.3
btn_base_y = -.3
bth_scale = .25
btn_gap = bth_scale + bth_scale/10

cross = [] # a list of entities shaped as CROSS (like a 3D multiply sign)
torus = [] # a list of entities shaped as Torus (that circle thing in 3D)
entity_base_x = -2.5
entity_base_y = -2.5
cross_scale = .6 
torus_scale = .7 
entity_gap = bth_scale + bth_scale/10 + 2

game_turn = 1 # game starts with torus
# the list of sequences required for winning
#win_Pattern = [ "012","345","678","036","147","258","059","246" ]  
#player1_pattern = []
#player2_pattern = []

# Creating the entities and buttons
# A reset button
btn_reset = Button(scale=bth_scale,color=color.rgba(100,100,100,20),position=(-.025,.54,0))
btn_reset.on_click = ResetGame
text_reset = Text(text="RESET", scale=3, color=color.rgb(255,0,0), origin=(.1,-6))

# A grid layout for the game
entity_tictactoe = Entity(model="tictactoe.obj", rotation=(0,90,90), position=(-.21,-.21,0), scale=1.1)

# Players and their symbols
entity_player1 = Entity( model="torus.obj", scale=torus_scale ,color=color.green,
        rotation=(90,0,0), position = (-5,0,0) )
text_player1 = Text(text="Player 1", scale=3, origin=(2.17,-3.333), color=color.blue)
entity_player2 = Entity( model="cross.obj", scale=cross_scale, color=color.red,
        rotation=(0,90,90), position = (5,0,0) )
text_player2 = Text(text="Player 2", scale=3, origin=(-2.17,-3.333), color=color.blue)

CreateAllEntitiesAndButtons()

# A button for quitting game
btn_quit = Button(text="QUIT GAME", scale=0.2,color=color.rgb(255, 153, 204),
           position=(.750,-.36,0),text_color=color.rgb(255, 0, 0), tooltip = Tooltip('QUIT GAME'))
btn_quit.on_click = application.quit

# Running Ursina Engine loop
app.run()