import pygame

 # Intialize  the pygame
pygame.init()

 # create the screen
screen = pygame.display.set_mode((800,600))
 # Title and Icon
 # Left

 # Game Loop
running = True
while running:
    for event in pygame.event.get () :
        if event.type == pygame.QUIT:running = False

   screen.fill(( 0, 0, 0))
   pygame.display.update()

