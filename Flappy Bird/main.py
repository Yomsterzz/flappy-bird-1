import pygame
import random
from pygame.locals import *
pygame.init()

WIDTH = 864
HEIGHT = 936

clock = pygame.time.Clock()
fps = 60
# title_font = pygame.font.SysFont("helvicta", 14)
ground_x = 0
scroll_speed = 4
run = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

bg = pygame.image.load("./images/bg.png")
ground = pygame.image.load("./images/ground.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        

while run:
    clock.tick(fps)

    screen.blit(bg, (0,0))
    
    # drawing and scrolling the ground
    screen.blit(ground, (ground_x, 768))
    ground_x -= scroll_speed
    if abs(ground_x) > 35:
        ground_x = 0
        
        
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()