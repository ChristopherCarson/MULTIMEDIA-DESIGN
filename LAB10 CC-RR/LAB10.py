#CST205 Chris Carson and Raul Ramirez LAB 10

#Warm Up PART A: Try out the new requestString() function. 
#In JES, type the following command
#name = requestString("What is your name?")
#Now print the value of the variable name.
def warmUp():
  name = requestString("What is your name?")
  print name.title()#makes any name input capitalized in the first letter 
  #PART B: Write a while loop that continually asks the user to 
  #enter a word (using request string).The loop should keep 
  #going until the user enters the word "stop". 
  while(name.lower() != "stop"):#will make any input lower case       
    print name.title()
    name = requestString("type stop to end loop")