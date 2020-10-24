import sys, pygame      # import pygame module

pygame.init()           # initialize each of the modules
 
size = width, height = 820, 740     
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)      #create a graphical window, 
#creates a new surfacee object to represent the displayed graphics
# pygame represents images as 'surface' objects

ball = pygame.image.load("thor_for_game.png")   # returns a surface with the ball data
#SDL_image library supports BMP, JPG, PNG, TGA, and GIF
ballrect = ball.get_rect()                      # stores rectangular coordinates

while 1:                                        #infinite loop (while 1 is true)
    for event in pygame.event.get():            #check for user input
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)             # move and draw the ball
    if ballrect.left < 0 or ballrect.right > width:     # reverse direction on hitting edges
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill(black)                      # erase the screen with black
    # erase the screen so we do not see a trail of balls, animation frame by frame
    screen.blit(ball, ballrect)             # draw one image onto anotheer
    # a blit means copying pixel colors from one image to another 
    # pass the blit a source surface to copy from, 
    # and a position to plae the source onto the destination
    pygame.display.flip() 
    # pygame manages the display with a double buffer, when we are finished
    # drawing we call pygame.display.flip() 
    # This makes everything we have drawn on the screen surgace become visible
    # this buffering makes sure we only see completley drawn frames on the screen
    # without it, the user would seee the half completed parts of the screen
    # as they are being createed                   

    # WFW