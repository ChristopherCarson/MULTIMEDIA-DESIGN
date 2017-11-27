#Lab 11 Christopher Carson, John Coffelt, Michael Rose, Raul Ramirez
import time
import array

end = false #Variable to flag whether the player wishes to end the game and exit.
lose = false #Variable for the lose condition
win = false #Variable for the win condition
correctInput = ["NORTH", "EAST", "SOUTH", "WEST"]
#Initiate a two demonsiaonl array with  "list comprehension" for the 12 rooms.
w, h = 6, 13;
RoomsArray = [[0 for x in range(w)] for y in range(h)]
#Initiate an array for the player containing the room they are in and what they have in their inventory.
#PlayerArray[0] = Room player is in
#PlayerArray[1] = Player Inventory
PlayerArray = [1, ""]

#Descriptions for each room stored in a multi-line triple quote string.
d1 = "You are coming home from work and hear something rustling inside. The door is locked, use your key to open the door."
d2 = """You sneak over to the fence that separates your house from the neighbors to the East of you. You've never trusted that strange family. You suspect they are all 
part of a traveling circus. That would explain their bearded mother and the siamese twin sisters. Who knows what else might be living with them. You inspect the fence 
for signs that anyone has climbed over or dug under. You find what appear to be the tracks of a flea, but can't be certain."""
d3 = """You enter the patio area and notice a nice picnic table.  On the northern wall you can see a nice barbecue.  You notice that the charcoal is slightly warm.  
When did I use my barbecue last? You notice windows on the east wall that allow you to see into the dining area.  Below the windows you notice a cooler that is empty.  
What happened to my beer?  To the east is the door back to the entrance of the house."""
d4 = """You enter the front of the house. The lights are off and for now, it is almost completely quiet. The faint sounds of a nearby clock's internal mechanisms are 
the only noise. To the west, the door to the patio is slightly ajar and a mild breeze is coming through. To the north lies the dining area."""
d5 = """Upon the entering the dining room, a sour, stale stench hits your face. What is that? Has some foul smelling creature been in here? Or do I just need to take 
out the garbage? You look around the room and notice what appear to be smudgy tracks leading outside throug the North door of the dining area."""
d6 = """You enter the gym.  You are immediately hit with the smell of musty towels.  From the west wall you hear the faint humming sound of a treadmill.  
Could someone have left it on?  Or did I forget to turn it off?  Near the dumbbell rack to the north is a door leading outside.  To the east is a door with a window that leads outside.  
You can see the pool house and the door leading to the dining area through it."""
d7 = """You step outside and notice the dim light of the neighbor's back portch illuminating the ground in front of you. There seems to be some muddy tracks leading into the Dining Area South. 
As you reach to close the door, smudges of what looks like mud are up aggainst it. There are also muddy tracks into the gym to the East. The light of the pool house is illuminating small puddles of water along the walkway leading into it to the North. 
Was someone already wet or just come out of the pool house? You can investigate the fence to the east for any clues regarding the wet floor."""
d8 = """You step outside and see the shed has been left alone to the North. The pool house to the East looks like someone was in there. The gym to the South has hardly been used since it was made a couple of days ago. 
There doesn't seem to be any obvious sign that someone walked through this area."""
d9 = """Upon entering the poolhouse, you notice the air is muggy and reeks of chlorine.  In the center of the room is a large rectangular pool.  
There is a stack of towels next to the northern door which leads outside.  You notice there are inner tubes stacked next to the western door which leads to an area between the gym and the shed.  
You also noticed wet footprints leading to the southern door which leads to the area between the poolhouse and the dining area.  Has someone been swimming in my pool?"""
d10 = """The door creaks open as you enter a small shed. From the light coming through the door, you can barely make out what looks like a sea of tools filling up the room. 
You notice an old chainsaw sitting on the table in the back. It is clear from the amount of dust on everything that no one has been in here for quite some time."""
d11 = """You take a moment in the fresh breeze to clear your head. Surely you must be imaging all of this. You remember being haunted by something in the dark at camp as a 
little kid. No one else would believe you, but you know what you saw. Those terrible eyes and such sharp fangs. Could it be back? No, of course not. It couldn't possibly be... could it?!"""
d12 = """You approach a chain-link fence. The fence is in disrepair and no longer stands straight, but is still managing to do its job. 
In the distance over the fence, you can almost make out what appears to be a better game. Unfortunately, you have no way to get to it."""
alt6 = """You are now able to enter your house."""

#Skipping array value 0 so it's easier to read the room number (1-12), room information is loaded as follows:
#[title, description, inventory, room to north, north to east, room to south, room to west]
RoomsArray[1] = ["Front Porth", d1, "keys", 0,0,0,0]
RoomsArray[2] = ["East Fence", d2, "", 0,0,0,7]
RoomsArray[3] = ["Covered Patio", d3, "", 0,4,0,0]
RoomsArray[4] = ["Inside House", d4, "", 5,0,1,3]
RoomsArray[5] = ["Dining Area", d5, "", 7,0,4,0]
RoomsArray[6] = ["Gym", d6, "", 8,7,0,0]
RoomsArray[7] = ["Outside South", d7, "", 9,2,5,6]
RoomsArray[8] = ["Outside West", d8, "", 10,9,6,0]
RoomsArray[9] = ["Pool House", d9, "", 11,0,7,8]
RoomsArray[10] = ["Shed", d10, "chainsaw", 0,0,8,0]
RoomsArray[11] = ["Outside North", d11, "", 12,0,0,9]
RoomsArray[12] = ["North Fence", d12, "", 0,0,11,0]

printIntro()#Print intro once before game begins

#Main while loop.
while end == false:
  #printNow(player.location.outString())
  printNow(RoomsArray[PlayerArray[0]][0]) #RoomsArray[PlayerArray[0]][0] is the title of the room
  printNow(RoomsArray[PlayerArray[0]][1]) #RoomsArray[PlayerArray[0]][1] is the description of the room
  printNow(genConString(RoomsArray[PlayerArray[0]])) #RoomsArray[PlayerArray[0]] will give the room array that the player is currenlty in
  command = requestString("What direction would you like to move?\nType: North, East, South or West\n"+
  "'use' = use item in room\n'help' = instructions\n'exit' = quit game")
  if command.upper() == "EXIT":
    end = true
  elif command.upper() == "HELP":
    printIntro()
  elif command.upper() == "USE":
    useObject(RoomsArray[PlayerArray[0]])
  elif command.upper() in correctInput:
    movePlayer(RoomsArray[PlayerArray[0]], command)
  else:
    printNow("I'm sorry, that's not a correct command... Please try again")
  
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
  if direction.upper() == "NORTH" and Room[3] != 0:
    PlayerArray[0] = Room[3]
  elif direction.upper() == "EAST" and Room[4] != 0:
    PlayerArray[0] = Room[4]
  elif direction.upper() == "SOUTH" and Room[5] != 0:
    PlayerArray[0] = Room[5]
  elif direction.upper() == "WEST" and Room[6] != 0:
    PlayerArray[0] = Room[6]
  else:
    printNow("You can't go that way")

def printIntro():
  printNow("""Welcome to The Code Blooded House of Horror!
While in each room, you will be told which direction you can move. You can move in that direction by typing either North, East, South or West.
Type help to return to these instruction anytime. Type exit to quit the game.\n""")
  time.sleep(1)
    
#uses an item in a room
def useObject(Room):
  if Room[2] == "":
    printNow("There is nothing to use in this room.")
  elif Room[2] == "chainsaw":
    printNow("After many attempts, you finally get the chainsaw running! It runs out of gas 5 seconds later.")
  elif Room[2] == "keys":
    Room[2] = ""
    Room[1] = alt6
    Room[3] = 4
    printNow("You feel a chill as you try to insert the key into the hole.")


