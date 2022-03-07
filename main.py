import turtle
import math 

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(dart):
  for x in range(-360, 360):
    y = math.sin(math.radians(x))
    dart.goto(x, y)
  return dart

def setupWindow(mywindow=None):
  wn = turtle.Screen()
  wn.bgcolor('lightblue')
  wn.setworldcoordinates(-360, -1, 360, 1)

def setupAxis(myturtle=None):
  dart = turtle.Turtle()
  dart.speed(1)
  dart.backward(360)
  dart.forward(720)
  dart.backward(360)
  dart.left(90)
  dart.forward(1)
  dart.backward(2)
  dart.forward(1)
  dart.left(90)
  dart.forward(360)
  return dart

def drawCosineCurve(dart):
  dart.up()
  dart.goto(-360,1)
  dart.down()
  for x in range(-360, 360):
    y = math.cos(math.radians(x))
    dart.goto(x, y)
  return dart

def drawTangentCurve(dart):
  dart.up()
  dart.goto(-360,0)
  dart.down()
  for x in range(-360, 360):
    y = math.tan(math.radians(x))
    dart.goto(x, y)
  return dart
  
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
