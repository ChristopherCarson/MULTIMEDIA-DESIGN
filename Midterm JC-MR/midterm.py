def get_pic():
  return makePicture(pickAFile())

def write_pic(pict):
  setMediaFolder()
  name = requestString("Please enter what you want the file to be called with .jpg at the end")
  file = getMediaPath(name)
  writePictureTo(pict, file)

def allBlue(image):
  pixels = getPixels(image)
  for p in pixels:
    setRed(p, 0)
    setGreen(p, p.green * .7)
    setBlue(p, p.blue * 1.5)
  repaint(image)

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

#Adds a transparent image to another image.
#Increase transparency parameter to make the image more transparent.
def addTransparentImage(source, target, targetX, targetY, transparency_level = 2):
  for x in range(targetX, source.width + targetX):
    for y in range(targetY, source.height + targetX):
      source_color = getPixel(source,x - targetX,y - targetY)
      target_color = getPixel(target,x,y)
      
      sr_ratio = source_color.red / 255.0
      sg_ratio = source_color.green / 255.0
      sb_ratio = source_color.blue / 255.0
      
      tr_ratio = target_color.red / 255.0
      tg_ratio = target_color.green / 255.0
      tb_ratio = target_color.blue / 255.0
      
      nr_ratio = ((sr_ratio - tr_ratio) / transparency_level) + tr_ratio   
      ng_ratio = ((sg_ratio - tg_ratio) / transparency_level) + tg_ratio
      nb_ratio = ((sb_ratio - tb_ratio) / transparency_level) + tb_ratio  

      new_color = makeColor(255 * nr_ratio, 255 * ng_ratio, 255 * nb_ratio)
      setColor(getPixel(target, x, y), new_color)      
  return target
