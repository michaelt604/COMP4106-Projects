"""
 This example shows having multiple balls bouncing around the screen at the
 same time. You can hit the space bar to spawn more balls.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Based paddle on this
"""
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
paddle_SIZE = 25


class Paddle:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

 
def make_paddle():
    """
    Function to make a new, random ball.
    """
    paddle = Paddle()
    # Starting position of the paddle.
    # Take into account the ball size so we don't spawn on the edge.
    paddle.x = 0
    paddle.y = random.randrange(paddle_SIZE, SCREEN_HEIGHT - paddle_SIZE)
    #paddle.y = 0
    # Speed and direction of paddle 
    paddle.change_x = random.randrange(0, 3)
    paddle.change_y = random.randrange(0, 3)
 
    return paddle
 
 
def main():
    """
    This is our main program.
    """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Bouncing Balls")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    paddle_list = []
    paddle = make_paddle()
    paddle_list.append(paddle)
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new paddle.
             #   if event.key == pygame.K_SPACE:
              #      paddle = make_paddle()
               #     paddle_list.append(paddle)
 
        # --- Logic
        #for paddle in paddle_list:
            # Move the paddle's center
        paddle.x += paddle.change_x
        paddle.y += paddle.change_y

        # Bounce the paddle if needed
        if paddle.y > SCREEN_HEIGHT - paddle_SIZE or paddle.y < paddle_SIZE:
            paddle.change_y *= -1
        if paddle.x > SCREEN_WIDTH - paddle_SIZE or paddle.x < paddle_SIZE:
            paddle.change_x *= -1
 

        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)

        # Draw the paddles
        #for paddle in paddle_list:
            #pygame.draw.circle(screen, WHITE, [paddle.x, paddle.y], paddle_SIZE)
        pygame.draw.rect(screen, RED, pygame.Rect(paddle.x, paddle.y, 30, 60))
        pygame.draw.rect(screen, RED, pygame.Rect(670, paddle.y, 30, 60))
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()