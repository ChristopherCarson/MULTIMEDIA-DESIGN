#Lab 11

#Class for creating an object that represents a room in a text-based adventure game.
class Room:
    __instances = []
    
    #Initializes room object with optional title and description.
    def __init__(self, title = "", description = ""):
      Room.__instances.append(self)
      self.index = Room.__instances.index(self)
      self.title = title
      self.description = description
      self.connections = {'N':'', 'E':'', 'S':'', 'W':'', 'U':'', 'D':''} #defines moveable directions
      self.inventory = {} #Defines interactable objects inside the room.
    
    #Generates the string that displays information about where the player can go from the room.
    def __genConString(self):
      connection_string = "You can go "
      if self.connections['N'] != "": connection_string += "North, "
      if self.connections['S'] != "": connection_string += "South, " 
      if self.connections['E'] != "": connection_string += "East, " 
      if self.connections['W'] != "": connection_string += "West, " 
      if self.connections['U'] != "": connection_string += "Up, " 
      if self.connections['D'] != "": connection_string += "Down, "
      connection_string = connection_string[:-2]
      connection_string += ".\n"
      last_comma = connection_string.rfind(",")  
      if last_comma != -1: connection_string = connection_string[:last_comma] + ", and" + connection_string[last_comma + 1:]
      if connection_string.count(",") == 1:
        last_comma = connection_string.rfind(",")
        connection_string = connection_string[:last_comma] + "" + connection_string[last_comma + 1:]    
      return connection_string
    
    #Connects a room object to another room object using the built-in directions N,S,E,W,U,D.            
    def connectRoom(self, index, direction, both_ways = true):
      assert index + 1 <= len(Room.__instances) , "Not a valid connection! Connecting room does not exist!"
      
      direction = direction.upper()
      assert direction in self.connections.keys(), "Not a valid direction!"
      self.connections[direction] = index
      
      if both_ways == true:
        if direction == "N": Room.__instances[index].connections['S'] = self.index
        if direction == "S": Room.__instances[index].connections['N'] = self.index  
        if direction == "E": Room.__instances[index].connections['W'] = self.index  
        if direction == "W": Room.__instances[index].connections['E'] = self.index
        if direction == "D": Room.__instances[index].connections['U'] = self.index  
        if direction == "U": Room.__instances[index].connections['D'] = self.index
    
    #Returns a string containing the room title, description, and possible directions.        
    def outString(self):
      string = self.title + "\n\n"   
      string += self.description + "\n\n"
      string += self.__genConString()
      
      return string
      
    def getRoom(self, index):
      assert index + 1 <= len(Room.__instances) , "Not a valid room index!"
      return Room.__instances[index]     

#Class for the player. Defines player objects and their actions in a text-based adventure game.
class Player:
    
    def __init__(self, location):
      self.location = location #defines starting room. Location parameter requires room object.
      self.inventory = {} #defines the player's inventory.

    #Moves the player object to another room if the room has a connected room in the provided direction.   
    def move(self, direction):
      room = self.location
      assert direction in room.connections.keys(), "Not a valid direction!"
      if room.connections[direction] != "":
        self.location = room.getRoom(room.connections[direction])
        return true
      else:
        return false

#Game begins here.    
r1 = Room("Room One", "This is room one. It's dusty! There is a sign on the wall that says 'Testing Room 1'.")
r2 = Room("Room Two", "This room seems awfully empty. Must be another test room.")
r3 = Room("Room Three", "This room is empty except for a small bug sitting in the corner. The bug eyes you suspiciously.")
r4 = Room("Room Four", "This room has 'TESTING' written all over the walls in various colors of Crayon.")

r1.connectRoom(r2.index,"e")
r1.connectRoom(r3.index,"n")
r1.connectRoom(r4.index,"S")

player = Player(r1)
printNow(player.location.outString())
player.move("S")
printNow(player.location.outString())
