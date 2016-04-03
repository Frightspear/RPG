class Player:
    ############################
    ## The constructor method.
    ############################
    def __init__(self):
    
        # intialise player "name" as an empty string
        # later we'll ask the player for a name
        self.name = ""
        
        # intialise player "maxhealth" to 100
        self.maxhealth = 100
        
        # intialise player "health" to maxhealth 
        # so they start with full health
        self.health = self.maxhealth
        
        # intialise player "damage" to 10
        self.damage = 10
        
        # intialise player "inventory" to an empty list
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
            item + " was added to your inventory!"
        )
