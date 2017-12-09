#CST 205 LAB16 Raul Ramirez, Chris Carson
import os #lets us use open module with jython
import urllib


def makePage():
  dir = os.path.dirname(__file__)#uses the parent folder of the program
  path = dir + "\\"+"NEW_MOVIES.html"#looks for test.html in the parent directory
  #replace the directory in the line below with the path to your file
  file = open(path, "wt")
  
  #opener = urllib.FancyURLopener({})  
  f = urllib.urlopen("http://www.imdb.com/movies-coming-soon/")
  text = f.read()#Read text from website
  
  start = 0
  movies = []#Create an array to hold movie titles
  
  while start != -1:
    start = text.find("http://schema.org/Movie")#find key text
    text = text[start+20:]#cut the html info to the key
    end = text.find("src=")#find the next key piece of html
    str = text[:end]#Trim a substring to this length
    start = text.find("title=")#Find the title
    m = str[start+6:]#Trim another substring to the title
    m = m[1:len(m)-2]#Remove the quotes around the title
    movies.append(m)#Add title to array
  
  stringList = "<h1>TOP NEW MOVIES COMING OUT SOON!</h1>"
  for m in range(0,10):
    stringList = stringList + "<h1>"
    stringList = stringList + movies[m]
    stringList = stringList + "</h1>"
   
  #Write html code to file, including the top 10 movies scraped from IMDB
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  <html>
  <head><title>New Movies</title>
  </head>
  <body>"""+stringList+"""
  </body>
  </html>""")
  
  file.close()
  
  