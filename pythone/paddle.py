import pygame
BLACK = (0,0,0)

# This class represents a paddle, it derives from the sprite class in Pygame
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # Call the parent class Sprite constructor(no idea wtf this mean)
        super().__init__()

        # Pass in the color of the paddle, its x and y position, width and height
        self.image = pygame.Surface([width, height])
        # Set the background color and set it to be transparent
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (A rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()


    def moveUp(self, pixels):
        self.rect.y -= pixels# Check that you are not going too far (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0
        
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400 :
            self.rect.y = 400
