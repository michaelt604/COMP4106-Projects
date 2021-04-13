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
from pygame.locals import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
paddle_SIZE = 25

PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = round(PAD_WIDTH / 2)
HALF_PAD_HEIGHT = round(PAD_HEIGHT / 2)

BALL_RADIUS = 20
ball_num = 0
total_balls = 0
balls = []
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

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

        paddle.change_y = 2
    
        return paddle

class Ball:
    # initialize balls in the center
    def __init__(self, right, id):
        horz = random.randrange(2, 4)
        vert = random.randrange(1, 3)
        if (random.randint(0, 1)):  # start ball shoooiing left or right
            horz = -horz

        self.id = id
        self.ball_pos = [random.randrange(200, 400), random.randrange(50, SCREEN_HEIGHT-50)]  # start in a range of the center
        self.colour = [random.randrange(1, 254), random.randrange(1, 254), random.randrange(1, 254)]  # different colour for each ball
        self.ball_vel = [horz, -vert]
        self.final_pos = ""
        self.bouncePosition()   #Calculate final position

    def bouncePosition(self):   #Calculates the final position
        bounce = False
        tempPos = [self.ball_pos[0], self.ball_pos[1]]
        tempVel = [self.ball_vel[0], self.ball_vel[1]]

        while(True):    #Loop until we hit the edge
            #Modify position based on velocity
            tempPos[0] += round(tempVel[0])
            tempPos[1] += round(tempVel[1])

            if (round(tempPos[1]) <= BALL_RADIUS) or (round(tempPos[1]) >= SCREEN_HEIGHT + 1 - BALL_RADIUS):    #If we hit the roof, flip the vertical velocity
                tempVel[1] *= -1    

            if (round(tempPos[0]) <= BALL_RADIUS + PAD_WIDTH) or (round(tempPos[0]) >=SCREEN_WIDTH + 1 - BALL_RADIUS - PAD_WIDTH):    # Ball hits the left or right side
                self.final_pos = [tempPos[0], tempPos[1]]
                break


# define event handlers
def init():
    # these are floats
    
    global l_score, r_score, paddle1_pos
    global score1, score2, total_balls, balls, ball_num   # these are ints
    paddle1_pos = [round(HALF_PAD_WIDTH - 1), round(SCREEN_HEIGHT/2)]
    '''
    paddle1_pos = [round(HALF_PAD_WIDTH - 1), round(HEIGHT/2)]
    paddle2_pos = [round(WIDTH + 1 - HALF_PAD_WIDTH), round(HEIGHT/2)]
    
    paddle1.x = round(HALF_PAD_WIDTH - 1)
    paddle1.y = round(HEIGHT/2)

    paddle2.x = round(WIDTH + 1 - HALF_PAD_WIDTH)
    paddle2.y = round(HEIGHT/2)
    '''
    l_score = 0
    r_score = 0
    total_balls = 1  # <<<<<<<<<<<<<<  HOW YOU CHNAGE TOTAL NUMBER OF BALLS
    balls = []
    ball_num = total_balls

    # initilize list of balls
    if random.randrange(0, 2) == 0:
        for x in range(total_balls):
            balls.append(Ball(True, x))
    else:
        for x in range(total_balls):
            balls.append(Ball(False, x))

# keydown handler
def keydown(event):
    global paddle1_vel, paddle2_vel

    if event.key == K_UP:
        paddle1_vel = -8
        #paddle1.change_y = -8
    elif event.key == K_DOWN:
        paddle1_vel = 8
        #paddle1.change_y = 8
    '''
    elif event.key == K_w:
        paddle1_vel = -8
    elif event.key == K_s:
        paddle1_vel = 8
    '''
# keyup handler
def keyup(event):
    global paddle1_vel, paddle2_vel

    if event.key in (K_UP, K_DOWN):
        #paddle1.change_y = 0
        paddle1_vel = 0
    '''
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0
    '''

def main():
    """
    This is our main program.
    """
    pygame.init()
    global paddle1_pos, paddle2_pos, l_score, r_score, ball_num, total_balls, balls, ball_num, paddle1_vel
    # Set the height and width of the screen
    init()
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
            #elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new paddle.
             #   if event.key == pygame.K_SPACE:
              #      paddle = make_paddle()
               #     paddle_list.append(paddle)
 
        # --- Logic
        #for paddle in paddle_list:
            # Move the paddle's center
        #paddle1.x += paddle1.change_x
        #paddle1.y += paddle1.change_y

        if (balls[0].final_pos[1] > paddle2.y):
            paddle2.y -= paddle2.change_y
        elif (balls[0].final_pos[1] < paddle2.y):
            paddle2.y += paddle2.change_y

        #paddle2.x += paddle2.change_x
        #paddle2.y += paddle2.change_y

        # Bounce the paddle if needed
        if paddle1_pos[1] > HALF_PAD_HEIGHT and paddle1_pos[1] < SCREEN_HEIGHT - HALF_PAD_HEIGHT:
            paddle1_pos[1] += paddle1_vel
        elif paddle1_pos[1] == HALF_PAD_HEIGHT and paddle1_vel > 0:
            paddle1_pos[1] += paddle1_vel
        elif paddle1_pos[1] == SCREEN_HEIGHT - HALF_PAD_HEIGHT and paddle1_vel < 0:
            paddle1_pos[1] += paddle1_vel
        
        '''
        if paddle2.x > HALF_PAD_HEIGHT and paddle1_pos[1] < SCREEN_HEIGHT - HALF_PAD_HEIGHT:
            paddle2.x += paddle1_vel
        elif paddle2.x == HALF_PAD_HEIGHT and paddle1_vel > 0:
            paddle2.x += paddle1_vel
        elif paddle2.x == SCREEN_HEIGHT - HALF_PAD_HEIGHT and paddle1_vel < 0:
            paddle2.x += paddle1_vel
        '''
        '''
        if paddle1.y > SCREEN_HEIGHT - PAD_HEIGHT or paddle1.y < 0:
            paddle1.change_y *= -1
        if paddle1.x > SCREEN_WIDTH  - PAD_WIDTH or paddle1.x < PAD_WIDTH:
            paddle1.change_x *= -1
        '''

        #if paddle2.y > SCREEN_HEIGHT - PAD_HEIGHT or paddle2.y < 0:
        #    paddle2.change_y *= -1
        #if paddle2.x > SCREEN_WIDTH  - PAD_WIDTH or paddle2.x < PAD_WIDTH:
        #    paddle2.change_x *= -1
 
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [SCREEN_WIDTH / 2, 0], [SCREEN_WIDTH / 2, SCREEN_HEIGHT], 1)
        pygame.draw.line(screen, WHITE, [PAD_WIDTH, 0], [PAD_WIDTH, SCREEN_HEIGHT], 1)
        pygame.draw.line(screen, WHITE, [SCREEN_WIDTH - PAD_WIDTH, 0], [SCREEN_WIDTH - PAD_WIDTH, SCREEN_HEIGHT], 1)
        pygame.draw.circle(screen, WHITE, [SCREEN_WIDTH//2, SCREEN_HEIGHT//2], 70, 1)
        # Draw the paddles
        #for paddle in paddle_list:
            #pygame.draw.circle(screen, WHITE, [paddle.x, paddle.y], paddle_SIZE)
        #pygame.draw.rect(screen, RED, pygame.Rect(paddle1.x, paddle1.y, PAD_WIDTH, PAD_HEIGHT))
        pygame.draw.polygon(screen, RED, [[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT]], 0)
        pygame.draw.rect(screen, GREEN, pygame.Rect(SCREEN_WIDTH - PAD_WIDTH, paddle2.y, PAD_WIDTH, PAD_HEIGHT))
        for pongBall in balls:
            pongBall.ball_pos[0] += round(pongBall.ball_vel[0])
            pongBall.ball_pos[1] += round(pongBall.ball_vel[1])

    # draw balls and paddles
        for pongball in balls:
            pygame.draw.circle(screen, pongball.colour, pongball.ball_pos, 20, 0)

        # ball collision check on top and bottom walls
        for pongBall in balls:
            if round(pongBall.ball_pos[1]) <= BALL_RADIUS:
                pongBall.ball_vel[1] = -pongBall.ball_vel[1]
            if round(pongBall.ball_pos[1]) >=SCREEN_HEIGHT + 1 - BALL_RADIUS:
                pongBall.ball_vel[1] = -pongBall.ball_vel[1]
            # ball collison check on gutters or paddles
        r_goal = False
        for pongball in balls:
            #leftSide = round(pongball.ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and round(pongball.ball_pos[1]) in range(paddle1.y - HALF_PAD_HEIGHT, paddle1.y + HALF_PAD_HEIGHT, 1)
            leftSide = round(pongball.ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and round(pongball.ball_pos[1]) in range(paddle1_pos[1] - HALF_PAD_HEIGHT, paddle1_pos[1] + HALF_PAD_HEIGHT, 1)
            rightSide = round(pongball.ball_pos[0]) >=SCREEN_WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and round(pongball.ball_pos[1]) in range(paddle2.y - HALF_PAD_HEIGHT, paddle2.y + HALF_PAD_HEIGHT, 1)

            score = False
            if (leftSide or rightSide):
                pongball.ball_vel[0] = -pongball.ball_vel[0]
                pongball.ball_vel[0] *= 1.1
                pongball.ball_vel[1] *= 1.1
                pongball.bouncePosition()
                paddle2.y = pongball.final_pos[1]

            elif round(pongball.ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:    # when scored on left side, increase score remove ball from list of balls        
                score = True
                r_score += 1                
            
            elif round(pongball.ball_pos[0]) >=SCREEN_WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:    # when scored on right side, increase score remove ball from list of balls          
                score = True
                l_score += 1

            if (score):
                ball_num -= 1
                r_goal = True
                balls.remove(pongball)
                paddle2.y = pongball.final_pos[1]
                print(f"FinalPos: {pongball.ball_pos}, CalcFinalPos: {pongball.final_pos}")
            
            #after ball estimation this changes paddle 2's location
            if paddle2.y > SCREEN_HEIGHT - PAD_HEIGHT or paddle2.y < 0:
                paddle2.change_y *= -1
                paddle2.y = pongball.final_pos[1]
    
            if paddle2.x > SCREEN_WIDTH  - PAD_WIDTH or paddle2.x < PAD_WIDTH:
                paddle2.change_x *= -1

        # If no more balls in play, reset game by remaking total number of balls
        if ball_num == 0:
            for x in range(total_balls):
                balls.append(Ball(r_goal, x))  # remake total number of balls
            ball_num = total_balls

        # update scores
        myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
        label1 = myfont1.render("Score "+str(l_score), 1, (255, 255, 0))
        screen.blit(label1, (50, 20))

        myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
        label2 = myfont2.render("Score "+str(r_score), 1, (255, 255, 0))
        screen.blit(label2, (470, 20))
        # --- Wrap-up
        # Limit to 60 frames per second
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                keydown(event)
            elif event.type == KEYUP:
                keyup(event)
            elif event.type == pygame.QUIT:
                done = True
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()