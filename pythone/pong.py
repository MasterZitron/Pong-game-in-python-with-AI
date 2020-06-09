"""
Pong Game made in Python!
I followed a tutorial online so i didn't make this from scratch
but the AI part was 100% all me (my brother is sleeping so he can't play with me and I don't wanna play alone lol, finished at 3 am).

Left Paddle: W and S 
Right Paddle: 'UP' arrow and 'DOWN' arrow

To toggle the second player between AI and human, change "AI" variable to either 'True' or 'False'

Sometimes the ball can get stuck inside a paddle and freak out, but hey i didn't made this i just
followed a tutorial
"""
# Ai Toggle
AI = False

#import modules and start pygame
import pygame
from paddle import Paddle
from ball import Ball
import time

pygame.init()

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Open a new window
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Paddle creation
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# Ball creation
ball = Ball(WHITE, 10, 10)
ball.rect.x = 350
ball.rect.y = 250

# A list that will contain all of the sprites we are going to use in the game
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#The game will keep going till user press X button (quits)
CarryOn = True

#Game FPS
clock = pygame.time.Clock()



# When one of the players score, reset both paddles and the ball positions
def reset():
    restart = True
    time.sleep(1)
    restart = False
    paddleB.rect.x = 670
    paddleB.rect.y = 200
    paddleA.rect.x = 20
    paddleA.rect.y = 200
    ball.rect.x = 350
    ball.rect.y = 250
    ball.bounce()
# Scores
scoreA = 0
scoreB = 0
#----- main thing loop-----
restart = False
while CarryOn == True and restart == False:
    #Main loop for events
    for event in pygame.event.get(): #if user does something
        if event.type == pygame.QUIT: #if they closed it
            CarryOn = False # END
        elif event.type == pygame.KEYDOWN:
            if event.key== pygame.K_x: # Pressing X quits the game
                CarryOn = False # END
            if event.key== pygame.K_r:
                reset()
    # Moving the paddles when the keys "W","S" and the arrow keys "up" and "down" are pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: 
        paddleA.moveUp(5) # move 5 pixels up
    if keys[pygame.K_s]: 
        paddleA.moveDown(5) # move 5 pixels Down 

    # If playing with someone else, enable Arrow Keys
    if AI == False:
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]: 
            paddleB.moveDown(5)
    
    # If alone, play with impossible AI
    # okay almost impossible, trying to make it predict the ball's direction
    # based on its velocity, its hard cuz i have soft brain
    if AI == True:
        pAmid = (paddleA.rect.y + 50) # I added 50 extra pixels to the paddles because it was hitting the ball with its edge
        pBmid = (paddleB.rect.y + 50) # doing this made it hit right in the middle
        if ball.rect.x > 350:
            if ball.velocity[0] == 4 and ball.velocity[1] >= 0 and ball.rect.y > pBmid:
                paddleB.moveDown(5)
            if ball.velocity[0] == 4 and ball.velocity[1] >= 0 and ball.rect.y < pBmid:
                paddleB.moveUp(5)
            if ball.velocity[0] == 4 and ball.velocity[1] <= -1 and ball.rect.y > pBmid:
                paddleB.moveDown(5)
            elif ball.velocity[0] == 4 and ball.velocity[1] <= -1 and ball.rect.y < pBmid:
                paddleB.moveUp(5)
            if ball.velocity[0] == 4 and ball.velocity[1] <= -3 and ball.rect.y < pBmid:
                paddleB.moveUp(5)
            if ball.velocity[0] == 4 and ball.velocity[1] <= -5 and ball.rect.y < pBmid:
                paddleB.moveDown(5)
        """ #Uncomment this section to have both paddles as AI
        else:
            if ball.velocity[0] == -4 and ball.velocity[1] >= 0 and ball.rect.y > pAmid:
                paddleA.moveDown(5)
            if ball.velocity[0] == -4 and ball.velocity[1] >= 0 and ball.rect.y < pAmid:
                paddleA.moveUp(5)
            if ball.velocity[0] == -4 and ball.velocity[1] <= -1 and ball.rect.y > pAmid:
                paddleA.moveDown(5)
            elif ball.velocity[0] == -4 and ball.velocity[1] <= -1 and ball.rect.y < pAmid:
                paddleA.moveUp(5)
            if ball.velocity[0] == -4 and ball.velocity[1] <= -3 and ball.rect.y < pAmid:
                paddleA.moveUp(5)
            if ball.velocity[0] == -4 and ball.velocity[1] <= -5 and ball.rect.y < pAmid:
                paddleA.moveDown(5)
            """

        

    # Update sprites
    all_sprites_list.update()

    # check if the ball is bouncing against any walls
    if ball.rect.x >= 690: #if it reackes the wall behind second player, the first one scores and the game is reseted
        scoreA+=1
        reset()
    if ball.rect.x <= 0: # same thing but for player 2
        scoreB+=1
        reset()
    if ball.rect.y >= 490: # Bounce of top and bottom walls
        ball.velocity[1] =- ball.velocity[1]
        print(ball.velocity[0], ',', ball.velocity[1])
    if ball.rect.y <= 0:
        ball.velocity[1] =- ball.velocity[1]
        print(ball.velocity[0], ',', ball.velocity[1])

    # Detect collisions on the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
        print(ball.velocity[0], ',', ball.velocity[1])

    
    # fill screen with black
    screen.fill(BLACK)

    #Draw a line on the middle
    pygame.draw.line(screen, WHITE, [349,0], [349,500],5)

    # Display Scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE) 
    screen.blit(text, (420,10))

    # Draw all of our sprites
    all_sprites_list.draw(screen)
    #Update the screen
    pygame.display.flip()

    #Limit to 60 FPS
    clock.tick(60)

#Close the game when CarryOn = False
pygame.quit()