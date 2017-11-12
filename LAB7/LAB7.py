
  
def test():
  setMediaFolder()
  pathTest = getMediaPath("TEST.jpg")
  pic = makePicture(pathTest)
  pathBack = getMediaPath("back.jpg")
  back = makePicture(pathBack)
  
  card = turkeyfi(pic, back, 200, 150)  
  repaint(card)
  
def turkeyfi(pic, back, targetX, targetY):
  card = makeEmptyPicture(800, 600)
  pic = shrinkPic(createTurkey(pic),3)
  pyCopy(back, card, 1, 1)
  chromakey(card, pic, targetX, targetX)
  return card
  
  
#Problem 3 
# Function that replaces all of the green pixels in an image with pixels forma background image
# The user must first select the BACKGROUND image, then the GREEN SCREEN image.
# With this code,the BACKGROUND must be larger than the GREEN SCREEN image.
def chromakey(background, green_pic, targetX, targetY):
  new_y = targetY
  for y in range (0,getHeight(green_pic)):
      new_y += 1
      new_x = targetX
      for x in range (0, getWidth(green_pic)):
        new_x += 1
        original=getPixel(green_pic, x, y)
        new=getPixel(background, new_x, new_y)
        color=getColor(original)
        if getRed(original) > (getGreen(original) - 30) or getBlue(original) > (getGreen(original) - 30):
          setColor(new, color)
  return green_pic

def shrinkPic(pic, int):
  width = getWidth(pic)
  height = getHeight(pic)
  
  copy = makeEmptyPicture(width/int, height/int)
  new_y = -1
  
  for y in range (0,height,int):
    if new_y < getHeight(copy)-1:
      new_y = new_y + 1
      new_x = -1
    for x in range (0, width,int):
      if new_x < getWidth(copy)-1:
        new_x = new_x + 1
      original=getPixel(pic, x, y)
      new=getPixel(copy, new_x, new_y)
      color=getColor(original)
      setColor(new, color)
  return copy

# function to create a copy of a picture that is 50% smaller
def createTurkey(pic):
  pathTurk = getMediaPath("turkey.jpg")
  turk = makePicture(pathTurk)
  pathGreen = getMediaPath("GREEN.png")
  copy = makePicture(pathGreen)

  new_y = -1
  for y in range (0,getHeight(pic)):
      new_y += 1
      new_x = 680
      for x in range (0, getWidth(pic)):
        new_x += 1
        original=getPixel(pic, x, y)
        new=getPixel(copy, new_x - y/2, new_y + x/2)
        color=getColor(original)
        if getRed(original) > (getGreen(original) - 30) or getBlue(original) > (getGreen(original) - 30):
          setColor(new, color)
          r = getBlue(new)
          setBlue(new, r*1.1-50)
          b = getBlue(new)
          setBlue(new, b*.9-50)    
          g = getGreen(new)
          setGreen(new, g*.9-50)   
  for y in range (0,getHeight(copy)-2):
     for x in range (600, getWidth(copy)-2):
       original=getPixel(copy, x, y)
       new=getPixel(copy, x-1, y)
       color=getColor(original)
       if getRed(new) < (getGreen(new) - 30) and getBlue(new) < (getGreen(new) - 30):
         setColor(new, color)
  new_y = 140
  for y in range (0,getHeight(turk)):
      new_y += 1
      new_x = 20
      for x in range (0, getWidth(turk)):
        new_x += 1
        original=getPixel(turk, x, y)
        new=getPixel(copy, new_x, new_y)
        color=getColor(original)
        if getRed(original) > (getGreen(original) - 30) or getBlue(original) > (getGreen(original) - 30):
          setColor(new, color)
          r = getBlue(new)
          setBlue(new, r*1.1-50)
          b = getBlue(new)
          setBlue(new, b*.9-50)    
          g = getGreen(new)
          setGreen(new, g*.9-50) 
  return(copy)
  
def pyCopy(source, target, targetX, targetY):
  new_y = targetY - 1
  
  for y in range (0,getHeight(source)):
    if new_y < getHeight(target)-1:
      new_y += 1
      new_x = targetX - 1
    for x in range (0, getWidth(source)):
      if new_x < getWidth(target)-1:
        new_x += 1
      original=getPixel(source, x, y)
      new=getPixel(target, new_x, new_y)
      color=getColor(original)
      setColor(new, color)

  return target

#Function requires a picture and an x and y coordinate
#It will ask you what you want the card to say, then how big you want it
#then itll add the text to the picture.
#You can change the font by change the first parameter in the myFont variable
#You can also color the font by changing/removing the color parameter to addTextWithStyle (default is black)  
def createText(picture, x, y):
  import java.awt.Font as Font
  text = requestString("Enter what you would like the card to say.")
  size = requestInteger("How big do you want the text?")
  myFont = makeStyle("Blackadder ITC", Font.BOLD, size) #you can change the font to anything in java awt
  addTextWithStyle(picture, x, y, text, myFont, red) 