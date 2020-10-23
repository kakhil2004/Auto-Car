import pygame
#from win32api import GetSystemMetrics
import time

#width = GetSystemMetrics(0)
#height = round(GetSystemMetrics(1)*(2/5))
#print(height)
pygame.init()
screen = pygame.display.set_mode((1080,1080))
running = True
enable = False
#images
background = pygame.image.load("images\\black.png")
enabled = pygame.image.load("images\\enable.png")


while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        if enable:
            enable = False
            print("done")
        elif keys[pygame.K_F1] and (not enable):
            enable = True
            print("on")


    screen.blit(enabled, (20, 30))
