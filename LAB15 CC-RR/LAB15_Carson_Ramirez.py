#CST 205 lab15 problem 1 Christopher Carson, Raul Ramirez  
from random import randint

end = false #global variable

def roll():#rolls two dice
  dice = randint(1,6)+randint(1,6)#adds random dice values
  print(dice)
  return dice
  
def craps():
  wannaPlay = requestString("This is craps, if your first roll is " + 
  "7 or 11 you win. If it's 2, 3 or 12 you lose. You keep rolling " +
  "until you get the same number and win or roll a 7 and lose.\n" +
  " Type y/n to play")
  if wannaPlay.upper() == "Y":
    #dice are rolled until point is rolled twice for win or roll 7 for lose. 
    while True:    
      firstR = roll()#first roll
      if firstR in (2,3,12):#If first roll is 2,3,12 then lose!
        print "You Lose!"
        break;
      elif firstR in (7,11):#if first roll is a 7 or 11 then win!
        print "You Win!"
        break;
      secondR = roll()#send roll if first roll isn't a win
      if secondR == firstR:#this would be point being rolled twice
        print "You Win!"
        break;
      if secondR == 7:
        print "You Lose!"
        break;
  elif wannaPlay.upper() == "N":
    showInformation("Ok go play something else then.")
  else:
    showInformation("Wrong Entry.")
    
          