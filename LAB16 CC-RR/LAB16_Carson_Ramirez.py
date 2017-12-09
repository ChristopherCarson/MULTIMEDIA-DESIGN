#CST 205 LAB14 Raul Ramirez
import os #lets us use open module because jython

def makePage():
  dir = os.path.dirname(__file__)#uses the parent folder of the program
  path = dir + "\\"+"test.html"#looks for eggs.txt in the parent directory
  #replace the directory in the line below with the path to your file
  file = open(path, "wt")
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <h1>MY PYTHON PAGE!!!</h1>
  </body>
  </html>""")
  
  file.close()