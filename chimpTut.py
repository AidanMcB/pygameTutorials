import os, sys
# allow us to create platform independent file paths
import pygame
from pygame.locals import *
# containts commonly used consants and functions 
# Ex: Rect, QUIT, HWSURFACE


if not pygame.font: print('Warning, fonts disabled') #display warnings if nots or sounds are unavailable
if not pygame.mixer: print('Warning, sound disabled')

def load_image(name, colorkey=None):      #takes image name and color
    fullname = os.path.join('data', name) #creates a path to the image file in the 'data' subdirectory
    try:
        image = pygame.image.load(fullname) #load the image
    except pygame.error as message:
        print('Cannot load image:', name)   #if the image cannot load..
        raise SystemExit(message)
    image = image.convert()        #makes a copy of a Surface and converts its color format and depth to match display, blitting to the screen will happen as quickly as possible
    if colorkey is not None:
        if colorkey is -1:      #derived from top left pixel of image
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:      # check if mixer module was loadeed
        return NoneSound()  # if not return NoneSound function 
    fullname = os.path.join('data', name)   #create a path to the sound
    try:
        sound = pygame.mixer.Sound(fullname)   
    except pygame.error as message:
        print('Cannot load sound:', fullname)
        raise SystemExit(message)
    return sound    #return the sound

