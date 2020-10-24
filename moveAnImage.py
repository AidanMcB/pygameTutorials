#   Pygame has a display Surface, this is basically an image that is visible
# on the screeen, and the image is made up of pixels. The main way you change these pixels 
# is by calling the blit() function. THis copies the pixels from one image onto another
import pygame
# When you blit an image on the screen, you are simply changing the color of the pixels on the screen

# Above all WFW

# No pixels are added or moved, only colors of existing pixels are changed
# Images in pygame are Surfaces, but are NOT connected to the display Surface

# They are copied to the displa when they are blitted, but an uniqe original still exists
# Basically, movement is created my rapidly drawing, erasing, and redrawing images on the screen

# NOTE: FOLLOWING MY CHARACTERS BUT NOT MY ORIGINAL EXAMPLE
# Create a Screen
screen = ["_", "_", "_", "_", "_", "_", "_", "_"]
print(screen) 
# Create Character (letter C for Character)
screen[4] = "C"
print(screen) 
# Assign the Character a Position as a variable 
character_position = 4
screen[character_position] = "C"
print(screen) 
# Now to change his position, change the value of the variable
character_position = character_position + 1 
screen[character_position] = "C"
print(screen) 
# The above code generates two characters, indicating to us why we need to erase the screen 
#  after each redrawing of an animation frame
# We can create a variable that will represent our "background"
# This will be reset every time we animate or move our character
background = ["_", "_", "_", "_", "_", "_", "_", "_"]
screen = [0]*6                         #a new blank screen
for i in range(6):
    screen[i] = background[i]
print(screen)
character_position = 4
screen[character_position] = 8
print(screen)

screen = create_screen()
player = load_player_image()
background = load_background_image()
screen.blit(background, (0, 0))        #draw the background
position = player.get_rect()
screen.blit(player, position)          #draw the player
pygame.display.update()                #and show it all
for x in range(100):                   #animate 100 frames
    screen.blit(background, position, position) #erase
    position = position.move(2, 0)     #move player
    screen.blit(player, position)      #draw new player
    pygame.display.update()            #and show it all
    pygame.time.delay(100)             #stop the program for 1/10 second