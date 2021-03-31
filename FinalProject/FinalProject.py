#PONG pygame

import random
import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = round(PAD_WIDTH / 2)
HALF_PAD_HEIGHT = round(PAD_HEIGHT / 2)
ball_num = 0
total_balls
balls=[]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Pong')

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
class Ball: 
	#initialize balls in the center
	def __init__(self,right):	
		self.ball_pos = [WIDTH/2,HEIGHT/2] # center of screen
		horz = random.randrange(2,4)
		vert = random.randrange(1,3)
		
		if right == False:  
			horz = - horz   # shoot ball left if variable is false
			
		self.ball_vel = [horz,-vert]  # ball starts shooting downward

	# reset balls to shoot from middle to opposite side of goal
	def resetBall(self,right):
		self.ball_pos = [WIDTH/2,HEIGHT/2] # reset to the center
		horz = random.randrange(2,4)
		vert = random.randrange(1,3)
		ball_num += 1
		
		if right == False:  
			horz = - horz   # shoot ball left if variable is false
		self.ball_vel = [horz,-vert]


# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,l_score,r_score,total_balls,balls,ball_num # these are floats
    global score1, score2  # these are ints
    paddle1_pos = [round(HALF_PAD_WIDTH - 1), round(HEIGHT/2)]
    paddle2_pos = [round(WIDTH +1 - HALF_PAD_WIDTH), round(HEIGHT/2)]
    l_score = 0
    r_score = 0
	total_balls = 1
	balls = []
	ball_num = total_balls
   
   #initilize list of balls
    if random.randrange(0,2) == 0:
        for x in range(total_balls):
			balls.append(Ball(True))
    else:
        for x in range(total_balls):
			balls.append(Ball(False))


#draw function of canvas
def draw(canvas):
    global paddle1_pos, paddle2_pos, l_score, r_score,ball_num,total_balls,balls,ball_num
           
    canvas.fill(BLACK)
    pygame.draw.line(canvas, WHITE, [WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(canvas, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] > HALF_PAD_HEIGHT and paddle1_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == HALF_PAD_HEIGHT and paddle1_vel > 0:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle1_vel < 0:
        paddle1_pos[1] += paddle1_vel
    
    if paddle2_pos[1] > HALF_PAD_HEIGHT and paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HALF_PAD_HEIGHT and paddle2_vel > 0:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle2_vel < 0:
        paddle2_pos[1] += paddle2_vel

    #update balls
	for pongBall in balls:
		pongBall.ball_pos[0] += round(pongBall.ball_vel[0])
		pongBall.ball_pos[1] += round(pongBall.ball_vel[1])

    #draw paddles and ball
	 for pongball in balls: 
		colour =  [random.randrange(1,254), random.randrange(1,254), random.randrange(1,254)]  # different colour for each ball
		pygame.draw.circle(canvas, colour, pongball.ball_pos, 20, 0)
    pygame.draw.polygon(canvas, GREEN, [[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT]], 0)
    pygame.draw.polygon(canvas, GREEN, [[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT]], 0)

    #ball collision check on top and bottom walls
    for pongBall in balls:
		if round(pongBall.ball_pos[1]) <= BALL_RADIUS:
        	pongBall.ball_vel[1] = - pongBall.ball_vel[1]
    	if round(pongBall.ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
        	pongBall.ball_vel[1] = -pongBall.ball_vel[1]
    
    #ball collison check on gutters or paddles
	r_goal = False
    for pongball in balls:	
		if round(pongball.ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and round(pongball.ball_pos[1]) in range(paddle1_pos[1] - HALF_PAD_HEIGHT,paddle1_pos[1] + HALF_PAD_HEIGHT,1):
			pongball.ball_vel[0] = -ball_vel[0]
			pongball.ball_vel[0] *= 1.1
			pongball.ball_vel[1] *= 1.1
		elif round(pongball.ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:
			r_score += 1
			ball_num -= 1
			r_goal = True	
			
	
	for pongball in balls:	
		if round(pongball.ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and round(pongball.ball_pos[1]) in range(paddle2_pos[1] - HALF_PAD_HEIGHT,paddle2_pos[1] + HALF_PAD_HEIGHT,1):
			pongball.ball_vel[0] = -ball_vel[0]
			pongball.ball_vel[0] *= 1.1
			pongball.ball_vel[1] *= 1.1
		elif round(pongball.ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
			l_score += 1
			ball_num -= 1
			r_goal = False
	
	#If no more balls in play, reset them all in center
	if ball_num = 0: 
		for pongball in balls:
			pongball.resetBall(r_goal)
		ball_num = total_balls
    
	#update scores
    myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = myfont1.render("Score "+str(l_score), 1, (255,255,0))
    canvas.blit(label1, (50,20))

    myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = myfont2.render("Score "+str(r_score), 1, (255,255,0))
    canvas.blit(label2, (470, 20))  
    
    
#keydown handler
def keydown(event):
    global paddle1_vel, paddle2_vel
    
    if event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 8
    elif event.key == K_w:
        paddle1_vel = -8
    elif event.key == K_s:
        paddle1_vel = 8

#keyup handler
def keyup(event):
    global paddle1_vel, paddle2_vel
    
    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0

init()


#game loop
while True:

    draw(window)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fps.tick(60)
def main():
	return

if (__name__ == "__main__"):
	main()