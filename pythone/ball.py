import pygame
from random import randint
BLACK = (0,0,0)

# This class represents a paddle, it derives from the sprite class in Pygame
class Ball(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        # Call the parent class Sprite constructor (again, no idea wtf that means it was on the website)

        # Pass in width and height of the ball
        self.image = pygame.Surface([width, height])
        # Set the background color and set it to be transparent
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (...a rectangle)
        pygame.draw.rect(self.image, color, [0,0, width, height])

        # Set it's X and Y velocity, change values here
        # My friend suggested I use Pythagores theorem to make it the ball velocity
        # and i have no clue how tf i do that so i didnt do it
        self.velocity = [randint(4,4),randint(-4,8)]
        self.rect = self.image.get_rect()
    def update(self): # Always update ball position
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    def bounce(self): # bouncy
        self.velocity[0] =- self.velocity[0]
        self.velocity[1] =- randint(-4,8) # Random orientantion the ball will bounce to



