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
            Scene1_1.begin()
            
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