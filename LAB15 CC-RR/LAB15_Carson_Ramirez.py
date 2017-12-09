#CST 205 lab15 problem 1 Christopher Carson, Raul Ramirez  
from random import randint

def roll():#rolls one dice
  diceGraphics = ['[ . ]', '[ : ]', '[ .:]','[ ::]','[.::]','[:::]']
  dice = randint(1,6)
  print(diceGraphics[dice-1])
  return dice
  
def craps():
  end = false
  wannaPlay = requestString("This is craps, if your first roll is " + 
  "7 or 11 you win.\n If it's 2, 3 or 12 you lose.\n Any other number is your point number.\n You keep rolling " +
  "until you get the point again and win or roll a 7 and lose.\n\n" +
  " Type y/n to play")
  if wannaPlay.upper() == "Y":
    #First Roll
    count = roll()
    count += roll()
    point = count
    
    print "You rolled %s." % (count)
    if count in (2,3,12):#If first roll is 2,3,12 then lose!
      print "You Lose!"
      end = true
    elif count in (7,11):#if first roll is a 7 or 11 then win!
      print "You Win!"
      end = true

    while end == false:
      print "You roll again..."
      count = roll()
      count += roll()
      if count == point:
        print "You rolled your point again! You win!"
        end = true
      elif count == 7:
        print "You loose!"
        end = true

  elif wannaPlay.upper() == "N":
    showInformation("Ok go play something else then.")
  else:
    showInformation("Wrong Entry.")
    
          