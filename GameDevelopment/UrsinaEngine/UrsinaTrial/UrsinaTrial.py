from ursina import*
from random import randint

# Same as update function in UNITY C# - gets called at the end of each frame by URSINA
def update():
	global speed
	if abs(cube.x)>6:
		speed = speed * -1
	cube.x = cube.x + speed*time.dt
	
	if held_keys["r"]:
		cube.rotation_x = cube.rotation_x + time.dt*100
		cube.rotation_y = cube.rotation_y + time.dt*100
		cube.rotation_z = cube.rotation_z + time.dt*100
	
	cube_txt.text = "X = "+str(round(cube.x,2))

	global ball1_speed
	ball1.x += time.dt * ball1_speed
	if ball1.intersects().hit:
		ball1_speed *= -1

	global e4_speed
	e4.y += e4_speed*time.dt
	if abs(e4.y)>2:
		e4_speed*=-1

	global dragon_speed
	dragon.y+=dragon_speed*time.dt
	if abs(dragon.y)>2:
		dragon_speed*=-1


def input(key):
	global speed 
	global keyPressed_s
	if held_keys["s"] and keyPressed_s==False:
		speed = 3
		keyPressed_s = True
	if held_keys["t"]:
		speed = 0
		keyPressed_s = False

	if held_keys["c"]:
		red = randint(0,256)
		green = randint(0,256)
		blue = randint(0,256)
		cube.color = color.rgb(red, green, blue)

	if key =="1":
		a.state ="faucet"
	if key =="2":
		a.state ="faucet_running"


def printTextOnButtonClick():
	print_on_screen("Welcome to URSINA", position = (randint(-3,3)*.1,randint(-3,3)*.1))
	
app = Ursina()

speed = 0
keyPressed_s = False
cube = Entity(model="cube", scale = (1,1,1), color = color.rgb(200,100,70), texture = "white_cube")
cube2 = Entity(model="cube", scale = (2,2,2), position = (-2,-2,0), texture = "crate2.jpg",rotation =(45,45,0), color = color.gray)

box1 = Entity(model = "cube", scale = (1,2,1), texture = "white_cube", color=color.rgb(0,100,200), position = (5,3,0), collider = "box")
box2 = duplicate(box1, position = (-5,3,0))
ball1_speed = 3
ball1 = Entity(model = "sphere", color=color.pink, position = Vec3(0,3,0), collider = "box")

b = Button(scale=0.25,color=color.azure, text="A Button", text_color=color.orange, icon="sword",text_origin=(-0.5,0.5))
b.on_click=printTextOnButtonClick
#mouse.visible = False
b.tooltip = Tooltip("Click me")

cube_txt = Text()
camera.position = (0,0,-20)

faucet = Entity(model="quad", texture = "assets/faucet.png", position = (4,0,0), scale=(4,3,1))
faucet_running = Animation("assets/running_water", position = (4.4, -2.3, 0),scale=(0.4,2.5,1), fps = 8, loop = True, autoplay = True)
a = Animator(
	animations={
		"faucet": Entity(model="quad", texture = "assets/faucet.png", position = (4,0,0), scale=(4,3,1)),
		"faucet_running": faucet_running
	}
)
a.state = "faucet"

e1 = Entity(model="circle", position = (-5,-1,0))
e2 = Entity(model="quad",color = color.orange, position = (-5,-2,0))
e3 = Entity(model="quad", color = color.cyan, position = (-5,-3,0), scale_y=2)
s1 = Sequence(1, Func(e1.blink, duration=1),loop = True)
s2 = Sequence(1, Func(e2.blink, duration=1), Func(e2.shake, duration = 2),loop = True)
s3 = Sequence(2, Func(e3.fade_out, duration=2), 2, Func(e3.fade_in, duration = 2),loop = True)
s1.start()
s2.start()
s3.start()

e4_speed = 1
e4 = Entity(model="circle", position = (6.5,1,0), color = color.pink, scale=.4)
e5 = Entity(model="circle", position = (6.5,3,0), color = color.yellow, scale=.5)
e5.add_script(SmoothFollow(target=e4, offset=(0,1,0)))

dragon_speed =3
dragon = Entity(model="quad", scale=1, texture="assets/dragon_head.png", position=(-2.5,1.75,0))
dragon_tail=[None] * 50
dragon_tail[0]=Entity(model="circle", scale=.2, color=color.orange)
dragon_tail[0].add_script(SmoothFollow(target=dragon, offset=(0.1,0,0)))
for i in range(1,50):
	dragon_tail[i]=Entity(model="circle", scale=.2, color=color.rgb(255,50,50))
	dragon_tail[i].add_script(SmoothFollow(target=dragon_tail[i-1], offset=(.1,0,0)))

app.run()