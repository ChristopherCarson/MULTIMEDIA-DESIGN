#Michael Rose
#John Coffelt
#CST 205 - Midterm

from random import *

def get_pic():
  return makePicture(pickAFile())

def write_pic(pict):
  setMediaFolder()
  name = requestString("Please enter what you want the file to be called with .jpg at the end")
  file = getMediaPath(name)
  writePictureTo(pict, file)

def simpleCopy(pic):
  newpic = makeEmptyPicture(getWidth(pic),getHeight(pic))
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      color_to_copy = makeColor(getPixel(pic,x,y).color)
      setColor(getPixel(newpic,x,y),color_to_copy)
  return newpic

#Adds a transparent image to another image.
#Increase transparency parameter to make the image more transparent.
def addTransparentImage(source, target, targetX, targetY, transparency_level = 2):
  #source - the image that will be placed on the target image.
  #target - the base image.
  #targetX, targetY - where on the base image the source will appear.
  #transparency_level - determines how transparent the source image is. Higher number = more transparent.
  #1 = opaque.
  
  assert transparency_level >= 1, "Transparency level cannot be less than 1."
  for x in range(targetX, source.width + targetX):
    for y in range(targetY, source.height + targetX):
      source_color = getPixel(source,x - targetX,y - targetY)
      if makeColor(source_color.color) != white: #Pure whites are not transferred.
        target_color = getPixel(target,x,y)
      
        #The percentage out of 255 for each color value.
        #Divide difference between source & base by transparency level and re-add the base image's ratios.
        #Source image color ratios. 
        sr_ratio = source_color.red / 255.0
        sg_ratio = source_color.green / 255.0
        sb_ratio = source_color.blue / 255.0
      
        #Target image color ratios.
        tr_ratio = target_color.red / 255.0
        tg_ratio = target_color.green / 255.0
        tb_ratio = target_color.blue / 255.0
      
        #The new color ratios. New color exists somewhere between the source and target image color.
        nr_ratio = ((sr_ratio - tr_ratio) / transparency_level) + tr_ratio   
        ng_ratio = ((sg_ratio - tg_ratio) / transparency_level) + tg_ratio
        nb_ratio = ((sb_ratio - tb_ratio) / transparency_level) + tb_ratio  

        new_color = makeColor(255 * nr_ratio, 255 * ng_ratio, 255 * nb_ratio)
        setColor(getPixel(target, x, y), new_color)      
  return target

#addScanlines adds horizontal "scan" lines to a photo.
def addScanlines(image, increment_percent = .25, increments = 2):
  #image - the image to be modified.
  #increment percent - the percentage at which the lines increase or decrease darkness.
  #increments - Determines the size of the lines. Smaller increments means smaller lines.
  #increment percent * the number of increments cannot go over 1.
  
  assert increment_percent * increments <= 1, "scan_factor goes over 100%"
  scan_factor = 0.0 #scan_factor determines the darkness of a color. Higher number represents darker color.
  scan_increment = true #scan increment determines whether the scan_factor is increasing or decreasing.
  
  #Increment or decrement scan_factor each horizontal line.
  for y in range(0, image.height):
    for x in range(0, image.width):
      p = getPixel(image, x, y)
      setBlue(p, p.blue * (1 - scan_factor))
      setRed(p, p.blue * (1 - scan_factor))
      setGreen(p, p.green * (1 - scan_factor))
    if scan_increment == true:
      scan_factor += increment_percent    
      if scan_factor >= increment_percent * increments: scan_increment = false
    elif scan_increment == false:
      scan_factor -= increment_percent
      if scan_factor <= 0.0: scan_increment = true
  return image

#Displays a series of random 1's and 0's in string format vertically over a blank layer image.    
def createBinaryLayer(width, height, freq_denominator = 10):
  #width, height - used to determine the size of the binary layer image.
  #frequency_denominator - determines how frequent the bytes will be. Smaller number = greater frequency.
  
  import java.awt.Font as Font
  image = makeEmptyPicture(width, height)
  
  #Creates the strings based on the frequency parameter.
  for count in range(0, (image.width + image.height) / freq_denominator):
    #randomizes their location.
    x = randint(0, image.width - 1)
    y = randint(0, image.height - 1)
    #randomizes their font size.
    font = makeStyle("Lucida Console", Font.BOLD, randint(10,25))
    #and randomizes their darkness.
    rand_color = randint(0,254)
    for index in range(1, 9): #8 times to simulate a byte.
      binary = randint(0,1)
      addTextWithStyle(image,x,y + (font.size * index),str(binary), font, makeColor(rand_color))
  return image

#Enhances the green or blue in an image while reducing red and blue. Gives serious green tint.
def enhanceGreenOrBlue(image, green = true):
  pixels = getPixels(image)
  
  rvalue = .3
  gvalue = .7
  bvalue = .7
  if green == true: gvalue = 1.5
  else: bvalue = 1.5
  
  for p in pixels:
    setRed(p, p.red * rvalue)
    setGreen(p, p.green * gvalue)
    setBlue(p, p.blue * bvalue)

#Deus Ex Machina Filter  
def DEM_filter(image, green = true):
  #image - the image to create a filtered version of.
  #green - if true, the image is filtered in green. If false, blue.
  new_image = simpleCopy(image)
  binaryLayer = createBinaryLayer(new_image.width, new_image.height)
  addTransparentImage(binaryLayer, new_image, 0, 0, 3)
  addScanlines(new_image)
  enhanceGreenOrBlue(new_image, green)
  return new_image
