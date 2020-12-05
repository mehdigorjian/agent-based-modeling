from pygame import draw, math
from settings import *
class Ball:
    def __init__(self, pos, mass, size_X, size_Y):
        self.pos = pos
        self.vel = math.Vector2(0,0)
        self.acc = math.Vector2(0,0)
        self.mass = mass
        self.size_X = size_X
        self.size_Y = size_Y
    
    def draw(self, screen):
        draw.rect(screen, (255,255,255), (self.pos.x, self.pos.y, self.size_X, self.size_Y))
        # draw.line(screen, (255,0,0), (self.pos.x, self.pos.y), (self.size_X, self.size_Y))

    def draw_line(self, other, screen):
        draw.line(screen, (255,0,0), (self.pos.x, self.pos.y), (other.pos.x,other.pos.y))

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def add_force(self, force):
        self.acc += force * self.mass * 0.1
        # print(self.acc)
    
    def check_edges(self):
        if self.pos.x < 0:
            self.pos.x = MAX_SIZE
            self.vel.x *= -1
        if self.pos.x > W:
            self.pos.x = W - MAX_SIZE
            self.vel.x *= -1
        if self.pos.y < 0:
            self.pos.y = MAX_SIZE
            self.vel.y *= -1
        if self.pos.y > H:
            self.pos.y = H - MAX_SIZE
            self.vel.y *= -1
        
