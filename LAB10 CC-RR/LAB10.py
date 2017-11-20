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
  print ("Welcome to Hang Man!")
  print ("The object of the game is to figure out a word by guessing characters.")
  print ("Each time you guess a character that is not in the word, the hangman gets another body part.")
  print ("If your hangman has a full body, you loose.")
  print ("Your clue to the length of the word are the amount of dashes. Each dash represents an unguessed character.")
  print "Good luck!"
  
  word = "CALIFORNIA" #This is the secret word that needs to be guessed
  numberOfWrong = 0 #Variable for the number of incorrect guesses
  won = 0 #This is a flag to determine if player has won. If set to 1, player wins
  wrongGuesses = "" #word to store incorrect guesses
  newChar = 0 #A flag to determine if the guess is a letter that has already been guessed
  
  #This sets the word that prints the amount of dashes for the length of the word
  printWord = ""
  for chars in word:
    printWord = printWord + "_ "

  #Main while loop
  while numberOfWrong < 6 and won == 0:
    rightFlag = 0
    newChar = 1
    
    print printWord
    print "Your incorrect guesses are: %s" % (wrongGuesses)
      
    char = requestString("Enter a character.")
    char = char.upper()
    
    #Here we check to see if the letter was already guessed
    for q in range (len(printWord)):
      if char == printWord[q]:
        newChar = 0
    for v in range (len(wrongGuesses)):
      if char == wrongGuesses[v]:
        newChar = 0
    
    if newChar == 0:
      print "You've already guessed the letter %s, please choose a new letter." % (char)
      rightFlag = 1 #If the letter was already guessed, we set the rightFlag so it doesn't count as an incorrect guess

    if char.isalpha() and len(char) == 1: #This checks to make sure the user is only entering one character
      
      newWord = "" #This word is a temporary word used to recreate the printWord
      
      #In this loop we check to see if the user guessed a character that's in the secret word
      for x in range (len(word)):
        if char == word[x]:
          newWord = newWord + char + " "
          rightFlag = 1 #This flag is used to determin if the user guessed a wrong character. If flag is never set to 1, we know they guessed right
        else:
          newWord = newWord + printWord[x*2] + " "
          
      printWord = newWord #swaps the temporary word for the printWord
      
    else:
      print "Please enter only a character."
      rightFlag = 1 #Set the flag so an incorrect entry doesn't get tracked as a wrong guess.
      
    #If the guess is incorrect, print the following letting the play know how many guesses they have left.
    if rightFlag == 0:
      numberOfWrong += 1
      wrongGuesses = wrongGuesses + char + " "
      print "Incorrect guess."
      print "You have %d guesses remaining." % (6-numberOfWrong)
      if numberOfWrong == 6: #If guesses = 6, then the player looses.
        print "Sorry, you loose!"
    
    #Here, we set the won flag to 1, then test. If there are any dashes left, we reset the flag to 0.
    won = 1
    for w in range (len(printWord)):
      if printWord[w] == "_":
        won = 0
        
    if won == 1: #If flag remains set, play has won.
      print "Congrats! You've won!"
    else:
      won = 0
  
 