#Lab 13 Problem 2
#Chris Carson and Michael Rose

#global setup
end = false #Variable to flag whether the player wishes to end the game and exit.
lose = false #Variable for the lose condition
win = false #Variable for the win condition
correctInput = ["NORTH", "EAST", "SOUTH", "WEST"]
#Initiate a two demonsiaonl array with  "list comprehension" for the 12 rooms.
w, h = 6, 14;
RoomsArray = [[0 for x in range(w)] for y in range(h)]
#Initiate a variable for the player containing the room they are in and what they have in their inventory.
PlayerRoom = 1
#player's inventory as a list.
playerInventory = ["keys"]

#Descriptions for each room stored in a multi-line triple quote string.
d1 = "You are coming home from work and hear something rustling inside. The door is locked, use your key to open the door."

d2 = """You sneak over to the fence that separates your house from the neighbors to the East of you. You've never trusted that strange family. You suspect they are all 
part of a traveling circus. That would explain their bearded mother and the siamese twin sisters. Who knows what else might be living with them. You inspect the fence 
for signs that anyone has climbed over or dug under. You find what appear to be the tracks of a flea, but can't be certain."""

d3 = """You enter the patio area and notice a nice picnic table.  On the northern wall you can see a nice barbecue.  You notice that the charcoal is slightly warm.  
When did I use my barbecue last? You notice windows on the east wall that allow you to see into the dining area.  Next to the barbecue, you see a tool chest.
Below the windows you notice a cooler that is empty.  What happened to your beer?  To the east is the door back to the entrance of the house."""

d4 = """You enter the front of the house. The lights are off and for now, it is almost completely quiet. You can make out a small squirrel figurine on top of a table. The faint sounds of a nearby clock's internal mechanisms are 
the only noise. To the west, the door to the patio is slightly ajar and a mild breeze is coming through. To the north lies the dining area."""

d5 = """Upon the entering the dining room, a sour, stale stench hits your face. What is that? Has some foul smelling creature been in here? Or do I just need to take 
out the garbage? You look around the room and notice what appear to be smudgy tracks leading outside throug the North door of the dining area. There is a bloody knife on the table. You might be able to use it."""

d6 = """You enter the gym.  You are immediately hit with the smell of musty towels.  From the west wall you hear the faint humming sound of a treadmill. Could someone have left it on?  Or did you forget to turn it off?  
Upon further inspection, you notice a key on the treadmill. Near the dumbbell rack to the north is a door leading outside. To the east is a door with a window that leads outside. You can see the pool house and the door leading to the dining area through it."""

d7 = """You step outside and notice the dim light of the neighbor's back portch illuminating the ground in front of you. There seems to be some muddy tracks leading into the Dining Area South. 
As you reach to close the door, smudges of what looks like mud are up aggainst it. There are also muddy tracks into the gym to the West. The light of the pool house is illuminating small puddles of water along the walkway leading into it to the North. 
Was someone already wet or just come out of the pool house? You can investigate the fence to the east for any clues regarding the wet floor."""

d8 = """You step outside and see the shed has been left alone to the North. The pool house to the East looks like someone was in there. The gym to the South has hardly been used since it was made a couple of days ago. 
There doesn't seem to be any obvious sign that someone walked through this area."""

d9 = """Upon entering the poolhouse, you notice the air is muggy and reeks of chlorine.  In the center of the room is a large rectangular pool.  
There is a stack of towels next to the northern door which leads outside.  You notice there are inner tubes stacked next to the western door which leads to an area between the gym and the shed.  
You also noticed wet footprints leading to the southern door which leads to the area between the poolhouse and the dining area.  Has someone been swimming in your pool? There seems to be some muffled 
noises coming from the pool house floor. Is that your imagination? You see a hatch to get under the floor but you cannot get enough leverage to open it with your bare hands.  If only you had a tool that could help you open it..."""

d10 = """The door creaks open as you enter a small shed. From the light coming through the door, you can barely make out what looks like a sea of tools filling up the room. 
You notice an old chainsaw sitting on the table in the back. It is clear from the amount of dust on everything that no one has been in here for quite some time."""

d11 = """You take a moment in the fresh breeze to clear your head. Surely you must be imaging all of this. You remember being haunted by something in the dark at camp as a 
little kid. No one else would believe you, but you know what you saw. Those terrible eyes and such sharp fangs. Could it be back? No, of course not. It couldn't possibly be... could it?!
As you look around you notice an odd pedastal in the center of the area."""

d12 = """You approach a chain-link fence. The fence is in disrepair and no longer stands straight, but is still managing to do its job. 
In the distance over the fence, you can almost make out what appears to be a better game. Unfortunately, you have no way to get to it."""

d13 = """You enter the secret room.  There is a note on the back wall stating that this room may be too easy for people to find and based on the fact you play adventure games a lot, you are inclined to agree.
Unfortunately, there is nothing else of value to you in this room."""
#Alternate Room descriptions
alt1 = "You are coming home from work and hear something rustling inside. Since the door is unlocked, you are now able to enter your house."

alt3 = """You enter the patio area and notice a nice picnic table.  On the northern wall you can see a nice barbecue.  You notice that the charcoal is slightly warm.  
When did I use my barbecue last? You notice windows on the east wall that allow you to see into the dining area.  Next to the barbecue, you see the tool chest where you got the crowbar.
Below the windows you notice a cooler that is empty.  What happened to your beer?  To the east is the door back to the entrance of the house."""

alt4 = """You enter the front of the house. The lights are off and for now, it is almost completely quiet. The faint sounds of a nearby clock's internal mechanisms are 
the only noise. To the west, the door to the patio is slightly ajar and a mild breeze is coming through. To the north lies the dining area."""

alt5 = """Upon the entering the dining room, a sour, stale stench hits your face. What is that? Has some foul smelling creature been in here? Or do I just need to take 
out the garbage? You look around the room and notice what appear to be smudgy tracks leading outside throug the North door of the dining area. 
There was a knife on the table, but now you have it in your hand.  You should probably avoid going back to the front of the house."""

alt6 = """You enter the gym.  You are immediately hit with the smell of musty towels.  From the west wall you hear the faint humming sound of a treadmill. Could someone have left it on?  Or did you forget to turn it off?  
Near the dumbbell rack to the north is a door leading outside. To the east is a door with a window that leads outside. You can see the pool house and the door leading to the dining area through it."""

alt11 = """You take a moment in the fresh breeze to clear your head. Surely you must be imaging all of this. You remember being haunted by something in the dark at camp as a 
little kid. No one else would believe you, but you know what you saw. Those terrible eyes and such sharp fangs. Could it be back? No, of course not. It couldn't possibly be... could it?!
The trapdoor on the east side is wide open, making you wonder what other secrets there are here..."""


#Skipping array value 0 so it's easier to read the room number (1-12), room information is loaded as follows:
#[title, description, inventory, room to north, north to east, room to south, room to west]
RoomsArray[1] = ["Front Porch", d1, "keys", 0,0,0,0]
RoomsArray[2] = ["East Fence", d2, "", 0,0,0,7]
RoomsArray[3] = ["Covered Patio", d3, "crowbar", 0,4,0,0]
RoomsArray[4] = ["Inside House", d4, "figurine", 5,0,1,3]
RoomsArray[5] = ["Dining Area", d5, "knife", 7,0,4,0]
RoomsArray[6] = ["Gym", d6, "key", 8,7,0,0]
RoomsArray[7] = ["Outside South", d7, "", 9,2,5,6]
RoomsArray[8] = ["Outside West", d8, "", 10,9,6,0]
RoomsArray[9] = ["Pool House", d9, "", 11,0,7,8]
RoomsArray[10] = ["Shed", d10, "chainsaw", 0,0,8,0]
RoomsArray[11] = ["Outside North", d11, "pedestal", 12,0,9,0]
RoomsArray[12] = ["North Fence", d12, "", 0,0,11,0]
RoomsArray[13] = ["Secret Room", d13, "", 0,0,0,11]

#Function for generating the string that tells the player which directions they can head in.
def genConString(Room):
  connection_string = "You can go "
  if Room[3] != 0: connection_string += "North, "
  if Room[4] != 0: connection_string += "East, " 
  if Room[5] != 0: connection_string += "South, " 
  if Room[6] != 0: connection_string += "West, " 
  connection_string = connection_string[:-2]
  connection_string += ".\n"
  last_comma = connection_string.rfind(",")
  if last_comma != -1: connection_string = connection_string[:last_comma] + ", and" + connection_string[last_comma + 1:]
  if connection_string.count(",") == 1:
    last_comma = connection_string.rfind(",")
    connection_string = connection_string[:last_comma] + "" + connection_string[last_comma + 1:]
  elif Room[3] == 0 and Room[4] == 0 and Room[5] == 0 and Room[6] == 0:
    connection_string = "You can go nowhere yet... the front door is locked."
  return connection_string
 
#Function that moves the player into the next room.
def movePlayer(Room, direction):
  global PlayerRoom
  if direction.upper() == "NORTH" and Room[3] != 0:
    PlayerRoom = Room[3]
  elif direction.upper() == "EAST" and Room[4] != 0:
    PlayerRoom = Room[4]
  elif direction.upper() == "SOUTH" and Room[5] != 0:
    PlayerRoom = Room[5]
  elif direction.upper() == "WEST" and Room[6] != 0:
    PlayerRoom = Room[6]
  else:
    printNow("You can't go that way")

#takes an object from a room if applicable and adds it to player inventory
def takeObject(Room):
  if Room[2] == "knife":
  #if the knife is in the current room, add the knife to your inventory, remove the knife from the room's inventory and change the description of the room
    playerInventory.append("knife")
    Room[2] = ""
    Room[1] = alt5
    printNow("You take the bloody knife from the table to use later just in case.")
  elif Room[2] == "figurine":
    playerInventory.append("figurine")
    Room[2] = ""
    Room[1] = alt4
    showInformation("You pick up the squirrel figurine and put it in your pocket. It might be useful.")
  elif Room[2] == "key":
    playerInventory.append("key")
    Room[2] = ""
    Room[1] = alt6
    showInformation("You take the key from the treadmill.  You expect something bad to happen but nothing happens.  You wonder what this key is used for.")
  elif Room[2] == "":
    showInformation("There is nothing you can take in this room")
  elif Room[2] == "chainsaw":
    showInformation("You don't want to lug around a broken chainsaw... Better test it first.")
    
#uses an item in a room
def useObject(Room, inventory):
  if Room[2] == "":
    showInformation("There is nothing to use in this room.")
  elif Room[2] == "pedestal":
    if "figurine" in inventory:#checks if you have the figurine
      inventory.remove("figurine")#removes figurine from inventory
      showInformation("You place the figurine on the pedastal and a trap door opens on the east side leading to a secret room!")#print out message
      #the next 3 commands remove the pedestal to prevent it from being used again and then adds a connection to the secret room
      Room[2] = ""
      Room[1] = alt11
      Room[4] = 13
    else:#if you don't have it you get a message
      showInformation("You inspect the pedastal and notice small indentations on the top.  Maybe you can put something on it.")
  elif Room[2] == "crowbar":
      if "key" in inventory:
        inventory.remove("key")
        showInformation("You open the tool chest with the key and open it to find a crowbar. Neat!")
        inventory.append("crowbar")
        Room[2] = ""
        Room[1] = alt3
      else:
        showInformation("You try to open the tool chest but it is locked.")
  elif Room[2] == "chainsaw":
    showInformation("After many attempts, you finally get the chainsaw running! It runs out of gas 5 seconds later.")
  elif "keys" in inventory and Room[2] == "keys":
    inventory.remove("keys")
    Room[1] = alt1
    Room[3] = 4
    showInformation("You feel a chill as you try to insert the key into the hole.")
    
def listInventory():
  list = ""
  global playerInventory
  if len(playerInventory)>0:
    list = playerInventory[0]
    if len(playerInventory)>1:
      for x in range (1,len(playerInventory)):
        list = list + ", " + playerInventory[x]
  return list
    
#Function to print the Intro
def printIntro():
  showInformation("""Welcome to The Code Blooded House of Horror! 
While in each room, you will be told which direction you can move. You can move in that direction by typing North, East, West or South. 
Type help to view these instructions at anytime. Type exit to quit the game.\n""")

#game starts here
#wait one second
printIntro()
playerName = requestString("Please enter your name:")

#Main while loop.
while end == false:
  printNow(RoomsArray[PlayerRoom][0]) #RoomsArray[PlayerArray[0]][0] is the title of the room
  printNow(RoomsArray[PlayerRoom][1]) #RoomsArray[PlayerArray[0]][1] is the description of the room
  printNow(genConString(RoomsArray[PlayerRoom])) #RoomsArray[PlayerArray[0]] will give the room array that the player is currenlty in
  list = listInventory()
  command = requestString("What direction would you like to move?\nType: North, East, South or West\n"+
  "'use' = use item in room\n'take' = take an item from the room\n'help' = instructions\n'exit' = quit game\n"+
  "Inventory = "+list)
  if command.upper() == "EXIT":
    end = true
  elif command.upper() == "HELP":
    printIntro()
  elif command.upper() == "USE":
    useObject(RoomsArray[PlayerRoom], playerInventory)
  elif command.upper() == "TAKE":
    takeObject(RoomsArray[PlayerRoom])
  elif command.upper() in correctInput:
    movePlayer(RoomsArray[PlayerRoom], command)
  else:
    printNow("I'm sorry, that's not a correct command... Please try again")
  if ("knife" in playerInventory and "crowbar" in playerInventory) and PlayerRoom == 9:#the player wins after finding a bum in the hidden room under the pool
    win = true 
    break;  
  if "knife" in playerInventory and PlayerRoom == 1:#The player loses if they take the knife and go to the front porch
    lose = true
    break; 
  
#end while loop check for conditions
if win:
  printNow("You open the hatch with your crowbar and it reveals a well lit passageway. After going down a small flight of stairs you find a " +
  "mostly naked man saying he lived there before. You threaten him with the knife and he claims squatter's rights. Little did he know you are a lawyer. Good Job, "+playerName+"!+\n You Win!")
if lose:
  printNow("As you return to the front porch you are tackled by a passerby who sees the knife in your hands and mistakes you for a serial killer. "+ 
  "He pins you down and calls the police. You are arrested and sent to jail. So sorry, "+playerName+".\nYOU LOSE!")
elif win == false and lose == false:
  printNow("It's a shame, "+playerName+". No one likes a quitter.")