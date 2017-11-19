#lab 8 warmups and write my own functions
def findS():
  s=pickAFile()
  sd=makeSound(s)
  return sd

#Now you try get sample sound returns 50
def testS():
  sd = findS()
  return getSampleValueAt(sd,10000)
  
  
# This function answers the question: What are the sample values at indicies 
#10730 and 20350 both before and after the function is run?
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

#Increase the volume
def increaseVolume():
  sd = findS()
  for sample in getSamples(sd):
    value = getSampleValue(sample)
    #increases the volume to double the original sample
    setSampleValue(sample, value * 2)
  play(sd)  

#1. Write a function called decreaseVolume that takes a 
#sound object and reduces the volume by half 
def decreaseVolume():
  sd = findS()
  for sample in getSamples(sd):
    value = getSampleValue(sample)
    #sets the volume to half of the original sample
    setSampleValue(sample, value / 2)
  play(sd)

#2. Write a function called changeVolume that takes a sound 
#object and a factor that tells you how much to increase 
#(or decrease) the volume by whatever amount user enters
def changeVolume(factor):
  sd = findS()
  for sample in getSamples(sd):
    value = getSampleValue(sample)
    #sets the volume to half of the original sample
    setSampleValue(sample, value * factor)
  play(sd)   
  
#More Volume 
#1Write a function called maxSample that 
#finds the maximum sample value in your sound. 
#You may find it useful to use the Python function 
#max(x, y) that takes two values (x and y) and returns 
#the larger of the two.
def maxSample():
  sd = findS()
  large=0
  for sample in getSamples(sd):
    #looks for the largest sample
    large = max(large,getSampleValue(sample))
  return large  
         
#You can use your maxSample function to write a new function 
#called maxVolume that increases the volume of each sample 
#by the factor (factor=32767/largest) where largest is the 
#value returned by your maxSample function. 
def maxVolume():
  sd = findS()
  factor = maxSample()
  for sample in getSamples(sd):
    value = getSampleValue(sample)
    #sets the volume to half of the original sample
    setSampleValue(sample, value*factor) 
  play(sd) 

#Write a new function called goToEleven, this function should 
#take a sound as a parameter. For each sample, if the sample 
#value is greater than 0, it should set the sample value to 
#the maximum possible value: 32767. If the sample value is 
#less than 0, it should set the sample value to the minimum 
#possible value: -32768.    
def goToEleven(sound):
  for sample in getSamples(sound):
    value = getSample(sample)
    if value > 0:
      setSample(sample,32767)
    if value < 0:
      setSample(sample,-32768)  
  return sound      