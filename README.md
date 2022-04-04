#### CS 110
# Midterm - Python Programming

***

_Replace anything surrounded by the `< >` symbols._

## SUMMARY:
What did you clean up?: Firstly, I changed all of the parameters of my functions to be named with default values. I improved on the dryness of my code by removing unnecessary return statements and by setting each of my parameters to default values I was able to remove unnecessary creation of variables for turtles and screens. Within the drawAxis function, though not necessarily more condensed(it is the same amount of lines), I made the code more readable and easier to follow. I made sure to make all of my variables not have single letter variable names. And finally, I fixed the parameters of the range within my for loops making them (360, 361) since the second value (361) is exclusive. 

Summary of function(s) added: The first function I added (zodiacGenerator) takes the users input birthday and, using a for loop, determines their zodiac sign. The second function that I added (inputBirthday) asks for the users birthday, turns it into a number that is able to be used with the datetime module, and returns that value. The next function (daysUntilBirthday) is a function that can calculate the days between the input birthday and the current date. Using a for loop it determines if the date has already passed or not and then subtracts that value from the current date as necessary. The parameters on this function require a call to the inputBirthday function and the current date using the datetime module which I learned how to navigate using python docs. Each of these functions are then called to in the main function in order to run.

Summary of Feature Added: In summation, I added two separate features that require three functions in total. The first feature determines the users zodiac sign and the second feature takes the users birthday and the current date and determines the amount of days until their next birthday. 

## KNOWN BUGS AND INCOMPLETE PARTS:
 None

## REFERENCES:
 https://docs.python.org/3/library/datetime.html?highlight=date#datetime.date 
 https://pythontic.com/datetime/datetime/date
 https://realpython.com/python-datetime/

## MISCELLANEOUS COMMENTS:
 None
