import math

#This is the drunkifi filter. It takes an image, blurs it, creates a double vision effect, adds beer glasses to the border,
#along with a drop shadow and finally puts the text "Don't Drive and Drive" on the image.
def drunkifi(img):
  path = getMediaPath("beer.jpg")
  beer = makePicture(path)
  
  img = blur(img)
  img = double(img)
  
  createText(img, "DON'T DRINK", 70, 60,60)
  createText(img, "AND DRIVE!", 70, 70,390)
  
  img = addBackgroundPattern(img, beer, 100, 100, 50, 50)
  img = addShadowEffect(img, 50, 50, img.height-100, img.width-100)
  
  show(img)
  return img

#This is the CSUMB filter. It creates a blue over-tone, adds an otter border and places a CSUMB water mark in the image.
def csumb(img):
  path = getMediaPath("CSUMB KEY.jpg")
  key = makePicture(path)
  path = getMediaPath("CSUMB KEY 2.jpg")
  key2 = makePicture(path)
  path = getMediaPath("otter.jpg")
  otter = makePicture(path)
 
  waterMark(img, key2, 50, 30, .3)
  waterMark(img, key, 50, 30, .7)
  
  img = addBackgroundPattern(img, otter, 100, 100, 50, 50)
  img = addShadowEffect(img, 50, 50, img.height-100, img.width-100)
  
  blueUp(img)
  
  show(img)
  return img
  

#A function that creates text on the image.
def createText(picture, text, size, x, y):
  import java.awt.Font as Font
  #text = requestString("Enter what you would like the card to say.")
  #size = requestInteger("How big do you want the text?")
  myFont = makeStyle("Arial", Font.BOLD, size) #you can change the font to anything in java awt
  addTextWithStyle(picture, x, y, text, myFont, red)

# This is a fun function that creates a double image of the image by separaing it 50 pixels apart. It averages out
# the RGB values of each pixel 50 pixels apart and resets the colors.
def double(img):
  pixels = getPixels(img)
  for p in pixels:
    if p.x < getWidth(img)-51 and p.y < getHeight(img)-1:
      pR=getPixel(img, p.x+50, p.y)
      bR = getBlue(pR)
      b = getBlue(p)
      setBlue(p, (bR+b)/2)
      setBlue(pR, (bR+b)/2)
      gR = getGreen(pR)
      g = getGreen(p)
      setGreen(p, (gR+g)/2)
      setGreen(pR, (gR+g)/2)
      rR = getRed(pR)
      r = getRed(p)
      setRed(p, (rR+r)/2)
      setRed(pR, (rR+r)/2)
  return img

# This function uses a modified Gaussian blur to blur the entire image.
def blur(img):
  pixels = getPixels(img)
  for p in pixels:
    if p.x < getWidth(img)-1 and p.y < getHeight(img)-1:
      pR=getPixel(img, p.x+1, p.y)
      pB=getPixel(img, p.x, p.y+1)
      p2=getPixel(img, p.x+1, p.y+1)
      bR = getBlue(pR)
      bB = getBlue(pB)
      b2 = getBlue(p2)
      b = getBlue(p)
      setBlue(p, (bR+bB+b2+b)/4)
      gR = getGreen(pR)
      gB = getGreen(pB)
      g2 = getGreen(p2)
      g = getGreen(p)
      setGreen(p, (gR+gB+g2+g)/4)
      rR = getRed(pR)
      rB = getRed(pB)
      r2 = getRed(p2)
      r = getRed(p)
      setRed(p, (rR+rB+r2+r)/4)
  return img
  
#Green screen function from previous assignment modified to take target x and y coordinates
def waterMark(img, key, targetX, targetY, shadow):
  new_y = targetY
  for y in range (0,getHeight(key)):
      new_y += 1
      new_x = targetX
      for x in range (0, getWidth(key)):
        new_x += 1
        original=getPixel(key, x, y)
        pixel=getPixel(img, new_x, new_y)
        color = makeColor(pixel.red * (1 - shadow), pixel.green * (1 - shadow), pixel.blue * (1 - shadow))
        if getRed(original) < (getGreen(original) - 30) and getBlue(original) < (getGreen(original) - 30):        
          setColor(pixel, color)
  return img

# function to blue up the image
def blueUp(pic):
  pixels = getPixels(pic)
  for p in pixels:
    b = getBlue(p)
    setBlue(p, b*1.9)
  return pic
  
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

#A helper function that finds the distance between two coordinates.
def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

