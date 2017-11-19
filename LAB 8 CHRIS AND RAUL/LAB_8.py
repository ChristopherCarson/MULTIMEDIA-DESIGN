
#This is a test function I used to quickly look at the increases in a sound clip at specific indicies.
def test(sound, location):
  v = getSampleValueAt(sound, location)
  print v
  increaseVolume(sound)
  v = getSampleValueAt(sound, location)
  print v
  increaseVolume(sound)
  v = getSampleValueAt(sound, location)
  print v

# This function answers the question: What are the sample values at indicies 10730 and 20350 both before and after the function is run?
def test2(sound):
  v = getSampleValueAt(sound, 10730)
  print v
  v = getSampleValueAt(sound, 20350)
  print v
  increaseVolume(sound)
  v = getSampleValueAt(sound, 10730)
  print v
  v = getSampleValueAt(sound, 20350)
  print v
  
#function to increase a sound (doubling it's volume)
def increaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 2)
      
#function to decrease a sound's volume. (by one half)
def decreaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * .5)
      
#function to change the volume by the any factor passed to it as a parameter.
def changeVolume(sound, factor):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * factor)
  
#function to find the maximum value of a sound
def maxSample(sound):
  max = 0
  for sample in range(0, getLength(sound)):
    value = getSampleValueAt(sound, sample)
    if value > max:
      max = value
  return max
 
#A function to find the maximum possible value, then to increase the volume to that level.         
def maxVolume(sound):
  factor = (32767/maxSample(sound))
  changeVolume(sound, factor)
      