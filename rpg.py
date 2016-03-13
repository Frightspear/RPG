import sys
import os

class Player:
    def __init__(self):
        self.name = ""
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        
class Scene:
    def __init__(self, x, y, intro):
        self.x = x
        self.y = y
        self.intro = intro
    def begin(self):
        os.system('clear')
        printOptions (
            self.intro
        )
          
        self.ready()
    def ready(self):
        option = raw_input("-> ") 
        if option == "help":
            help(self)
        
Scene1_1 = Scene(
    1,
    1,
    "You come to on the side of a road.\n" +
    "You see a caravan and dead bodies lying everywhere.\n" +
    "You can't remember anything."

)

class Start:
    def __init__(self, message):
        self.message = message
    def ready(self):
        say (
            self.message
        )
        option = raw_input("-> ")
        if option == "y":
            Scene1_1.begin()
        elif option == "n":
            main()
        else:
            say (
                "Sorry could you speak up a bit?"
            )
            
StartNow = Start(
    "Would you like to begin [y/n]"
)
    
def help(currentScene):
    os.system('clear')
    printOptions (
        "\"exit\" to exit.\n" +
        "\"i\" to open your inventory.\n" +
        "\"m\" to view the map."
    )
    currentScene.ready()

def say(line):
    print (line + "\n")
      
def printOptions(line):
    print ("\n==============================\n")
    print (line)
    print ("\n==============================\n")  

def main():
    os.system('clear')
    #instantiate a player
    PlayerIG = Player()
    printOptions (
        "Welcome to the land.\n" +
        "Type \"help\" at anytime to see the options.\n" +
        "You can exit the game at anytime by typing \"exit\"\n" +
        "To start the game type \"start\""
    )
 
    option = raw_input("-> ")
    
    if option == "help":
        help(StartNow)
    elif option == "exit":
        sys.exit()
    elif option == "start":
        Scene1_1.begin()
    else:
      say ("Oops thats not an option silly\n")
      main()
       
main()
