#Lab 15 CST205 Christopher Carson, Raul Ramirez
#get python to print out month we were born 
#get python to print days until next birth day
#get python to print day of the week the Declaration was ratified.
import datetime
import calendar

showInformation("First we need to get your birthdate.")
y = int(requestString("Input the year you were born as a number: "))
m = int(requestString("Input the month you were born as a number: "))
d = int(requestString("Input the day you were born as a number: "))

#Print a calendar of the month you were born
print(calendar.month(y, m))

#Print the number of days until your next birthday
today = datetime.date.today()
if datetime.date(today.year,m,d) < today:
  diff = datetime.date(today.year+1,m,d) - today
  print("There are %s days until your next birthday.") % (diff.days)
else:
  diff = datetime.date(today.year,m,d) - today
  print("There are %s days until your next birthday.") % (diff.days)

#Print the name of the weekday Congress ratified Dec. of Ind.
date = datetime.date(1776, 7, 4)
print("The Declaration of Independence was ratified by Congress on a %s." )% (calendar.day_name[date.weekday()])
