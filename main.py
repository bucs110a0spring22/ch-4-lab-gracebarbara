import turtle
import math 
import datetime
from datetime import date

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(myturtle=None):
	myturtle.up()
	myturtle.goto(-360, 0)
	myturtle.down()
	for x_coord in range(-360, 361):
		y_coord = math.sin(math.radians(x_coord))
		myturtle.goto(x_coord, y_coord)

def setupWindow(mywindow=None):
	mywindow.bgcolor('lightblue')
	mywindow.setworldcoordinates(-360, -1, 360, 1)

def setupAxis(myturtle=None):
	myturtle.speed(1)
	myturtle.up()
	myturtle.goto(-360, 0)
	myturtle.down()
	myturtle.goto(360, 0)
	myturtle.up()
	myturtle.goto(0, -1)
	myturtle.down()
	myturtle.goto(0, 1)

def drawCosineCurve(myturtle=None):
	myturtle.up()
	myturtle.goto(-360,1)
	myturtle.down()
	for x_coord in range(-360, 361):
		y_coord = math.cos(math.radians(x_coord))
		myturtle.goto(x_coord, y_coord)

def drawTangentCurve(myturtle=None):
	myturtle.up()
	myturtle.goto(-360,0)
	myturtle.down()
	for x_coord in range(-360, 361):
		y_coord = math.tan(math.radians(x_coord))
		myturtle.goto(x_coord, y_coord)

def zodiacGenerator():
	print("Welcome to the Astrological Sign Generator!")
	day = int(input("What is your birthday? (1-31): " ))
	month = int(input("What is your birth month? (1-12): "))
	if month == 1:
		if day<20:
			zodiacsign = 'Capricorn'
		else:
			zodiacsign = "Aquarius"
	elif month == 2:
		if day<19:
			zodiacsign = 'Aquarius'
		else:
			zodiacsign = 'Pisces'
	elif month == 3:
		if day<21:
			zodiacsign = 'Pisces'
		else:
			zodiacsign = 'Aries'
	elif month == 4:
		if day<19:
			zodiacsign = 'Aries'
		else:
			zodiacsign = 'Taurus'
	elif month == 5:
		if day<20:
			zodiacsign = 'Taurus'
		else:
			zodiacsign = 'Gemini'
	elif month == 6:
		if day<20:
			zodiacsign = 'Gemini'
		else:
			zodiacsign = 'Cancer'
	elif month == 7:
		if day<22:
			zodiacsign = 'Cancer'
		else:
			zodiacsign = 'Leo'
	elif month == 8:
		if day<22:
			zodiacsign = 'Leo'
		else:
			zodiacsign = 'Virgo'
	elif month == 9:
		if day<22:
			zodiacsign = 'Virgo'
		else:
			zodiacsign = 'Libra'
	elif month == 10:
		if day<22:
			zodiacsign = 'Libra'
		else:
			zodiacsign = 'Scorpio'
	elif month == 11:
		if day<21:
			zodiacsign = 'Scorpio'
		else:
			zodiacsign = 'Sagittarius'
	elif month == 12:
		if day<21:
			zodiacsign = 'Sagittarius'
		else:
			zodiacsign = 'Scorpio'
	print("Your Astrological Sign is: ", zodiacsign)
	return zodiacsign

def inputBirthday():
	day = int(input("What is your birthday? (1-31): " ))
	month = int(input("What is your birth month? (1-12): "))
	year = int(input("What year were you born?: "))
	birthday = date(year, month, day)
	return birthday

def daysUntilBirthday(birthday_date=0, current_date=0):
	birthday_hasnt_passed = date(current_date.year, birthday_date.month, birthday_date.day)
	birthday_has_passed = date(current_date.year+1, birthday_date.month, birthday_date.day)
	if birthday_hasnt_passed > current_date:
		days = (birthday_hasnt_passed - current_date).days
		return days
	else:
		days = (birthday_has_passed - current_date).days
		return days

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

		#AstrologicalGenerator
		zodiacGenerator()
		print("Now we will calculate how many days there are until your next birthday!")
		birthday_date = inputBirthday()
		current_date = date.today()
		days = daysUntilBirthday(birthday_date, current_date)
		print("There are", days,"days until your birthday!")
		
main()
