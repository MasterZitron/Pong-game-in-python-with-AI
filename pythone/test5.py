"""
Some different AIs I tried, they all suxs lmao

# Move on the ball's position, works the best
if ball.rect.y >= pBmid and ball.rect.x > 300:
            paddleB.moveDown(5)
        if ball.rect.y <= pBmid and ball.rect.x > 300:
            paddleB.moveUp(5)
        if ball.rect.y >= pAmid and ball.rect.x < 400:
            paddleA.moveDown(5)
        if ball.rect.y <= pAmid and ball.rect.x < 400:
            paddleA.moveUp(5)

# Try to predict where it will go and move, works most of the time
if ball.velocity[0] == (-4) and ball.velocity[1] <= 0 and ball.rect.y < pAmid:
            paddleA.moveUp(5)
        if ball.velocity[0] == (-4) and ball.velocity[1] >= 0 and ball.rect.y > pAmid:
            paddleA.moveDown(5)
        if ball.velocity[0] == 4 and ball.velocity[1] <= 0 and ball.rect.y < pBmid:
            paddleB.moveUp(5)
        if ball.velocity[0] == 4 and ball.velocity[1] >= 0 and ball.rect.y > pBmid:
            paddleB.moveDown(5)
"""

