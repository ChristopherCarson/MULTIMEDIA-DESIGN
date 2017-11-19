#Lab 10 - CST 205
#John Coffelt, Michael Rose
import random

#Warm Up
def whileTest():
  word = requestString("Enter a word. Enter 'stop' to stop.")
  while(word != "stop"):
    print word
    word = requestString("Enter a word. Enter 'stop' to stop.")

#Problem 1: Call this function to start the hangman game
def hangman():
#Things to do:
#Add more words to list
#remove duplicate code for correct and incorrect (new function)
#make more efficient possibly
  words = "fringe foul grinder locust promised antique spell front sissy feign carrion alphabet sideshow picnic infinite hoax natural wealthy friend pattern ink sprites parade volcanic cast".split() #words separated with a space
  wordIndex = random.randint(0, len(words)-1) #pick a random number
  print "Welcome to hangman.\n The rules are simple.\nA blank word will show up and you have to guess it by picking letters in the word!"
  print "If you guess incorrectly 6 times, you lose.\nIf you guess the word before that, you win!\nON WITH THE SHOW!!!!\n"
  word = words[wordIndex] #pick a random word from the word list
  iguess = '' #incorrect guess array
  cguess = '' #correct guess array
  bword = list('_ '*len(word)) #blank word list
  wrong = 0  #wrong guesses
  foundAll = False
  
  while(wrong != 6 and (not foundAll)):
    guess = requestString("Enter a letter!")
    guess = guess.lower()
    if len(guess) != 1 or not guess.isalpha():#check for a single letter
      print "Please enter only one letter."
    elif guess in iguess or guess in cguess:#already guessed
      print "You guessed '%s' already. Enter another letter." % (guess)
    elif guess in word:#correct letter
      print "Correct!"
      cguess = cguess + guess #add the correct guess to the correct guess array
      foundAll = True #set this to true for checking purposes
      for i in range(len(word)): #go through the word
        if word[i] not in cguess: #if the current isn't in the guesses, return false and break
          foundAll = False
          break
      if foundAll:#if foundAll is still true then you've found all the letters and must break
        break
      print "Word so far:"
      for x in range(len(word)): #replaces the blank space in bword with the letter
        if word[x] in cguess:
          bword[x*2] = word[x]
      print "".join(bword) #removes the list formatting of bword
      print "Incorrect guesses:"
      print iguess
      print "You have used %d of 6 incorrect guesses." % (wrong)
    elif guess not in word:#wrong letter
      print "Incorrect!"
      wrong = wrong + 1 #increment wrong counter
      iguess = iguess + guess #add to list of incorrect guesses
      print "Word so far:"
      for x in range(len(word)): #replaces the blank space in bword with the letter
        if word[x] in cguess:
          bword[x*2] = word[x]
      print "".join(bword) #removes the list formatting of bword
      print "Incorrect guesses:"
      print iguess
      print "You have used %d of 6 incorrect guesses." % (wrong)
    
  #check to see if you won or not
  if(wrong == 6):#lose condition
    print "Sorry! You lose! Better luck next time."
  else: #win condition
    print "You got the whole word!!!"
    print "Word so far:"
    for x in range(len(word)):
      if word[x] in cguess:
        bword[x*2] = word[x]
    print "".join(bword)
    print "Incorrect guesses:"
    print iguess
    print "You have used %d of 6 incorrect guesses." % (wrong)