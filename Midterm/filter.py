def r():
  #setMediaFolder()
  path = getMediaPath("beer.jpg")
  key = makePicture(path)
  path = getMediaPath("CSUMB KEY 2.jpg")
  key2 = makePicture(path)
  path = getMediaPath("bar.jpg")
  img = makePicture(path)
  path = getMediaPath("beer.jpg")
  otter = makePicture(path)


def filter_blur(pic,radius):
  import ImageFilter
  blur = image.filter(ImageFilter.GaussianBlur(radius))
  image.paste(blur,(0,0))
  return pic
