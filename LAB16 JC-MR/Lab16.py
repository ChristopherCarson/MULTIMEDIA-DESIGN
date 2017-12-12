#Lab 16
#Partner: John Coffelt, Michael Rose
import urllib

#Sample Function
def makePage(filename):
  dir = os.path.dirname(__file__)#uses the parent folder of the program
  path = dir + "\\" + filename + ".html"
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
 
#Creates a website that lists the headlines on CNN.com. Input: the name of the html file to be created. 
def getCNNHeadlinesSite(new_site_name):
  dir = os.path.dirname(__file__)#uses the parent folder of the program
  
  #Create the start to the HTML page
  html = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>CNN Headlines</title>
  </head>
  <body>
  <h1>CNN Headlines:</h1>"""
  
  #Open CNN site and get the HTML.
  cnn_site = urllib.urlopen("http://www.cnn.com")
  cnn_text = cnn_site.read()
  
  #Turn each headline into single lines of html.
  headlines = cnn_text.split('"headline":"')
  headlines = headlines[2:]
  for headline in headlines:
    headline = headline[0:headline.find('",')]
    headline = headline.replace('\u003c','')
    headline = headline.replace('strong>','')
    headline = headline.replace('/','')
    html += "\n<text>" + headline + "</text><br>"
  
  #Finish the HTML page.
  html += """\n</body>
          </html>"""
  
  #Write the new page.
  new_site_path = dir + "\\" + new_site_name + ".html"
  new_site = open(new_site_path, "wt")
  new_site.write(html)
  
  #Close everything.
  cnn_site.close()
  new_site.close()
  
