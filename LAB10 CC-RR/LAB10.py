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
    
#Hangman: 1.Output a brief description of the game of hangman and how to play
def hangman():
  print ("Guess a letter in a word correctly and it appears, you win!")
  print ("Guess wrong and you slowly get HANGMAN, you lose!")
  print ("Your clue is the number of dashes to guess")
  print ("Correct guesses don't count against your 6 tries")
  
#2.The word to guess can be hard-coded in your program, but it should be easy to 
#change the word; a list of words

#3.Output the appropriate number of dashes and spaces to represent the phrase 

#4.Continuously read guesses of a letter from the user and fill in the corresponding blanks 
#report that the user has made an incorrect guess if not in the current word
#The user MUST enter letters - if the user enters anything that is not a letter, you 
#should print an error message and reprompt for input. Your program should handle input 
#either as uppercase or lowercase letters

#5.Each turn you will display the phrase as dashes but with any already guessed letters 
#filled in, as well as which letters have been incorrectly guessed so far and how many 
#guesses the user has remaining.

#6.You MUST use at least 3 string methods or operators in a useful manner 
 
