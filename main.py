from FGAme import *
import random

world.add.margin(-200, 0)
world.gravity = (0, -500)
# world.background = 'backgroud'

TITLE = 'Falling Pixel'
WIDTH = 400
HEIGHT = 708
JUMPSPEED = 200
SPEED = 4
GAP = 10
WIDTH_RANGE = (0, 400)
HEIGHT_RANGE = (400, 700)
RANGE = (3,7)

p1 = world.add.circle(20, pos=(400, 300), color='red', mass='10')

@listen('long-press', 'right', dx=20)
@listen('long-press', 'left', dx=-20)
def move_p1_dx(dx):
    p1.move(dx, 0)

attacker1 = Actor('ghost', pos=(random.randint(*WIDTH_RANGE), 700))
attacker1.vy = random.randint(*RANGE)

attacker2 = Actor('ghost', pos=(random.randint(*WIDTH_RANGE), 700))
attacker2.vy = random.randint(*RANGE)

attacker3 = Actor('ghost', pos=(random.randint(*WIDTH_RANGE), 700))
attacker3.vy = random.randint(*RANGE)

def set_random_height(attacker):
    attacker.x = random.randint(*WIDTH_RANGE)
    attacker.vy += 0.5
    if pixel.dead:
        pixel.x = WIDTH / 2
        pixel.image = 'awesomeface'
        pixel.vx = 0
        pixel.dead = False

def dead():
    pixel.dead = True
    pixel.image = 'awesomeserious'

def update(dt):

    pixel.x += pixel.vx * dt
    pixel.vy =  0
    if keyboard.left and not pixel.dead:
        pixel.vx = -JUMPSPEED
    if keyboard.right and not pixel.dead:
        pixel.vx = JUMPSPEED
    if not pixel.dead:
        pixel.image = 'awesomeface'

    attacker1.y -= attacker1.vy/dt*dt
    attacker2.y -= attacker2.vy/dt*dt
    attacker3.y -= attacker3.vy/dt*dt

    if attacker1.y < 0:
        set_random_height(attacker1)
        attacker1.y = HEIGHT + 50

    if attacker2.y < 0:
        set_random_height(attacker2)
        attacker2.y =  HEIGHT + 50

    if attacker3.y < 0:
        set_random_height(attacker3)
        attacker3.y = HEIGHT + 50

    if not pixel.dead and pixel.right > attacker1.left and pixel.left < attacker1.right and pixel.top < attacker1.bottom and pixel.bottom > attacker1.top:
        dead()

    if not pixel.dead and pixel.right > attacker2.left and pixel.left < attacker2.right and pixel.top < attacker2.bottom and pixel.bottom > attacker2.top:
        dead()

    if not pixel.dead and pixel.right > attacker3.left and pixel.left < attacker3.right and pixel.top < attacker3.bottom and pixel.bottom > attacker3.top:
        dead()



def draw():
    screen.blit('background', pos=(0, 0))
    attacker1.draw()
    attacker2.draw()
    attacker3.draw()
    pixel.draw()

run()
