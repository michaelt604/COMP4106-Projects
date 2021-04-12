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


class Paddle1:
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
        paddle = Paddle1()
        # Starting position of the paddle.
        # Take into account the ball size so we don't spawn on the edge.
        paddle.x = 0 #x coordinate where the ball will be
        paddle.y = 100 #where the y will be for the ball coordinates
        #paddle.y = 0

        # Speed and direction of paddle 
        paddle.change_x = random.randrange(1, 3)
        paddle.change_y = random.randrange(1, 3)
    
        return paddle
 

class Paddle2:
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
        paddle = Paddle2()
        # Starting position of the paddle.
        # Take into account the ball size so we don't spawn on the edge.
        paddle.x = 0 #x coordinate where the ball will be
        paddle.y = 0 #where the y will be for the ball coordinates
        #paddle.y = 0

        # Speed and direction of paddle 
        paddle.change_x = random.randrange(1, 3)
        paddle.change_y = random.randrange(1, 3)
    
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
    
    paddle1 = Paddle1.make_paddle() #calls the make paddle function for the x and y's
    paddle2 = Paddle2.make_paddle() 
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
        paddle1.x += paddle1.change_x
        paddle1.y += paddle1.change_y

        paddle2.x += paddle2.change_x
        paddle2.y += paddle2.change_y

        # Bounce the paddle if needed
        if paddle1.y > SCREEN_HEIGHT - 60 or paddle1.y < 0:
            paddle1.change_y *= -1
        if paddle1.x > SCREEN_WIDTH  - 30 or paddle1.x < 30:
            paddle1.change_x *= -1

        if paddle2.y > SCREEN_HEIGHT - 60 or paddle2.y < 0:
            paddle2.change_y *= -1
        if paddle2.x > SCREEN_WIDTH  - 30 or paddle2.x < 30:
            paddle2.change_x *= -1
 
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)

        # Draw the paddles
        #for paddle in paddle_list:
            #pygame.draw.circle(screen, WHITE, [paddle.x, paddle.y], paddle_SIZE)
        pygame.draw.rect(screen, RED, pygame.Rect(paddle1.x, paddle1.y, 30, 60))
        pygame.draw.rect(screen, RED, pygame.Rect(670, paddle2.y, 30, 60))
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()