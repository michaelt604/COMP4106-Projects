"""
 This example shows having multiple balls bouncing around the screen at the
 same time. You can hit the space bar to spawn more balls.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 Based paddle on this
"""
import heapq
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
paddles = []

l_score = 0
r_score = 0

paddle1 = 0
paddle2 = 0

averageFps = 60.0

class Paddle:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self, id, colour, xStart, yStart, control):
        self.id = id
        self.colour = colour
        self.x = xStart
        self.y = yStart
        self.change_x = 0
        self.change_y = 0
        self.control = control
        self.moveVel = 8
        self.calcDelay = 0

    def movePaddle(self, balls):    #AI Handling of the ball movement
        ''' if (self.control == "AI"):
            if (abs(balls[0].final_pos[1] - self.y) <= 8):  #If within distance of point, stop moving
                self.change_y = 0   
            elif (balls[0].final_pos[1] > self.y):
                self.change_y = self.moveVel
            elif (balls[0].final_pos[1] < self.y):
                self.change_y = -self.moveVel
        '''     
        if (self.control == "AI"):

            orderedBalls = []

            while balls != []:                                         # prio list not empty
                bally = heapq.heappop(balls)                        # take top ball on list 
                orderedBalls.append(bally)
            
            if orderedBalls != []:  #list not empty                
                reachBall = self.canGetToBall(orderedBalls[0], self.y)
                reachBall2 = False

                target = orderedBalls[0][3].final_pos[1]
                #print(f"target default: {target}")

                if (len(orderedBalls) > 1 and not reachBall):   #If there are only two balls, and first ball isn't reachable, prioritise
                    reachBall2 = self.canGetToBall(orderedBalls[1], self.y)
                    if (reachBall2):    #Ball 2 is reachable but ball 1 isn't. We set ball2 as the target instead
                        target = orderedBalls[1][3].final_pos[1]
                        #print(f"target not default 2: {target}")          

                if (len(orderedBalls) > 2 and reachBall):  #If there are three or more balls, and first ball is reachable, but the next two are not
                    reachBall2 = self.canGetToBall(orderedBalls[1], orderedBalls[0][3].final_pos[1])    #Time to get reachBall2 from ball1 position
                    if (not reachBall2):    #We can't reach second ball after getting first ball
                        reachBall2 = self.canGetToBall(orderedBalls[1], self.y)
                        if (reachBall): #We can reach second ball from starting position
                            reachBall3 = self.canGetToBall(orderedBalls[2], orderedBalls[1][3].final_pos[1])
                            if (reachBall3):    #We can reach second and third ball from starting position, but not with first, then target second ball
                                target = orderedBalls[1][3].final_pos[1]
                                #print(f"target not default 3: {target}")

                if (abs(target - self.y) <= 8):  #If within distance of point, stop moving
                    self.change_y = 0   
                elif (target > self.y):
                    self.change_y = self.moveVel
                elif (target < self.y):
                    self.change_y = -self.moveVel
                

            #print(f"Position: {self.y} - Goal {balls[0].final_pos[1]}")

        # Bounce the paddle if needed
        if (self.y > HALF_PAD_HEIGHT and self.y < SCREEN_HEIGHT - HALF_PAD_HEIGHT):
            self.y += self.change_y
        elif (self.y == HALF_PAD_HEIGHT and self.change_y > 0):
            self.y += self.change_y
        elif (self.y == SCREEN_HEIGHT - HALF_PAD_HEIGHT and self.change_y < 0):
            self.y += self.change_y
    
    def canGetToBall(self, bally, startPos):
        totalIterations = 0
        testPos = startPos     #Paddle pos
        finalPos = bally[3].final_pos[1]    #Ball final pos

        while(True):
            if (abs(finalPos - testPos) <= 8):  #If within distance of point, stop moving
                break
            elif (finalPos > testPos):
                totalIterations += 1
                testPos += self.moveVel
            elif (finalPos < testPos):
                totalIterations += 1
                testPos -= self.moveVel
        ticks = pygame.time.get_ticks()
        timeToBall = ticks + totalIterations / averageFps * 1000  #Number of milliseconds    
        returnVal = timeToBall < bally[0] + 5    #Can reach ball in time

        #if(not returnVal):
        #    print("Ball not reachable")
        return returnVal


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
        self.arrivalT = []
        self.bounces = 0
        self.countI = 0

        self.bouncePosition()   #Calculate final position


    def bouncePosition(self):   #Calculates the final position        
        self.countI -= 1
        if (self.countI <= 0):
            bounce = False
            tempPos = [self.ball_pos[0], self.ball_pos[1]]
            tempVel = [self.ball_vel[0], self.ball_vel[1]]

            self.bounces = 0
            while(True):    #Loop until we hit the edge
                self.bounces += 1
                #Modify position based on velocity
                tempPos[0] += round(tempVel[0])
                tempPos[1] += round(tempVel[1])

                if (round(tempPos[1]) <= BALL_RADIUS) or (round(tempPos[1]) >= SCREEN_HEIGHT + 1 - BALL_RADIUS):    #If we hit the roof, flip the vertical velocity
                    tempVel[1] *= -1    

                if (round(tempPos[0]) <= BALL_RADIUS + PAD_WIDTH) or (round(tempPos[0]) >=SCREEN_WIDTH + 1 - BALL_RADIUS - PAD_WIDTH):    # Ball hits the left or right side
                    self.final_pos = [tempPos[0], tempPos[1]]
                    self.timeOfArrival()
                    
                    self.countI = 30
                    break
            self.countI = 30


    def timeOfArrival(self): 
        #bounceTime = pygame.time.get_ticks() + self.bounces / averageFps * 1000    #Number of milliseconds    
        bounceTime = pygame.time.get_ticks() + self.bounces / averageFps * 1000 - (self.bounces / 3)    #Number of milliseconds    

        #bounceTime = pygame.time.get_ticks() + self.bounces * 33.5    #Number of milliseconds        
    
        if (self.ball_vel[0] > 0): # if ball is going right
            self.arrivalT = [bounceTime, "R"]
        else:
            self.arrivalT = [bounceTime, "L"]
        #print(f"Time of Arrival: {round(self.arrivalT[0])}")
        
        



# define event handlers
def init():
    # these are floats
    
    global l_score, r_score, paddle1_pos
    global score1, score2, total_balls, balls, ball_num   # these are ints    

    l_score = 0
    r_score = 0
    total_balls = 5  # <<<<<<<<<<<<<<  HOW YOU CHNAGE TOTAL NUMBER OF BALLS
    balls = []
    ball_num = total_balls

    #Initialize the paddles

    # initilize list of balls
    if random.randrange(0, 2) == 0:
        for x in range(total_balls):
            balls.append(Ball(True, x))
    else:
        for x in range(total_balls):
            balls.append(Ball(False, x))

# keydown handler
def keydown(event):
    for paddle in paddles:
        if (paddle.id == 1 and paddle.control == "Player"):
            if (event.key == K_w):
                paddle.change_y = -8
            elif (event.key == K_s):
                paddle.change_y = 8
        elif (paddle.id == 2 and paddle.control == "Player"):
            if (event.key == K_UP):
                paddle.change_y = -8
            elif (event.key == K_DOWN):
                paddle.change_y = 8

# keyup handler
def keyup(event):
    for paddle in paddles:
        if (paddle.id == 1 and paddle.control == "Player"):
            if (event.key in (K_w, K_s)):
                paddle.change_y = 0
        if (paddle.id == 2 and paddle.control == "Player"):
            if (event.key in (K_UP, K_DOWN)):
                paddle.change_y = 0


def main():
    """
    This is our main program.
    """
    pygame.init()
    global l_score, r_score, ball_num, total_balls, balls, paddles, ball_num, paddle1_vel, paddle1, paddle2
    # Set the height and width of the screen
    init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Bouncing Balls")

    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    paddles.append(Paddle(1, GREEN, round(HALF_PAD_WIDTH - 1), round(SCREEN_HEIGHT/2), "Player"))      #Paddle 1
    paddles.append(Paddle(2, RED, round(SCREEN_WIDTH + 1 - HALF_PAD_WIDTH), round(SCREEN_HEIGHT/2), "AI"))    #Paddle 2

    def prioList(side, ballsPlaying):  # pritority list for balls
        priotemp=[]
        for pongballs in ballsPlaying:
            if pongballs.arrivalT[1] == side:
                heapq.heappush(priotemp,(pongballs.arrivalT[0]-pygame.time.get_ticks(),pongballs.ball_vel[0],pongballs.id, pongballs))
        return priotemp

    print("start main loop")

    cc = 0
    # -------- Main Program Loop -----------
    while not done:
        #cc += 1
        #if (cc % 100 == 0):
            #print(clock.tick(30))
            #elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new paddle.
             #   if event.key == pygame.K_SPACE:
              #      paddle = make_paddle()
               #     paddle_list.append(paddle)
 

        '''Move Game Entities'''
        for pongBall in balls:  #Move balls
            pongBall.ball_pos[0] += round(pongBall.ball_vel[0])
            pongBall.ball_pos[1] += round(pongBall.ball_vel[1])

        prioBallsR = prioList("R", balls) # Prioity list for right paddle
        prioBallsL = prioList("L", balls) # and left

       # for paddle in paddles:  #Move paddles
        #    paddle.movePaddle(prioBallsR)
        paddles[0].movePaddle(prioBallsL)
        paddles[1].movePaddle(prioBallsR)

        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [SCREEN_WIDTH / 2, 0], [SCREEN_WIDTH / 2, SCREEN_HEIGHT], 1)
        pygame.draw.line(screen, WHITE, [PAD_WIDTH, 0], [PAD_WIDTH, SCREEN_HEIGHT], 1)
        pygame.draw.line(screen, WHITE, [SCREEN_WIDTH - PAD_WIDTH, 0], [SCREEN_WIDTH - PAD_WIDTH, SCREEN_HEIGHT], 1)
        pygame.draw.circle(screen, WHITE, [SCREEN_WIDTH//2, SCREEN_HEIGHT//2], 70, 1)
        

        # draw balls 
        for pongball in balls:
            pygame.draw.circle(screen, pongball.colour, pongball.ball_pos, 20, 0)

        #Draw the paddles    
        for paddle in paddles:
            pygame.draw.polygon(screen, paddle.colour, [[paddle.x - HALF_PAD_WIDTH, paddle.y - HALF_PAD_HEIGHT], [paddle.x - HALF_PAD_WIDTH, paddle.y + HALF_PAD_HEIGHT], [paddle.x + HALF_PAD_WIDTH, paddle.y + HALF_PAD_HEIGHT], [paddle.x + HALF_PAD_WIDTH, paddle.y - HALF_PAD_HEIGHT]], 0)


        # ball collision check on top and bottom walls
        for pongBall in balls:
            if round(pongBall.ball_pos[1]) <= BALL_RADIUS:
                pongBall.ball_vel[1] = -pongBall.ball_vel[1]
            if round(pongBall.ball_pos[1]) >=SCREEN_HEIGHT + 1 - BALL_RADIUS:
                pongBall.ball_vel[1] = -pongBall.ball_vel[1]
        
        # ball collison check on gutters or paddles
        r_goal = False
        for pongball in balls:
            leftSide = round(pongball.ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and round(pongball.ball_pos[1]) in range(paddles[0].y - HALF_PAD_HEIGHT, paddles[0].y + HALF_PAD_HEIGHT, 1)
            rightSide = round(pongball.ball_pos[0]) >=SCREEN_WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and round(pongball.ball_pos[1]) in range(paddles[1].y - HALF_PAD_HEIGHT, paddles[1].y + HALF_PAD_HEIGHT, 1)
            

            score = False
            if (leftSide or rightSide):
                pongball.ball_vel[0] = -pongball.ball_vel[0]
                pongball.ball_vel[0] *= 1.1
                pongball.ball_vel[1] *= 1.1
                pongball.bouncePosition()
                #pongball.timeOfArrival()
                #print(f"Time of Arrival: {round(pygame.time.get_ticks())}")

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
                #paddle2.y = pongball.final_pos[1]
                print(f"FinalPos: {pongball.ball_pos}, CalcFinalPos: {pongball.final_pos}")
            
        pongball.bouncePosition()   #Recalculate every frame (testing only)

            
 
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

        # --- Wrap-up :: Limit to 60 frames per second :: Event Processing --- 
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
        #pygame.display.set_caption("fps: " + str(clock.get_fps()))
        averageFps = clock.get_fps()
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()