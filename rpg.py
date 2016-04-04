import sys
import os
import time
import pdb
import random

###################################################################################################
# GLOBAL HELPERS
###################################################################################################

#############################
## Simple method for adding a
## new line to a String.
############################
def say(line):
    
    # print the line with a new line character at the end
    print (line + "\n")
    
#############################
## This is a helper function that
## prints out a formatted block of text.
##
## line: String
#############################
def printOptions(line):

    # prints a line break before and after a statement
    print ("\n==============================\n")
    print (line)
    print ("\n==============================\n")
    
def map(currentScene):
    printOptions (
        """
+-----------+-----------+-----------+        N
|           |           |           |        ^
|           |    Old    |           |        |
|   Forest  |  Wanderer | Wasteland |   W <-----> E
|           |           |           |        |
|           |           |           |        v
+-----------------------------------+        S
|           |           |           |
|           |           |           |
|  Floppy   |  Caravan  |  Meadows  |
|   Bush    |           |           |
|           |           |           |
+-----------------------------------+
|           |           |           |
|           |   Black   |  Melgrove |
|   Adam    |   Marsh   |   Ruins   |
|           |           |           |
|           |           |           |
+-----------+-----------+-----------+
        """
    )
        
    # return to the current scene
    currentScene.ready()
    
#############################
## Prints out the help menu
## and then calls ready for
## the scene you were in.
#############################
def help(currentScene):

    # prints the commands the player can use in any scene
    printOptions (
        "\"look around\" to see what items and people are around.\n"
        "\"pick up\" to pick up items.\n"
        "\"attack\" to attack nearby enimies.\n"
        "\"talk\" to talk to anyone nearby.\n"
        "\"exit\" to exit.\n" +
        "\"i\" to open your inventory.\n" +
        "\"m\" to view the map.\n" +
        "\"go north\" to move north.\n" +
        "\"go south\" to move south.\n" +
        "\"go east\" to move east.\n" +
        "\"go west\" to move west."
        )
    
    # return to the current scene
    currentScene.ready()

###################################################################################################
# START
###################################################################################################

class Start:
    #############################
    ## The constructor method.
    ##
    ## message: String
    ############################
    def __init__(self, message):
    
        # set message to message
        self.message = message
    
    #############################
    ## This handles all the input
    ## commands from the player
    ############################
    def ready(self):
    
        # prints the start message
        say (
            self.message
        )
        
        # wait for input from player
        option = input("-> ")
        
        # "y": yes, start the game
        if option == "y":
        
            # clear the screen
            os.system('clear')
            
            # begin at scene one
            gameScenes[0].begin()
            
        # "n": no, go back to the main menu
        elif option == "n":
        
            # clear the screen
            os.system('clear')
            
            # return to main
            main()
            
        # "exit": exit the game
        elif option == "exit":
        
            # exit the game
            sys.exit
            
        # to catch any input thats not an option
        else:
            say (
                "Sorry could you speak up a bit?"
            )
            
            # waits 0.5 seconds before continuing
            time.sleep(0.5)
            
            # return to StartNow.ready
            StartNow.ready()
            
# initialise the start sequence           
StartNow = Start(
    "Would you like to begin [y/n]"
)

###################################################################################################
# PLAYER
###################################################################################################

class Player:
    ############################
    ## The constructor method.
    ############################
    def __init__(self):
    
        # initialise player "name" as an empty string
        # later we'll ask the player for a name
        self.name = ""
        
        # initialise player "maxhealth" to 50
        self.maxhealth = 50
        
        # initialise player "health" to maxhealth 
        # so they start with full health
        self.health = self.maxhealth
        
        # initialise player "damage" to 10
        self.damage = [1, 10]
        
        # initialise player "inventory" to an empty list
        self.inventory = []
        
    ############################
    ## pickUp is called whenever
    ## the player types "pick up"
    ## in a scene.
    ##
    ## item: String
    ## sceneItems: List - A reference to the scene's items
    ############################
    def pickUp(self, item, sceneItems):
    
        # add the picked up item to the players inventory
        self.inventory.append(item)
        
        # remove the picked up item from the scene
        # that it was picked up from
        sceneItems.remove(item)
        
        # print that the picked up item was added to
        # the players inventory
        say (
            item.name + " was added to your inventory!"
        )
        
# initialise the currentPlayer object
currentPlayer = Player()

###################################################################################################
# CHARACTER
###################################################################################################

class Character:
    #############################
    ## The constructor method.
    ##
    ## name: String
    ## health: Integer
    ## damage: List
    ## items: List
    ############################
    
    def __init__(self, name, health, damage, items):
    
        # set the local "name" property
        self.name = name
        
        # initialise player "health" to maxhealth 
        # so they start with full health
        self.health = health
        
        # initialise character "damage" 
        self.damage = damage
        
        # set the local "items" property to the list of items
        self.items = items

###################################################################################################
# ITEM
###################################################################################################

class Item:
    #############################
    ## The constructor method.
    ##
    ## name: String
    ## damage: Integer
    ############################ 
    def __init__(self, name, damage):
    
        # set the local "name" property
        self.name = name
        
        # initialise item "damage" 
        self.damage = damage

###################################################################################################
# SCENE
###################################################################################################

class Scene:
    #############################
    ## The constructor method.
    ##
    ## x: Integer
    ## y: Integer
    ## intro: String
    ## items: List
    ## description: String
    ## characters: List
    ############################
    def __init__(self, x, y, intro, items, description, characters):
    
        ##############################################
        ## Each scene is one square in a grid.
        ## So each scene needs an "x" axis coordinate
        ## and a "y" axis coordinate.
        ##############################################
        
        # set the local "x" property to an integer
        self.x = x
        
        # set the local "y" property to an integer
        self.y = y
        
        # set the local "description" property
        self.description = description
        
        # set the local "characters" property
        self.characters = characters
        
        ##############################################
        ## Each scene has an intro which is the
        ## discription the player gets when they enter
        ## the scene.
        ##############################################
        
        # set the local "intro" property
        self.intro = intro
        
        ##############################################
        ## Each scene has a number of unique items
        ## that the player can pick up.
        ##############################################
        
        # set the local "items" property to the list of items
        self.items = items
        
        self.beenHereBefore = False
    
    #############################
    ## Begin is called everytime a player
    ## enters a scene.
    #############################
    def begin(self):
    
        if not self.beenHereBefore:
                
            # print the intro
            printOptions (
                self.intro
            )
        
            self.beenHereBefore = True
            
        else:
        
            printOptions (
                self.description
            )
            
        # go to self.ready  
        self.ready()
        
    #############################
    ## This method handles all the
    ## input commands from the player.
    ############################    
    def ready(self):
    
        # wait for input from player
        option = input("-> ")
        
        # "help": call the help method which prints the list of possible commands
        if option == "help":
            help(self)
        
        # "i": display the players inventory.
        elif option == "i":
        
            # initialising inventoryItems as an empty String
            inventoryItems = ""
            
            # loop through the inventory items
            for inventoryItem in currentPlayer.inventory:
            
                # add a formatted line for this inventory item
                inventoryItems = inventoryItems + "     * %s" % inventoryItem.name + " that does " + str(inventoryItem.damage) + " damage.\n"
            
            # print the formatted inventory
            printOptions (
                "Inventory:\n\n" +
                inventoryItems
            )
            
            # return to self.ready
            self.ready()
            
        # "look around": check for items in the current scene
        elif option == "look around":
        
            if self.characters:
                
                # initialising characters as an empty String
                characters = ""
                
                # loop through the characters
                for character in self.characters:
                
                    # add a formatted line for this character
                    characters = characters + "   * %s" % character.name + " who can deal " + str(character.damage) + " damage.\n"
                    
                # print the characters that are in the current scene    
                say (
                    "You notice:\n\n" +
                    characters
                )
                              
            # check if there are any items in the list of items
            if self.items:
            
                # initialising inventoryItems as an empty String
                items = ""
                
                # loop through the items
                for item in self.items:
                
                    # add a formatted line for this item
                    items = items + "   * %s" % item.name + " that does " + str(item.damage) + " damage.\n"
                    
                # print the items that are in the current scene    
                say (
                    "You see:\n\n" +
                    items
                )
                                
            # if there are no items or people in the current scene
            if not self.items and not self.characters:
                say (
                    "You don't see anything"
                )
                
            # return to self.ready    
            self.ready()
            
        # "pick up": wait for user input
        elif option == "pick up":
        
            # prompt the user for what item in the current scene they would like to pick up
            say (
                "What would you like to pick up?"
            )
            
            # initialise the empty container "foundItem" as false
            foundItem = False
            
            # wait for input from player
            option = input ("-> ")
            
            # loop through the scene's items
            for item in self.items:
                
                # if the option the user typed is the name of this item
                if item.name == option:
                    
                    # setting foundItem item to the item the player typed
                    foundItem = item
            
            # testing to see if an item was found        
            if foundItem:
                currentPlayer.pickUp(foundItem, self.items)
                
            # if the player input something that isn't an item
            else:
                say (
                    "There is no such thing as \"" + option + "\""
                )
                
            # return to self.ready    
            self.ready()
        
        # currently a place holder for the talk option
        elif option == "talk":
            
            if self.characters:
            
                say (
                    "No one really understands what you're saying.\n" +
                    "it's like you're speaking a different language.\n"
                )
            
            else:
            
                say(
                    "Who are you talking to? There is nobody around.\n"
                )
                
            self.ready()
            
        # currently a place holder for the battle option
        elif option == "attack":
                
            if self.characters:
            
                itemDamage = 0
                
                for item in currentPlayer.inventory:
                    
                    itemDamage = itemDamage + item.damage
                    
                
                say (
                    "\nYou:\n" +
                    "Health = " + str(currentPlayer.health) + "\n" +
                    "Base damage = " + str(currentPlayer.damage) +  "\n" +
                    "Item damage = " + str(itemDamage) + "\n"
                )
                
                for character in self.characters:
                    
                    if character.health > 0:
                    
                        say (
                            "\n" + character.name + ":\n" +
                            "Health = " + str(character.health) + "\n" +
                            "Damage = " + str(character.damage) + "\n"       
                        )

                        say (
                            "...\n"
                        )
                        
                        time.sleep(1)
                        
                        playerDamageDealt = random.randint(currentPlayer.damage[0], currentPlayer.damage[1]) + itemDamage
                        
                        character.health = character.health - playerDamageDealt
                        
                        if character.health <= 0:
                        
                            say (
                                "You have slain " + character.name + "!\n" 
                            )
                            
                            droppedItems = False
                            
                            for item in character.items:
                                
                                self.items.append(item)
                                
                                droppedItems = True
                                
                            if droppedItems:
                                
                                say (
                                    "It looks like " + character.name + " dropped something.\n"
                                )
                            
                            self.characters.remove(character)
                            
                        else:                 
                            
                            say (
                                "You attack " + character.name + " for " + str(playerDamageDealt) + " damage!\n" +
                                character.name + " is at " + str(character.health) + " health!\n"
                            )
                            
                            
                            say (
                                "...\n"
                            )
                            
                            time.sleep(1)
                            
                            characterDamageDealt = random.randint(character.damage[0], character.damage[1])
                            
                            currentPlayer.health = currentPlayer.health - characterDamageDealt
                            
                            say (
                                character.name + " attacked you dealing " + str(characterDamageDealt) + " damage!\n" +
                                "You're at " + str(currentPlayer.health) + " health.\n"
                            )
                            
                        if currentPlayer.health <= 0:
                        
                            say (
                                "You have been slain by " + character.name + "\n"
                            )
                            
                            time.sleep(1.5)
                            
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            sys.exit
                            
                                                
            else:
            
                say (
                    "You look for someone to hit but\n" +
                    "there isn't anybody around.\n"
                )
                   
            self.ready()
                
                
        
        # "m": call the map method that prints out the map    
        elif option == "m":
            map(self)
        
        # "go north": adds 1 to the current y coordinate    
        elif option == "go north":
        
            newX = self.x
            newY = self.y + 1
            
            os.system('clear')
            
            time.sleep(1)
            
            printOptions (
                "You head north..."
            )
            
            time.sleep(2)
            
            os.system('clear')
            
            self.goToNextScene(newX, newY)       
                                                          
        # "go south": minus 1 to the current y coordinate 
        elif option == "go south":
        
            newX = self.x
            newY = self.y - 1
            
            os.system('clear')
            
            time.sleep(1)
            
            printOptions (
                "You head south..."
            )
            
            time.sleep(2)
            
            os.system('clear')
            
            self.goToNextScene(newX, newY)
            
        # "go east": adds 1 to the current x coordinate 
        elif option == "go east":
        
            newX = self.x + 1
            newY = self.y
            
            os.system('clear')
            
            time.sleep(1)
            
            printOptions (
                "You head east..."
            )
            
            time.sleep(2)
            
            os.system('clear')
            
            self.goToNextScene(newX, newY)
        
        # "go west": minus 1 to the current x coordinate     
        elif option == "go west":
        
            newX = self.x - 1
            newY = self.y
            
            os.system('clear')
            
            time.sleep(1)
            
            printOptions (
                "You head west..."
            )
            
            time.sleep(2)
            
            os.system('clear')
            
            self.goToNextScene(newX, newY)
            
        # "exit": exit the game
        elif option == "exit":
        
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
            sys.exit
         
        # to catch anything the player inputs that not an option 
        else:
            say (
                    "There is no such thing as \"" + option + "\""
            )
            
            # return to self.ready
            self.ready()
            
    def goToNextScene(self, newX, newY):
    
        nextScene = False
        
        for Scene in gameScenes:
            
            if Scene.x == newX and Scene.y == newY:
                
                nextScene = Scene
                
        if nextScene:
            
            nextScene.begin()
            
        else:
            say (
                "You can't go there, sorry!"
            )
            
            self.ready()                                    
            
gameScenes = []

# initialising the first scene of the game
# x coordinate = 0
# y coordinate = 0
# intro 
gameScenes.append(Scene(
    0,
    0,
    "You come to on the side of a road.\n" +
    "You see a caravan and dead bodies lying everywhere.\n" +
    "You can't remember anything. What do you do?\n",
    [
        Item(
            "a dull dagger",
            4
        ),
        
        Item(
            "some mouldy bread",
            -1
        ),
        
        Item(
            "a tattered cloak",
            0
        )
    ],
    "Nothing has changed, you see the caravan and the dead bodies lying everywhere.",
    []
 ))

gameScenes.append(Scene(
    0,
    1,
    "After heading down the road for awhile, you see a figure\n" +
    "in the distance. Eventually they get closer and you see that\n" +
    "its an old wanderer. He sits down on the side of the road\n" +
    "and waves at you, you walk over to him.\n",
    [],
    "Nothing has changed, the road is still the same.\n",
    [
        Character(
            "the Old Wanderer",
            20,
            [0, 8],
            [
                Item(
                    "a shimmering sabre",
                    12
                ),
                
                Item(
                    "some smelly cheese",
                    -4
                ),
                
                Item(
                    "a pair of well worn socks",
                    0
                )
            ]   
        ),
        
    ]
))

gameScenes.append(Scene(
    1,
    1,
    "As you continue to walk, you notice the scenery beginning\n" +
    "to change. It gradually becomes less green and more brown.\n" +
    "Eventually there aren't any plants and everything is eerily quiet.\n" +
    "\n" +
    "As you come over the next rise in the road you begin to hear a sort\n" +
    "of chanting. You continue walking until you come across a goblin camp.\n" +
    "in the middle of the camp is a pile of treasure. 4 goblins are dancing\n" +
    "around the treasure.\n" +
    "\n" +
    "The chanting stops and the goblins turn towards you, drawing their\n" +
    "weapons. They start running towards you, waving their weapins menacingly.\n",
    [
        Item(
            "a jewelled dagger",
            8
        ),
        
        Item(
            "some cotton brandy",
            -4
        )
    ],
    "Nothing has changed, the goblin camp is still there.\n",
    [
        Character(
            "a Goblin",
            10,
            [0, 5],
            [
                Item(
                    "a soiled loin cloth",
                    -20
                )
            ]
        ),
            
        Character(
            "a Goblin",
            12,
            [0, 7],
            [
                Item(
                    "a rusty knife",
                    3
                )
            ]
        ),
            
        Character(           
            "a Goblin",
            7,
            [0, 15],
            [
                Item(
                    "a torn ear",
                    0
                )
            ]
        ),
        
        Character(
             "the Goblin Chief",
            30,
            [0, 20],
            [
                Item(
                    "a rusty broadsword",
                    10
                )
            ]   
        )
    ]
))

gameScenes.append(Scene(
    1,
    0,
    "You travel for awhile and eventually come to a meadow full\n" +
    "of flowers. A little girl is in the meadow picking\n" +
    "flowers. She looks at you cursiously as you\n" +
    "walk past.\n",
    [
        Item(
            "a bright dandalion",
            0
        ),
        
        Item(
            "a thorny rose",
            1
        )
    ],
    "Nothing has changed, the meadow is still flowery.\n",
    [
        Character(
            "a Little Girl",
            5,
            [0, 2],
            [
                Item(
                    "a sad bouqet",
                    0
                ),
                
                Item(
                    "a bloodstained dress",
                    0
                )                
            ]   
        ),
        
    ]
))

gameScenes.append(Scene(
    1,
    -1,
    "As you're walking along, lost in thought, you realise that the air\n" +
    "has become much cooler and thicker. Their appear to be some ruins strewn\n" +
    "haphazardly around the place. You hear a spooky \"WOoooOOOOOo\" \n" +
    "as a ghost appears out of the ruins by your right.\n",
    [
        Item(
            "some spOOky chains",
            1.5
        ),
                
        Item(
            "a blob of goo",
            0
        )      
    ],
    "Nothing has changed, you hear a ghostly WOooOOo in the distance.\n",
    [
        Character(
            "a spoOky ghost",
            20,
            [0, 8],
            [
                Item(
                    "a puff of smoke",
                    0
                )
            ]   
        ),
        
    ]
))

gameScenes.append(Scene(
    0,
    -1,
    "As you're walking along, you're feet start sinking into the ground\n" +
    "you look around and notice that there is puddles everywhere.\n" +
    "You see a cabin on stilts in the middle of a big puddle.\n" +
    "\n" +
    "As you walk over to the cabin, an Ugly Witch sticks her head" +
    "out of the door and starts chanting a spell.\n" +
    "It doesn't look like it's going to be a nice one...\n",
    [
        Item(
            "a gross toadstool",
            -5
        ),
        
        Item(
            "a little toad",
            0
        )
        
    ],
    "Nothing has changed, the swamp still smells and everything feels damp.\n",
    [
        Character(
            "the Ugly Witch",
            25,
            [0, 30],
            [
                Item(
                    "a magical wand",
                    6
                )
            ]   
        ),
        
    ]
))

gameScenes.append(Scene(
    -1,
    -1,
    "You see a great floating blur in the distance.\n" +
    "As you get closer, you see that it's a giant head.\n" +
    "\n" +
    "\"Hello\" says the head. \"I am Adam.\" if you can defeat\n" +
    "me in combat, you will reach enlightenment.\n",
    [],
    "Nothing has changed, Adam is still there, floating around.\n",
    [
        Character(
            "Adam",
            1000,
            [500, 1000],
            []
        )                
    ]
))  

gameScenes.append(Scene(
    -1,
    0,
    "As you're walking down the road, you hear a rustling beside you.\n" +
    "You look to see a bush that seems to be flopping along on the ground.\n" +
    "It seems to be some sort of useless enchanted bush.\n",
    [],
    "Nothing has changed.",
    [
        Character(
            "a Floppy Bush",
            1,
            [0, 0],
            [
                Item(
                    "a floppy leaf",
                    0
                )
            ]   
        ),
        
    ]
))

gameScenes.append(Scene(
    -1,
    1,
    "You head into a leafy sunlit forest, you notice some small faeries\n" +
    "darting between the trees laughing. A badger shuffles across your\n" +
    "path and stops to look at you before shuffling off.\n" +
    "It seems like a very peacful place.\n",
    [],
    "Nothing has changed, the forest is still full of sunlight and the faeries are still laughing.",
    [
        Character(
            "an Old Badger",
            50,
            [15, 30],
            [
                Item(
                    "a sharp claw",
                    7
                ),
                
                Item(
                    "a fluffy pelt",
                    0
                )
            ]   
        ),
        
    ]
))

###################################################################################################
# MAIN
###################################################################################################

#############################
## Main is the function that 
## gets called by Python when
## the program runs
#############################
def main():

    # Start debugging
    #pdb.set_trace()

    # clear the screen
    os.system('clear')
    
    # instantiate a player
    PlayerIG = Player()
    
    # print the start menu
    printOptions (
        "Welcome to the land of Oooo.\n" +
        "Type \"help\" at anytime to see the options.\n" +
        "You can exit the game at anytime by typing \"exit\"\n" +
        "To start the game type \"start\""
    )
    
    # wait for user input
    option = input('-> ')
    
    # "help": to go to the help menu
    if option == "help":
    
        # clear the screen
        os.system('clear')
        
        # go to the help menu
        help(StartNow)
        
    # "exit": exit the game
    elif option == "exit":
    
        # exit the game
        sys.exit()
        
    # "start" start the game
    elif option == "start":
    
        # clear the screen
        os.system('clear')
        
        # go to Scene0_0.begin
        gameScenes[0].begin()
        
    # to catch any input that isn't an option
    else:
      say (
           "Oops thats not an option\n"
            )
      
      # wait 0.5 seconds      
      time.sleep(0.5)
      
      # go back to main
      main()
      
# calling main
main()