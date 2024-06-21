from ursina import *
from random import randint

def update():
    global food_eaten_by_snake

    snake_movement()
    food_eaten_by_snake = detect_collisions()
    if food_eaten_by_snake:
        generate_food()
        increase_snake_length()
        update_texts_snake_length()
    snake_movement_bounds()

    update_texts_snake_length()

def detect_collisions():
    global txt_snake_length_updated
    global food
    global food_eaten_by_snake
    if food.intersects().hit:
        txt_snake_length_updated =False
        return True
    else: return False

def snake_movement():
    global snake_speed
    if held_keys["a"]:
        snake_head.x-=snake_speed*time.dt
    if held_keys["d"]:
        snake_head.x+=snake_speed*time.dt
    if held_keys["w"]:
        snake_head.y+=snake_speed*time.dt
    if held_keys["s"]:
        snake_head.y-=snake_speed*time.dt

def snake_movement_bounds():
    global snake_head
    global snake_width
    global boundary_width
    global movement_bound_left
    global movement_bound_right
    global movement_bound_top
    global movement_bound_bottom
    if (snake_head.x<movement_bound_left.x+snake_width/2+boundary_width/2):
        snake_head.x=movement_bound_left.x+snake_width/2+boundary_width/2
    if (snake_head.x>movement_bound_right.x-snake_width/2-boundary_width/2):
        snake_head.x=movement_bound_right.x-snake_width/2-boundary_width/2
    if (snake_head.y<movement_bound_bottom.y+snake_width/2+boundary_width/2):
        snake_head.y=movement_bound_bottom.y+snake_width/2+boundary_width/2
    if (snake_head.y>movement_bound_top.y-snake_width/2-boundary_width/2):
        snake_head.y=movement_bound_top.y-snake_width/2-boundary_width/2

def generate_food():
    global food
    global food_eaten_by_snake
    posX = randint(-625,625)/100
    posY = randint(-315,315)/100
    food.x = posX
    food.y = posY
    food_eaten_by_snake = False

def increase_snake_length():
    global snake_length
    global snake_tail
    for i in range(snake_length,snake_length+1):
	    snake_tail[i]=Entity(model="sphere", scale=.2, color=color.rgb(255,50,50))
	    snake_tail[i].add_script(SmoothFollow(target=snake_tail[i-1], offset=(.1,0,0), speed=25))
    snake_length +=1

def update_texts_snake_length():
    global txt_snake_length_updated
    global txt_snake_length
    global snake_length
    if not txt_snake_length_updated:
        if snake_length<10:
            txt_snake_length.text = "  Length : "+str(snake_length)
        elif snake_length <100:
            txt_snake_length.text = " Length : "+str(snake_length)
        else: txt_snake_length.text = "Length : "+str(snake_length)
        txt_snake_length_updated=True

app = Ursina()

# Game Window
window.title = "Game 1"
window.borderless = False 
window.exit_button.visible = False

# defining the snake
food_eaten_by_snake = False
snake_speed = 3
snake_length = 1
snake_width = .5
snake_head = Entity(model = "sphere", color=color.red, scale=snake_width, collider = "box", position=(0,0,0))
snake_tail=[None]*200
snake_tail[0]=Entity(model="sphere", scale=.4, color=color.orange)
snake_tail[0].add_script(SmoothFollow(target=snake_head, offset=(.1,0,0)))
food = Entity(model = "sphere", color=color.white,scale=0.25, position = Vec3(0,0,0), collider = "box")

# Creating the movement boundaries
boundary_width = 0.25
movement_bound_left = Entity(model="cube",position=(-6.5,0,0),scale=(boundary_width,7,0),color=color.gray)
movement_bound_right = duplicate(movement_bound_left, position=(6.5,0,0))
movement_bound_top = Entity(model="cube",position=(0,3.4,0),scale=(13.25,boundary_width,0),color=color.gray)
movement_bound_bottom = duplicate(movement_bound_top, position=(0,-3.4,0))

# Text
Text.default_resolution = 1080 * Text.size
txt_snake_length_updated = False
txt_snake_length = Text(text="Length : "+str(snake_length), origin=(5,-18), background=True)

app.run()