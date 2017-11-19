
#LAB 8 - CST 205
#John Coffelt, Michael Rose

#Increases the volume of a sound by twice the sample value.
def increaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 2)

#Decreases the volume of a sound by half the sample value.      
def decreaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value / 2)

#Changes the volume of a sound by a factor parameter.
#Factors less than 1 decrease volume.
def changeVolume(sound, factor):
   assert factor >= 0, "factor must be greater than or equal to 0!"
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * factor)

#Finds the max sample value in a sound.      
def maxSample(sound):
  samples = getSamples(sound)
  max_value = getSampleValue(samples[0])
  for sample in samples:
    max_value = max(max_value,getSampleValue(sample))
  return max_value

#Sets every sample value to 32767 if it is greater than 0 and -32767 if it is less than 0.    
def goToEleven(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0: setSampleValue(sample, 32767)
    elif value < 0: setSampleValue(sample, -32767)



