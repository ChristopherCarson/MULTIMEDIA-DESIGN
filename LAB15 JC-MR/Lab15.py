#Lab 15
import calendar
import datetime
#Note the lab name and partner name have to be formatted as stated in the assignment.  I would delete this comment after formatting it.
#Partner: 

#Problem 2

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