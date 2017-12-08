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

def olderDate():
  from datetime import datetime

  mDt = datetime(1900,01,01)
  dt = datetime.strptime('20-02-1899', "%d-%m-%Y")
  resultString = datetime(dt.year + (mDt - dt).days/365 + 
  1, dt.month, dt.day).strftime('%B %d, %Y').replace('1900', str(dt.year))
  print resultString