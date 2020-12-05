from pygame import draw
class Attractor:
    def __init__(self, pos):
        self.pos = pos
        self.mass = 20
        self.gFactor = .1
    
    def draw(self, screen):
        draw.circle(screen, (255,0,0), (self.pos.x, self.pos.y), 10)

    def attract(self, ball):
        diff = self.pos - ball.pos
        diff.normalize()
        return self.gFactor * (self.pos - ball.pos) / self.mass
