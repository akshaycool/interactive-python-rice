import simplegui
import math


time=0
my_score=0
total_score=0
stopwatch_running=False
timer_check=False

def reset_values():
    global time,my_score,total_score
    time=0
    my_score=0
    total_score=0

def format(t):
    a,b,c,d=0,0,0,0
    if(t==0):
        return str(a)+':'+str(b)+str(c)+'.'+str(d)
    d=t%10
    c=((t/10)-(t/600)*60)%10
    b=((t/10)-(t/600)*60)/10
    a=t/600                    
    return str(a)+':'+str(b)+str(c)+'.'+str(d)
    
def start():
    global timer,stopwatch_running,timer_check
    stopwatch_running=True
    timer_check=True
    timer.start()

def stop():
    
    global timer,stopwatch_running,total_score,my_score
    timer.stop()
    if stopwatch_running and total_score<5:
        total_score=total_score+1
        if ((time%10) == 0):
            my_score=my_score+1
    stopwatch_running=False
    
def reset():
    global timer,stopwatch_running
    stopwatch_running=False
    timer.stop()
    reset_values()
        
def stopwatch():
    global time
    time=time+1

def draw_handler(canvas):
    global time,total_score,my_score,stopwatch_running
    time_text=format(time)
    canvas.draw_text(time_text,(60,100),36,'Blue')
    if (stopwatch_running or timer_check):
        canvas.draw_text(str(my_score)+"/"+str(total_score),(160,20),20,'Yellow')
            

frame=simplegui.create_frame('STOPWATCH GAME',200,200)
frame.set_draw_handler(draw_handler)
timer=simplegui.create_timer(100,stopwatch)


start_button=frame.add_button('START',start)
stop_button=frame.add_button('STOP',stop)
reset_button=frame.add_button('RESET',reset)

                                 
frame.start()