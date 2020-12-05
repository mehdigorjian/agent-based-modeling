import pygame, random
from ball import Ball
from attractor import Attractor
from settings import *
# -------------------------------------------------------
pygame.init()
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Mehdi\'s Agent')
clock = pygame.time.Clock()
# -------------------------------------------------------
gForce = pygame.math.Vector2(0,0.2)
wForce = pygame.math.Vector2(0.05,0)
balls = []
mouse_X, mouse_Y = pygame.mouse.get_pos()
# -------------------------------------------------------
def ball_control():
    att = Attractor(pygame.math.Vector2(mouse_X, mouse_Y))
    att.draw(win)
    print(mouse_X, mouse_Y)

    if len(balls) < NUMBER_OF_BALLS:
        posInit = pygame.math.Vector2(random.randint(0,W),random.randint(0,H))
        sz = random.randint(2,MAX_SIZE)
        ball = Ball(posInit, sz**2, sz, sz)
        balls.append(ball)
    
    flag = False   
    for ball in balls:
        attForce = att.attract(ball)
        ball.add_force(attForce)
        ball.add_force(gForce)
        if flag:
            ball.add_force(wForce)
            flag = False
        else:
            ball.add_force(-wForce)
            flag = True

        # friction = - ball.vel
        # if friction.length() != 0:
        #     friction.normalize()
        #     friction *= 0.01 
        # ball.add_force(friction)

        ball.update()
        ball.check_edges()
        ball.draw(win)

    for i in range(len(balls)):
        if i < len(balls)-1:
            balls[i].draw_line(balls[i+1], win)
        else:
            balls[0].draw_line(balls[i], win)
            
        # for bb in balls:
            # if ball.pos.distance_to(bb.pos) > DIST:
                # ball.draw_line(bb, win)
# -------------------------------------------------------
def redraw():
    win.fill((0,0,0))
    ball_control()
    pygame.display.update()
    clock.tick(30)
# -------------------------------------------------------
def main_loop():
    global mouse_X, mouse_Y
    action = True
    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                action = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_X, mouse_Y = pygame.mouse.get_pos()

        redraw()
main_loop()