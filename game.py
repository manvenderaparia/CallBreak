import pygame
import sys
pygame.init()
#set Game resolution
screen = pygame.display.set_mode((1000,600))
#Title of the game
pygame.display.set_caption('Call Break')
#Framerate of the Game
clock=pygame.time.Clock()
# Font inside the Game
font = pygame.font.Font(None, 50)
#calling picture in the Game
Table_top=pygame.image.load('PNG/table.jpg').convert()#convert_alpha for cards
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#now inserting the picture in the game 
    screen.blit(Table_top,(0,0))
    pygame.display.update()
