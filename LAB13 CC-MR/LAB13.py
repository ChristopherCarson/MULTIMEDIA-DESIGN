
#Problem 1
def madLib():
  article = """As the fallout continues following Matt Lauer's firing from NBC News, insiders at the network are coming forward with more details about what led to Lauer's termination and the speculation running rampant inside 30 Rock.
Before a NBC staffer filed an official complaint on Monday, executives at NBC had reportedly been hearing rumors about stories being reported for Variety and New York Times and asked Lauer if there was anything that he thought we should know or could fit into this category, and he adamantly denied that there was, Vanity Fair's Sarah Ellison reports.
The outlet cites a person familiar with [the former staffer's] complaint who alleges that she didn't use the words rape or assault in her official complaint to NBC's HR department."""

  wordsToReplace = ["Matt Lauer", "NBC News", "network", "Lauer's termination", "speculation", "30 Rock", "NBC staffer", "complaint", "NBC", "Variety and New York Times", "Lauer", "category", "Sarah Ellison", "[the former staffer's] complaint", "rape", "assault", "NBC's HR department"]
  wordDescriptions = ["person", "place", "thing", "thing", "idea", "place", "job", "thing", "business", "noun", "name", "noun", "name", "item", "random word", "another random word", "place"]
  #wordDescriptions = ["person", "place", "thing", "thing"]
  
  newWords = []
  
  for d in wordDescriptions:
    word = requestString("Please enter a "+d)
    newWords.append(word)
    
  for x in range (0, len(newWords)):
    article = article.replace(wordsToReplace[x], newWords[x])

  showInformation(article)