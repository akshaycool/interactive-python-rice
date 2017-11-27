import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
#vel = [-40.0 / 60.0,  5.0 / 60.0]
vel = [0,0]
acc=[0,0]
time=0
# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
    if ball_pos[0] >= (WIDTH-BALL_RADIUS):
        vel[0] = - vel[0]
    if ball_pos[1] >= (HEIGHT-BALL_RADIUS):
        vel[1] = - vel[1]
    if ball_pos[1] <=0:
        vel[1] = -vel[1]

    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    
def keydown(key):
    #acc = 1
    if key==simplegui.KEY_MAP["left"]:
        vel[0] -= acc[0]
    elif key==simplegui.KEY_MAP["right"]:
        vel[0] += acc[0]
    elif key==simplegui.KEY_MAP["down"]:
        vel[1] += acc[1]
    elif key==simplegui.KEY_MAP["up"]:
        vel[1] -= acc[1]
        
    print ball_pos
    '''
    global var,count
    count=count+1
    var*=2    
    print "keydown",var
    '''
    

def keyup(key):
    #acc = 1
    if key==simplegui.KEY_MAP["left"]:
        vel[0] -= acc[0]
    elif key==simplegui.KEY_MAP["right"]:
        vel[0] += acc[0]
    elif key==simplegui.KEY_MAP["down"]:
        vel[1] += acc[1]
    elif key==simplegui.KEY_MAP["up"]:
        vel[1] -= acc[1]
        
    print ball_pos
    '''
    global var,count
    count+=1
    var-=3
    print "keyup",var
    '''
    
def incr():
    global time
    time=time+1
    acc[0]+=0.1
    acc[1]+=0.1
    
# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)
timer=simplegui.create_timer(100,incr)
# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
# start frame
frame.start()
timer.start()
