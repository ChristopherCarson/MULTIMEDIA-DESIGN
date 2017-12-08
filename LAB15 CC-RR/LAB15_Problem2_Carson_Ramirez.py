#Lab 15 CST205 Christopher Carson, Raul Ramirez
#get python to print out month we were born 
#get python to print days until next birth day
#get python to print day of the week the Declaration was ratified.
import datetime

mydate = datetime.date(1989,02,24)#prints out month I was born
print(mydate.strftime("%B"))#formats it to the month

today = datetime.date.today()#takes today
next = datetime.date(2018,02,24)#takes birthday
diff = next - today#calculates how many days
print diff.days
