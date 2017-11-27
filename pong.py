# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
speed_multiple=1



#paddle1_pos=[[0,HEIGHT/2-PAD_HEIGHT/2],[0,HEIGHT/2 + PAD_HEIGHT/2]]
paddle1_pos=HEIGHT/2
paddle1_vel=0
#paddle2_pos=[[WIDTH,HEIGHT/2-PAD_HEIGHT/2],[WIDTH,HEIGHT/2 + PAD_HEIGHT/2]]
paddle2_pos=HEIGHT/2
paddle2_vel=0
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,0]
acc=[1,1]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel ,speed_multiple# these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    #ball_vel=[1,1]
    #if ball_pos
    rand_x=random.randrange(120, 240)/60
    rand_y=-random.randrange(60, 180)/60
    speed_multiple=1
    if direction == LEFT:
        ball_vel = [-rand_x, rand_y]
    if direction == RIGHT:
        ball_vel = [rand_x, rand_y]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos,paddle2_pos=HEIGHT/2,HEIGHT/2
    score1,score2=0,0
    paddle1_vel,paddle2_vel=0,0
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel,speed_multiple
    

    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += speed_multiple*ball_vel[0]
    ball_pos[1] += speed_multiple*ball_vel[1]
    
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    print "PAddle pos",paddle1_pos,paddle2_pos
    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel
    
    #fNewY = self.tPos._iY() + self.vVelocity._fY()
    #if fNewY >= self.iMaxY
    #lower bborder
    if paddle1_pos>= (HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos=HEIGHT-HALF_PAD_HEIGHT
        paddle1_vel=0
    elif paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos=HALF_PAD_HEIGHT
        padde1_vel=0
        
    if paddle2_pos>= (HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos=HEIGHT-HALF_PAD_HEIGHT
        paddle2_vel=0
    elif paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos=HALF_PAD_HEIGHT
        padde2_vel=0
    
        
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos-HALF_PAD_HEIGHT],[PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT],[PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT],[0,paddle1_pos+HALF_PAD_HEIGHT]],1,'white','white')
    canvas.draw_polygon([[WIDTH-PAD_WIDTH,paddle2_pos-HALF_PAD_HEIGHT],[WIDTH,paddle2_pos-HALF_PAD_HEIGHT],[WIDTH,paddle2_pos+HALF_PAD_HEIGHT],[WIDTH-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT]],1,'white','white')
    #print (ball_pos[0]-BALL_RADIUS)
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH and ball_pos[1]:
        if ball_pos[1] < paddle1_pos - HALF_PAD_HEIGHT or ball_pos[1] > paddle1_pos + HALF_PAD_HEIGHT:
            score2 += 1
            spawn_ball(RIGHT)
        else:
            ball_vel[0] = -ball_vel[0]
            speed_multiple = 1.1*speed_multiple
            
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if ball_pos[1] < paddle2_pos - HALF_PAD_HEIGHT or ball_pos[1] > paddle2_pos + HALF_PAD_HEIGHT:
            score1 += 1
            spawn_ball(LEFT)
        else:
            ball_vel[0] = -ball_vel[0]
            speed_multiple = 1.1*speed_multiple
            
        
    if ball_pos[1] >= (HEIGHT-BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] <=0:
        ball_vel[1] = -ball_vel[1]    
    #draw scores
    canvas.draw_text(str(score1), (260, 100), 36, 'White')
    canvas.draw_text(str(score2), (340, 100), 36, 'White')
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
       
    #Paddle control
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= 5
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += 5
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 5
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

def reset():
    new_game()
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button1 = frame.add_button('RESET',reset)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
