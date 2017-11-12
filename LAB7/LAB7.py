
def turkey():
  setMediaFolder()
  pathHead = getMediaPath("head.jpg")
  head = makePicture(pathHead)
  pathTurk = getMediaPath("kturkey.jpg")
  turkey = makePicture(pathTurk)
  pathGreen = getMediaPath("greenhead.png")
  greenHead = makePicture(pathGreen)
  pathBack = getMediaPath("back.jpg")
  back = makePicture(pathBack)
  
  head = rotatePic(head)
  head = vpic(head)
  head = tiltPic(head)
  head = fixSpots(head)
  head = redColor(head)
  head = greenCopy(turkey, greenHead, head, 530, 60)
  head = shrinkPic(head, 2)
  card = chromakey(back, head, 1, 140)
  show(card)
  writePictureTo(card,"C:\Users\chris\Desktop\image.png")
  
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
  return background
  
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
  
def redColor(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getBlue(p)
    setBlue(p, r*1.1)
    b = getBlue(p)
    setBlue(p, b*.9)
    g = getGreen(p)
    setGreen(p, g*.9) 
  return(pic)
  
def greenCopy(turkey, greenHead, head, targetX, targetY):
  new_y = targetY
  for y in range (136,318):
      new_y += 1
      new_x = targetX
      for x in range (200, 389):
        new_x += 1
        key=getPixel(greenHead, x, y)
        original=getPixel(head, x, y)
        new=getPixel(turkey, new_x, new_y)
        color=getColor(original)
        if getRed(key) < (getGreen(key) - 30) and getBlue(key) < (getGreen(key) - 30):
          setColor(new, color)
  return turkey
  
def fixSpots(copy):
  for y in range (0,getHeight(copy)-2):
     for x in range (2, getWidth(copy)-2):
       original=getPixel(copy, x, y)
       new=getPixel(copy, x-1, y)
       color=getColor(original)
       if getRed(new) + getGreen(new) + getBlue(new) > 630:
         setColor(new, color)
  return copy

def tiltPic(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  copy = makeEmptyPicture(width+300, height+300)
  for y in range (0,height):
    for x in range (0, width):
        left=getPixel(pic, x, y)
        right=getPixel(copy, (x+100) + y/2 , (y+200) - x/2)
        color=getColor(left)
        setColor(right, color)
  return copy   

def vpic(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  copy = makeEmptyPicture(width, height)
  for y in range (0,height):
    for x in range (0, width):
        left=getPixel(pic, x, y)
        right=getPixel(copy, width-x-1,y)
        color=getColor(left)
        setColor(right, color)
  return copy    

# function to mirror half of the picture horizontally
def hpic(pic):

  width = getWidth(pic)
  height = getHeight(pic)

  for y in range (0,height):
    for x in range (0, width):
        top=getPixel(pic, x, y)
        bottom=getPixel(pic, x,height-y-1)
        color=getColor(top)
        setColor(bottom, color)
  return pic

# function to create a copy of a picture rotated 90 degrees
def rotatePic(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  copy = makeEmptyPicture(height, width)
  for y in range (0,height):
    for x in range (0, width):
        original=getPixel(pic, x, y)
        new=getPixel(copy, y, x)
        color=getColor(original)
        setColor(new, color) 
  return copy

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

#Surrounds an image with a background pattern by creating a larger blank image,
#inserting a pattern image to create the background, and then printing the original image on top.
#If the pattern image is smaller than the size of the new image, it will repeat to fill up space,
#so a repeating vector image works best.
def addBackgroundPattern(image, pattern, width_increase, height_increase, startX, startY):
  #image - the original image.
  #pattern - the pattern that will populate the background.
  #width_increase - the total width that the new image will increase by over the original image.
  #height_increase - the total height that the new image will increase by over the original image.
  #startX - The the top-left x-coordinate where the image will be placed on the new_image.
  #startY - The the top-left y-coordinate where the image will be placed on the new_image.
  
  new_width = width_increase + image.width
  new_height = height_increase + image.height  
  new_image = makeEmptyPicture(new_width,new_height)
  
  #Add pattern to new blank image.
  patternX = 0
  for x in range(0, new_width):
    patternX += 1
    if patternX == pattern.width: patternX = 0
    patternY = 0 
    for y in range(0, new_height):
      patternY += 1
      if patternY == pattern.height: patternY = 0 
      pattern_color = makeColor(getPixel(pattern, patternX, patternY).color)
      color_to_replace = getPixel(new_image, x,y)
      setColor(color_to_replace, pattern_color)
        
  #Add original image to new image.
  for x in range(0, image.width):
      for y in range(0, image.height):
        image_color = makeColor(getPixel(image, x, y).color)
        color_to_replace = getPixel(new_image, startX + x - 1, startY + y - 1)
        setColor(color_to_replace, image_color)       

  return new_image   
  
#Adds an artificial shading effect to the bottom and right sides of a chosen area inside of a photo.
def addShadowEffect(image, startX, startY, height, width, shadow_depth = 20, shadow_offset = 10, blur_repetitions = 3):   
  #image - The image that the effect will be applied to.
  #startX - The starting x-coordinate of the area the effect will be applied to.
  #startY - The starting y-coordinate of the area the effect will be applied to.
  #height - The height of the area the effect will be applied to.
  #width - The width of the area the effect will be applied to.
  #shadow_depth (optional) - The amount of pixels out from the x and y coordinates that will be shaded. Higher value = longer shadow.
  #shadow_offset (optional) - The amount of pixels that the shadow will be offset from the startX and startY coordinates. Creates more angled look.
  #blur_repetitions (optional) - The amount of time the blur effect will be run on the shading values.

  #Creates a matrix to store shading values.
  #Matrix contains x and y coordinates and determines each coordinate's shading value
  #by its right/bottom distance from the area that the effect is being applied to,
  #stopping once it reaches the designated depth. 
  #Shading values are from 1.0 to 0.
  shadow_matrix = [[0 for i in xrange(height + shadow_depth)] for i in xrange(width + shadow_depth)]
  for x in range(shadow_offset - 1,width + shadow_depth - 1):
    for y in range(shadow_offset - 1, height + shadow_depth - 1):
      if x <= width and y <= height:
        shadow_matrix[x][y] = 1.0
      elif x > width and y <= height:
        shadow_matrix[x][y] = ((width + shadow_depth) - x) * (1.0 / shadow_depth)
      elif x <= width and y > height:
        shadow_matrix[x][y] = ((height + shadow_depth) - y) * (1.0 / shadow_depth)
      elif x > width and y > height:
        dist = calculateDistance(width, height, x, y)
        if dist > shadow_depth: shadow_matrix[x][y] = 0
        else: shadow_matrix[x][y] = (shadow_depth - dist) * (1.0 / shadow_depth)  

  #Create Blur to smooth edges
  #Blur works by taking the average of each coordinate's shadow multiplier and the multipliers of its 8 surrounding neighbors.
  #Repeats multiple times to increase the effect.
  for count in range(blur_repetitions):
    for x in range(1, width + shadow_depth - 1):
      for y in range(1, height + shadow_depth - 1):
        sum = shadow_matrix[x][y]
        for i in range(-1, 2):
          for j in range(-1, 2):
            if i != 0 or j != 0: sum += shadow_matrix[x + i][y + j]
        shadow_matrix[x][y] = sum / 9  

  #Applies the shadow effect using the shading matrix to each pixel on the right and bottom side of the selected area.
  #Uses depth and offset values to determine where to shade.
  #Formula for applying the effect is color value * (1 - shading value)
  for x in range(0, width + shadow_depth - 1):
    for y in range(0, height + shadow_depth - 1):
      if x >= width - 1 or y >= height - 1: 
        pixel = getPixel(image, startX + x, startY + y)
        color = makeColor(pixel.red * (1 - shadow_matrix[x][y]), pixel.green * (1 - shadow_matrix[x][y]), pixel.blue * (1 - shadow_matrix[x][y]))
        setColor(pixel, color)  
  return image 

#image = get_pic()
#pattern = get_pic()
#border_image = addBackgroundPattern(image, pattern, 200, 200, 100, 150)
#image_with_shadow = addShadowEffect(border_image, 100, 150, image.height, image.width)
#show(image_with_shadow) 
