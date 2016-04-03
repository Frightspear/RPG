class Scene:
    #############################
    ## The constructor method.
    ##
    ## x: Integer
    ## y: Integer
    ## Intro: String
    ## Items: List
    ############################
    def __init__(self, x, y, intro, items):
    
        ##############################################
        ## Each scene is one square in a grid.
        ## So each scene needs an "x" axis coordinate
        ## and a "y" axis coordinate.
        ##############################################
        
        # set the local "x" property to an integer
        self.x = x
        
        # set the local "y" property to an integer
        self.y = y
        
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
    
    #############################
    ## Begin is called everytime a player
    ## enters a scene.
    #############################
    def begin(self):
    
        # print the intro
        printOptions (
            self.intro
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
                inventoryItems = inventoryItems + "     * %s\n" % inventoryItem
            
            # print the formatted inventory
            printOptions (
                "Inventory:\n\n" +
                inventoryItems
            )
            
            # return to self.ready
            self.ready()
            
        # "look around": check for items in the current scene
        elif option == "look around":
        
            # check if there are any items in the list of items
            if self.items:
            
                # initialising inventoryItems as an empty String
                items = ""
                
                # loop through the items
                for item in self.items:
                
                    # add a formatted line for this item
                    items = items + "   * %s\n" % item
                    
                # print the items that are in the current scene    
                say (
                    "You see:\n\n" +
                    items
                )
                
                # return to self.ready
                self.ready()
                
            # if there are no items in the current scene
            else:
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
            
            # intialise the empty container "foundItem" as false
            foundItem = False
            
            # wait for input from player
            option = input ("-> ")
            
            # loop through the scene's items
            for item in self.items:
                
                # if the option the user typed is the name of this item
                if item == option:
                    
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
            say (
                "You're dazed and confused, there is no one around."
            )
            self.ready()
            
        # currently a place holder for the battle option
        elif option == "attack":
            say (
                "You look around for something to hit,\n" +
                "but there isn't anything around."
            )
            self.ready()
            
        # "exit": exit the game
        elif option == "exit":
            sys.exit
         
        # to catch anything the player inputs that not an option 
        else:
            say (
                    "There is no such thing as \"" + option + "\""
            )
            
            # return to self.ready
            self.ready()