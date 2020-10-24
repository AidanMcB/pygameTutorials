import pygame
from pygame.locals import *
# pygame is a colleection of different modules in a single python package
# some of the moduless are written in c and some in python

# Line 1 imports all available pygame modules into the pygamee packages 
# Line 2 (optional) puts a limited set of constants and functions into the global namespace of your script

pygame.init()
# you must initialize pygame before you can use it 
# This will attempt to initialize all the pygame modules for you
# Not all modules need to be initialized, but this will automatically initializee the ones that do 
# You could also initialize each modile by hand, ex:
pygame.font.init()
# This will throw a more specific error if something goes wrong
# Any modules that must be initialized also have a git_init() function which will 
#   return true if the module has been initialized 

# Modules that are initialized also usually have a quit() function. You do not need 
#   to explicitly call these as pygame will cleanly quit all the 
#   initializeed modules when python finishes
# WFW