# Implementation of classic arcade game Pong

import simplegui
import random

# CONSTANTS
# the nearest thing to constants I found in Python are single-value functions
def aTableWidth(): return 600
def aTableHeigth(): return 400
def aBallRadius(): return 14
def aBallColor(): return "Orange"
def asPaddleColor(): return "White"
def asDividingLineColor(): return "Green"
def aPaddleWidth(): return 8
def aPaddleHeight(): return 80
def asFrameName(): return "Pong game"
def aiControlAreaWidth(): return 70
def aiButtonWidth(): return 60
def aiScoreFontSize(): return 100
def asScoreFontFace(): return "sans-serif"
def asScoreColor(): return "Green"

class PositionClass:
    def __init__(self):
        """Create a new position with zero coordinates"""
        self.iX = 0
        self.iY = 0
        return self
    
    def __init__(self,iX,iY):
        """create a position from a pair of coordinates"""
        self.iX = iX
        self.iY = iY
        return self
    
    def _tGetXY(self):
        return (self.iX, self.iY)
    
    def _iX(self): return self.iX
    
    def _iY(self): return self.iY
    
    def _tMove(self, vIncrement):
        self.iX = round(self.iX + vIncrement.fXcomp)
        self.iY = round(self.iY + vIncrement.fYcomp)
        return (self.iX, self.iY)
    
    def __str__(self):
        """convert to string for printing"""
        return ("( %g, %g )" % (self.iX, self.iY) )

class VectorClass:
    """ Vector variables such as speed, acceleration etc"""
    def __init__(self):
        """a zero vector"""
        self.fXcomp = 0
        self.fYcomp = 0
        return self
    
    def __init__(self,fX, fY):
        """Initialize vector with X and Y components.
        Parameters: fX, fY: floats"""
        self.fXcomp = fX
        self.fYcomp = fY
        return self
    
    def add(self, vAnother):
        self.fXcomp += vAnother.fXcomp
        self.fYcomp + vAnother.fYcomp
        return
    
    def _IncrX(self,fChange):
        self.fXcomp += fChange
        return
    
    def _IncrY(self,fChange):
        self.fYcomp += fChange
        return
    
    def _Mult_By_Number(self,fNum):
        self.fXcomp *= fNum
        self.fYcomp *= fNum
        return
    
    def _fX(self): return self.fXcomp
    
    def _fY(self): return self.fYcomp
    
    def _BounceY(self): 
        self.fYcomp = -self.fYcomp
        return
    
    def _BounceX(self):
        self.fXcomp = -self.fXcomp
        return
    
    def _Set(self,fX,fY):
        self.fXcomp = fX
        self.fYcomp = fY
        return
    
    def _tfGetXY(self): return (self.fXcomp, self.fYcomp)
    
    def __str__(self):
        """convertion to string for printint"""
        return ( "x=%g, y=%g" % (self.fXcomp, self.fYcomp) )


class BallClass:
    def __init__(self, iX, iY):
        self.ptCurrentPos = PositionClass(iX, iY)
        self.vVelocity = VectorClass(0,0)
        self.iRadius = aBallRadius()
        self.sColor = aBallColor()
        return self
    
    def _SetPos(self, iX, iY):
        self.ptCurrentPos = PositionClass(iX, iY)
        return
    
    def _SetSpeed(self, fXcomp, fYcomp):
        self.vVelocity._Set(fXcomp, fYcomp)
        return
    
    def _oWhere(self): return self.ptCurrentPos

    def _tNextPos(self):
        """compute a next position of the ball with
        the current position and velocity"""
        self.ptCurrentPos._tMove(self.vVelocity)
        return self.ptCurrentPos._tGetXY()
    
    def _Launch(self,sDirection):
        if sDirection.lower() == "right":
            fXcomp=random.randrange(1,3)
        elif sDirection.lower() == "left":
            fXcomp=random.randrange(-2,0)
        fYcomp = random.randrange(-4,-1)
        self.vVelocity._Set(fXcomp, fYcomp)
        return
    
    def _Draw(self,oCanvas):
        # update position
        self._tNextPos()
        # print "*DBG* + str(self.ptCurrentPos), + " " + str(self.vVelocity)
        # draw the ball
        oCanvas.draw_circle(self.ptCurrentPos._tGetXY(),
                            self.iRadius, 1, self.sColor,self.sColor)
        return

class RestrictedBallClass(BallClass):
    def __init__(self, iX, iY, iYMin, iYMax):
        BallClass.__init__(self,iX,iY)
        self.iUpperBoundary = iYMin + self.iRadius
        self.iLowerBoundary = iYMax - self.iRadius
        return self
    
    def _tNextPos(self):
        tPos = self.ptCurrentPos._tGetXY()
        tVel = self.vVelocity._tfGetXY()
        if tPos[1] + tVel[1] > self.iLowerBoundary:
            self._SetPos(tPos[0]+tVel[0], self.iLowerBoundary)
            self.vVelocity._BounceY()
        if tPos[1] + tVel[1] < self.iUpperBoundary:
            self._SetPos(tPos[0]+tVel[0], self.iUpperBoundary)
            self.vVelocity._BounceY()
        self.ptCurrentPos._tMove(self.vVelocity)
        return
    
    def _BounceX(self):
        self.vVelocity._BounceX()
        return

    def _bTouchVerticalLine(self, iLineX):
        iMyX = tPos = self.ptCurrentPos._iX()
        return ( abs(iMyX - iLineX) <= self.iRadius )
        return
    
    def _Accelerate(self):
        self.vVelocity._Mult_By_Number(1.1)
        return
    
class PaddleClass:
    """ A paddle (left or rigtht) """
    def __init__(self, bLeft=True):
        self.bLeft=bLeft
        self.bRight=not self.bLeft
        self.iHeight=aPaddleHeight()
        self.iWidth=aPaddleWidth()
        self.iHalfWidth=self.iWidth/2
        self.iHalfHeight=self.iHeight/2
        self.tPos=None  # need to be set later
        self.vVelocity=VectorClass(0,0)
        self.sColor = asPaddleColor()
        # Not the best method, I prefer to use parameters for this
        self.iMaxY = aTableHeigth() - self.iHalfHeight
        return
    
    def _SetPos(self,iX,iY):
        # for left paddle, iX = 0, for rigth paddle, iX = width of table
        self.tPos = PositionClass(iX, iY)
        if self.bLeft:
            iXCoord = (iX + self.iHalfWidth)
        else:
            iXCoord = (iX - self.iHalfWidth)
        self.ptUpper= ( iXCoord, (self.tPos._iY() - self.iHalfHeight) )
        self.ptLower=( iXCoord, (self.ptUpper[1] + self.iHeight) )
        # if not self.bLeft: print ("*DBG* Right Paddle position: " + str(self.tPos) )
        return
    
    def _Draw(self,oCanvas):
        # update position, if in canvas
        fNewY = self.tPos._iY() + self.vVelocity._fY()
        if fNewY >= self.iMaxY:
            # collision of paddle with lower border
            self._SetPos(self.tPos._iX(), self.iMaxY)
            self.vVelocity._Set(0,0)
        elif fNewY < self.iHalfHeight:
            # collision of paddle with upper border
            self._SetPos(self.tPos._iX(), self.iHalfHeight)
            self.vVelocity._Set(0,0)
        else:
            self._SetPos(self.tPos._iX(), fNewY)
        # draw paddle
        oCanvas.draw_line(self.ptUpper, self.ptLower, self.iWidth, self.sColor)
        return
    
    def _Up(self):
        """Move up or stop (if moved down)"""
        self.vVelocity._IncrY(-5)
        return
        
    def _Down(self):
        self.vVelocity._IncrY(5)
        return
    
    def _Stop(self):
        self.vVelocity._Set(0,0)
        return
    
    def _bCollideBall(self,oBall):
        """if the ball collides with the paddle"""
        bBallBounced = False
        iBallYPos = oBall._oWhere()._iY()
        iPaddleCenter=self.tPos._iY()
        if abs(iBallYPos - iPaddleCenter) <= self.iHalfHeight:
            # ball is bounced back
            oBall._BounceX()
            oBall._Accelerate()
            bBallBounced = True
        return bBallBounced

class TableClass:
    def __init__(self):
        self.iWidth=aTableWidth()
        self.iHeight=aTableHeigth()
        self.lScore = [0,0]
        self.oBall = RestrictedBallClass(self.iWidth/2, self.iHeight/2, 0, self.iHeight)
        self.oLeftPaddle = PaddleClass(bLeft=True)
        self.oLeftPaddle._SetPos(0, self.iHeight/2)
        self.oRightPaddle = PaddleClass(bLeft=False)
        self.oRightPaddle._SetPos(self.iWidth, self.iHeight/2)
        self.oFrame = simplegui.create_frame(asFrameName(), 
                                             self.iWidth, self.iHeight,
                                            aiControlAreaWidth())
        self.oFrame.set_draw_handler(self._Draw)
        self.oFrame.add_button("New game", self._NewGame, aiButtonWidth() )
        self.iScoreYPos=self.iHeight - (self.iHeight - aiScoreFontSize())/2
        self.iNumberWidth=self.oFrame.get_canvas_textwidth("0", aiScoreFontSize(), 
                                                      asScoreFontFace())
        self.iLeftScoreXPos=(self.iWidth/2 - self.iNumberWidth)/2
        self.iRightScoreXPos=self.iWidth/2 + self.iLeftScoreXPos
        return

    def _Draw(self,oCanvas):
        """Draw a table and everything on it"""
        # dividing line (half-width)
        oCanvas.draw_line((self.iWidth/ 2, 0), 
                         (self.iWidth/2, self.iHeight), 1, 
                         asDividingLineColor())
        # score zone lines
        oCanvas.draw_line((aPaddleWidth(), 0), (aPaddleWidth(), self.iHeight),
                         1, asDividingLineColor())
        oCanvas.draw_line((self.iWidth - aPaddleWidth(), 0), 
                          (self.iWidth - aPaddleWidth(), self.iHeight),
                         1, asDividingLineColor())
        # Upper and lower boundaries
        oCanvas.draw_line((0,0), (self.iWidth,0), 2, "Red")
        oCanvas.draw_line((0,self.iHeight), (self.iWidth,self.iHeight), 2, "Red")
        # Draw current score
        oCanvas.draw_text(str(self.lScore[0]),(self.iLeftScoreXPos,self.iScoreYPos), 
                          aiScoreFontSize(), asScoreColor(), asScoreFontFace())
        oCanvas.draw_text(str(self.lScore[1]),(self.iRightScoreXPos,self.iScoreYPos), 
                          aiScoreFontSize(), asScoreColor(), asScoreFontFace())
        # Draw the objects on table: paddles and ball
        self.oLeftPaddle._Draw(oCanvas)
        self.oRightPaddle._Draw(oCanvas)
        self.oBall._Draw(oCanvas)
        # if the ball touch left/right lines:
        if self.oBall._bTouchVerticalLine(aPaddleWidth()):
            # ball is on the left score zone
            if self.oLeftPaddle._bCollideBall(self.oBall):
                pass
            else:
                 # increase score, new game
                # self.oBall._BounceX()
                self.lScore[1] += 1
                self._FaceOff("right")
        elif self.oBall._bTouchVerticalLine(self.iWidth - aPaddleWidth()):
            if self.oRightPaddle._bCollideBall(self.oBall):
                pass
            else:
                # increase score, new game
                self.lScore[0] += 1
                self._FaceOff("left")
        return
    
    def _KeyDnHandler(self,iKey):
        if iKey == simplegui.KEY_MAP["up"]:
            self.oRightPaddle._Up()
        elif iKey == simplegui.KEY_MAP["down"]:
            self.oRightPaddle._Down()
        if iKey == simplegui.KEY_MAP["w"]:
            self.oLeftPaddle._Up()
        elif iKey == simplegui.KEY_MAP["s"]:
            self.oLeftPaddle._Down()
        return
    
    def _KeyUpHandler(self,iKey):
        if iKey == simplegui.KEY_MAP["up"]:
            self.oRightPaddle._Stop()
        elif iKey == simplegui.KEY_MAP["down"]:
            self.oRightPaddle._Stop()
        if iKey == simplegui.KEY_MAP["w"]:
            self.oLeftPaddle._Stop()
        elif iKey == simplegui.KEY_MAP["s"]:
            self.oLeftPaddle._Stop()
        return
    
    def _Start(self):
        self.oFrame.set_keydown_handler(self._KeyDnHandler)
        self.oFrame.set_keyup_handler(self._KeyUpHandler)
        self.oFrame.start()
        return

    def _FaceOff(self,sDirection):
        self.oBall._SetPos(self.iWidth/2, self.iHeight/2)
        self.oBall._SetSpeed(0,0)        
        self.oBall._Launch(sDirection)
        
    def _NewGame(self):
        self.lScore[0] = 0 ; self.lScore[1] = 0
        sDirection = random.choice(("left","right"))
        self._FaceOff(sDirection)
        return

# initialize globals - pos and vel encode vertical info for paddles
# Moved to Table class WIDTH = 600
#                      HEIGHT = 400       
# Moved to Ball class BALL_RADIUS = 20
# Moved to Paddle class PAD_WIDTH = 8; PAD_HEIGHT = 80
# moved to Paddle class HALF_PAD_WIDTH = PAD_WIDTH / 2, HALF_PAD_HEIGHT = PAD_HEIGHT / 2
# LEFT = False
# RIGHT = True

# Moved to Ball class
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
# def spawn_ball(direction):
#     global ball_pos, ball_vel # these are vectors stored as lists


# define event handlers
# def new_game():   <--- moved to TableClass
#     global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
#     global score1, score2  # these are ints

# def draw(canvas): <--- moved to TableClass
#    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    # canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    # canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    # canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
            
    # draw ball
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
# Moved to PaddleClass def keydown(key):
   
# Moved to PaddleClass def keyup(key): 



oTable = TableClass()
# # create frame
# frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
# frame.set_draw_handler(draw)
# frame.set_keydown_handler(keydown)
# frame.set_keyup_handler(keyup)


# start frame
# new_game()
oTable._Start()
