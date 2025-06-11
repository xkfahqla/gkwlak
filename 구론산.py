from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
cube = Entity(
    model = 'cube',
    scale = 5,
    color = color.red,
    collider = 'mesh',
    position = (5, 6, 5)
)
# map = [
#    [0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0]    
# ]
for i in range(10):
    i = Entity(
        model = 'cube',
        scale = 1,
        position = (1*i, 1*i, 1*i + 1),
        collider = 'mesh'
    )
def update():
    cube.rotation_x += 1
    cube.rotation_y += 1.5
    roller.rotation_x -= 1
    roller.rotation_y += 0.5
roller = Entity(
    model = 'cube',
    scale = 6,
    color = color.blue,
    position = (16, 11, 6),
    collider = 'mesh'
)
glower = Entity(
    model = 'cube',
    scale = 7,
    color = color.white,
    position = (23, 19, 7),
    Collider = 'mesh'
)
ground = Entity(
    model = 'plane',
    scale = 150,
    position = (0, 0, -50),
    color = color.gold,
    collider = 'mesh'
)
def input(key):
    if key == 'escape':
        app.quit()
app.run()