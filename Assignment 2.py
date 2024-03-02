#Import Simple Graphics
from SimpleGraphics import*
resize(800,800)

#Create a function to prompt the user to choose background and foreground colors
def chooseColors(): #This first part gets the input of the background colors
    colorList = ['black', 'white', 'blue', 'green']
    backgroundColor = input("What color do you want to use for the background? (black, white, blue, green): ")

    while True: #This true statement checks if the color is not in the list then it will execute said statements
        if backgroundColor not in colorList:
            print(f"{backgroundColor} is not a valid option")
            backgroundColor = input("Please pick one of the colors provided (black, white, blue, green): ")
        else:
            background(backgroundColor)
            break
    
    foregroundColor = input("What color do you want to use for the foreground? (black, white, blue, green): ")
# Below checks if the foreground color is the same as the background & not in the list given
    while True: 
        if foregroundColor == backgroundColor:
            print(f"{foregroundColor} cannot be the same as the background!")
            foregroundColor = input("Please pick one of the colors provided: ")
        if foregroundColor not in colorList:
            print(f"{foregroundColor} is not a valid option.")
            foregroundColor = input("Please pick one of the colors provided (black, white, blue, green)")
            
        else:
            setOutline(foregroundColor)
            break

    return backgroundColor, foregroundColor

def getCoordinates():
    # Get the starting x-coordinates from the user
    xCoor = int(input("Enter the starting x-coordinate: "))
    while True:
        if xCoor < 0 or xCoor > 800:
            print("Coordinates must be between 0 and 800.")
            xCoor = int(input("Please enter the starting x-coordinate: "))
        else:
            break

    # Now get the starting y-coordinates from the user
    yCoor = int(input("Enter the starting y-coordinate: "))
    while True:
        if yCoor < 0 or yCoor > 800:
            print("Coordinates must be between 0 and 800.")
            yCoor = int(input("Please enter the starting y-coordinate: "))
        else:
            break

    return xCoor, yCoor

def nextCoordinates(): #Although it is the same as above, it checks the coordinates as well as give a different prompt
    nextX = int(input("Enter the next x-coordinate: "))
    while True:
        if nextX < 0 or nextX > 800:
            print("Coordinates must be between 0 and 800.")
            nextX = int(input("Please enter the next x-coordinate: "))
        else:
            break

    nextY = int(input("Enter the next y-coordinate: "))
    while True:
        if nextY < 0 or nextY > 800:
            print("Coordinates must be between 0 and 800.")
            nextY = int(input("Please enter the next y-coordinate: "))
        else:
            break
    
    return nextX, nextY

# Draws a line from the starting x and y to the ending y with the foreground color
def drawLine(xCoor, yCoor, endX, endY):
    line(xCoor, yCoor, endX, endY)

    return line

#Start the game!
def playGame():
    print("Welcome to Pictionary! Let's get started.")
    chooseColors()

#Prompt the drawer to start first
    print("Can I have the drawer step up!")
    shape = str(input("What is the shape? "))

# Get the coordinates by calling the previous function
    startX, startY = getCoordinates()

#Now put in the spaces so that the guesser cannot see the shape
    for i in range(11):
        print(' ')

#Now start the count since they inputed a point, and make sure they have the previous cordinates down
    count = 1
    previousX, previousY = startX, startY

# Now prompt the guesser to see what choice they want to make
    while True:
        guesserChoice = int(input("Do you want to 1) guess the shape or 2) guess the next point? "))
        if guesserChoice == 2:
            xCoor, yCoor = nextCoordinates() #Call upon the previous function created
            drawLine(previousX, previousY, xCoor, yCoor)
            previousX, previousY = xCoor, yCoor
            count = count + 1
            if startX == xCoor and startY == yCoor:
                print(f"Awwwww nice try, it was {shape}!")
                break
        elif guesserChoice == 1: 
            guessShape = input("Okay! What do you think it is hmmm? ")
            if guessShape != shape:
                print("Ahhhh that was sadly not the correct choice. Better luck next time!")
                break
            else: 
                print(f"Wow! You got it after seeing {count} points.")
                break
        else:
            print("Invalid output, try 1 or 2 :)") #provide an output for when they put in other options besides 1 or 2
        
    #Now give the game over text
    print("Game Over!")

playGame()