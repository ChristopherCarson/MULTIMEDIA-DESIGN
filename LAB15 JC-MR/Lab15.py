#Lab 15
import calendar
import datetime
#Partner: John Coffelt, Michael Rose

#Problem 1

#Problem 2
#Rolls a "dice". Takes the amount of sides a dice has and then rolls a random number and returns it.
def roll_dice(num_sides):
  import random
  return random.randint(1,num_sides)

#Set up variables.    
sides = 6
point = 0

#Set up conditional booleans.
first_roll = true
win = false
game_over = false
print "Welcome to Craps!"
while not game_over:
  raw_input("Enter any key to roll: ")
  roll = roll_dice(sides) + roll_dice(sides)
  print "You roll: " + str(roll)
  
  #Determine if the game is over based on the result of the roll.
  if first_roll and roll in [7,11]:
    win = true
    game_over = true
  elif first_roll and roll in [2,3,12]:
    game_over = true 
  elif first_roll and roll in [4,5,6,8,9,10]:
    point = roll
  elif roll == point:
    win = true
    game_over = true
  elif roll == 7:
    game_over = true
    
  if first_roll: first_roll = false
  
if win:
  print "Congratulations! You won!"
else:
  print "Sorry! You lost!"
  
#This function takes a year and a month and prints out the calendar for the month in that year.
#Use a monospaced font to remove formatting issues
def birthMonth(year, month):
  #The month function in calendar prints out a calendar of that month in that year.
  print calendar.month(year, month)


#This function takes the year month and day of your next birthday and tells you how many days until your birthday.
def howLong(year, month, day):
  #saves the parameters as a date item
  birthday = datetime.date(year, month, day)
  #datetime.date.today() is a date item with todays year, month, and day.  .days returns just the days part
  #then the difference is printed and forced to type string to allow concatenation
  print "There are " + str((birthday - datetime.date.today()).days) + " days until your birthday."

#This function tells you when the Declaration of Independence was ratified. It takes no parameters.
def ratified():
  #Take the day the Declaration of Independence was ratified and store it in a date object.
  day = datetime.date(1776, 7, 4)
  #calendar.day_name[int] takes a number from 0 to 7 and prints out a day of the week with Monday = 0
  #day.weekday returns a number from 0 to 7 based on what day of the week it was with Monday = 0
  print "The Declaration of Independence was ratified on a " + calendar.day_name[day.weekday()]
