import sys
import os
import time
import pdb
import random
from Player import Player
from Scene import Scene
from Start import Start
    
# intialise the currentPlayer object
currentPlayer = Player()

# intialising the first scene of the game
# x coordinate = 1
# y coordinate = 1
# intro 
Scene1_1 = Scene(
    1,
    1,
    "You come to on the side of a road.\n" +
    "You see a caravan and dead bodies lying everywhere.\n" +
    "You can't remember anything. What do you do?\n",
    ["a dull dagger", "some mouldy bread", "a tattered cloak"]
)

# intialise the start sequence           
StartNow = Start(
    "Would you like to begin [y/n]"
)

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
    
#############################
## Prints out the help menu
## and then calls ready for
## the scene you were in.
#############################
def help(currentScene):

    # prints the commands the player can use in any scene
    printOptions (
        "\"look around\" to see what items are around.\n"
        "\"pick up\" to pick up items.\n"
        "\"attack\" to attack nearby enimies.\n"
        "\"talk\" to talk to anyone nearby.\n"
        "\"exit\" to exit.\n" +
        "\"i\" to open your inventory.\n" +
        "\"m\" to view the map."
    )
    
    # return to the current scene
    currentScene.ready()  

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
        "Welcome to the land.\n" +
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
        
        # go to Scene1_1.begin
        Scene1_1.begin()
        
    # to catch any input that isn't an option
    else:
      say (
           "Oops thats not an option\n"
            )
      
      # wait 0.5 seconds      
      time.sleep(0.5)
      
      # go back to main
      main()
      
# call main
main()
