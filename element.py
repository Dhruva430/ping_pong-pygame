from pygame import Surface, Vector2
import pygame 
import random

class ping_pong:
    def __init__(self,screen_size) -> None:
        self.rect = pygame.Rect(0,0,0,0)
        self.position = Vector2(
            random.randint(0,screen_size[0]),
            random.randint(0,screen_size[1])
        )
        self.direction = Vector2(
            random.choice((-1,1)),
            random.choice((-1,1))
        )
        self.velocity = 300
        self.colour = (
            random.randint(0,255),random.randint(0,255),random.randint(0,255)
        )
        self.direction2 = Vector2(0)

    def draw(self,screen: Surface):

        self.rect = pygame.draw.circle(screen, self.colour,self.position,10)

    def update(self,size,delta):
        self.position += self.direction*self.velocity*delta
        p = self.position
        # if p.x<0:
        #     # self.direction.x = 1
        #     self.position = Vector2(400,300)
        if p.y<0:
            self.direction.y = 1
        # if p.x>size[0]:
        #     # self.direction.x = -1
            
        if p.y>size[1]:
            self.direction.y = -1


def clamp(n, lower, upper):
    return min(max(n, lower), upper)

class paddle:
    def __init__(self,x: int) -> None:
        self.position = Vector2(x,0)
        self.rect = pygame.Rect(0,0,0,0)


    def draw(self, screen: Surface):
        self.rect = pygame.draw.rect(screen,(255,0,0),pygame.Rect(self.position.x,self.position.y,10,100))

        # pygame.Rect.colliderect(rect1, rect2)
    def update(self):
        self.position.y = clamp(self.position.y,0,500)
        

        

    
    
