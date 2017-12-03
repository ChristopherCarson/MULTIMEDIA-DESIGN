#CST 205 John Coffelt, Raul Ramirez
#Lab13 Lists Problem 1: Mad Libs

#Fun game where grab an article, replace some words and output it as a new and "improved" article.
def madLibs():
  #Article that says cats aren't as smart as dogs.
  newsA = """You know that age-old debate about whether dogs are smarter than cats? Well, science now has a definitive answer. It's dogs. That's the conclusion of an international 
  team of researchers, who found that dogs possess twice the number of neurons than cats. Neurons are cells that process information. And so, the more neurons an animal has, the better 
  its information processing capability, these scientists say. The study was conducted by researchers from six universities in the US, Brazil, Denmark and South Africa. It's been 
  accepted for publication in the journal Frontiers in Neuroanatomy."""
  
  replaced = ["dogs","cats","neurons","Neurons","neurons","cells","information","Neuroanatomy"]#list of the words that will be replaced by the user
  
  userWords = ["animals", "animals","things","things","things","random word","random word","fake science"]#list of what the user will be prompted to think about for new words

  libs = []#list that stores user words
  
  showInformation("This is Madlibs and the point of the game is to use zany words to help tell a story or make a news article funny. Try it out!")
  
  for x in userWords:
    w = requestString("Enter some "+ x)#asks the user to enter a new word that is prompted
    libs.append(w)#adds a new element to the end of the new list of words
    
  for y in range (0, len(libs)):
    newsA = newsA.replace(replaced[y], libs[y])#takes the new words and puts them into the old words, then replaces thos words in the article

  printNow(newsA)#displays the updated article...madlibs style
  