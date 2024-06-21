from ursina import *

def update():
    for e in entities:
        e.rotation_y += time.dt *100

def input(key):
    if key =="1":
        camera.position = (0,0,-20)
        camera.rotation_x = 0
    elif key == "2":
        camera.position = (0,25,0)
        camera.rotation_x = 90
    elif key == "3":
        camera.position = (0,10,-17)
        camera.rotation_x = 30

app = Ursina()

entities=[]
sun = Entity(model="sphere", scale = 3, color = color.yellow)
earth = Entity(parent = sun,model="sphere", scale = .4, color = color.green, position = (1,0,1))
moon = Entity(parent = earth,model="sphere", scale = .3, color = color.gray, position = (.5,0,.5))
entities.append(sun)
entities.append(earth)
entities.append(moon)

app.run()