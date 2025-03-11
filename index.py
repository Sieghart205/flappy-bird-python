import pygame
import random

pygame.init()

magent = (255,0,255)
white = (255,255,255)
black = (0,0,0)

size = width,height = 500,600
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Bird con una bola morada")

pajarracoSize = width2,height2 = 30,30
pajarox = (width / 5) - width2 / 2
pajaroy = (height / 2) - height2 / 2
velocidad = [0,10]
pajarraco = pygame.Rect(pajarox,pajaroy,width2,height2)

tuberiaTopSize = tuberiaWidth,tuberiaHeight = 20, random.randint(0, height - 220)
tuberiaTopX = width - tuberiaWidth
tuberiaTopY = 0
velocidadTuberiaTop = [0,40]
tuberiaTop = pygame.Rect(tuberiaTopX,tuberiaTopY,tuberiaWidth,tuberiaHeight)

tuberiaBottomSize = tuberiaBottomWidth, tuberiaBottomHeight = tuberiaWidth, (height - tuberiaHeight)
tuberiaBottomX = width - tuberiaWidth
tuberiaBottomY = height - tuberiaBottomHeight +90
velocidadTuberiaBottom = [0,40]
tuberiaBottom = pygame.Rect(tuberiaBottomX,tuberiaBottomY,tuberiaBottomWidth,tuberiaBottomHeight)

clock = pygame.time.Clock()

inGame = True

while inGame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False

    keys  = pygame.key.get_pressed()
    

    pajarraco.y += 2
        

    if keys[pygame.K_SPACE]:
        pajarraco.y -= 8
    

    screen.fill(black)

    pygame.draw.ellipse(screen, magent, pajarraco)
    
    pygame.draw.rect(screen, white, tuberiaTop)
    pygame.draw.rect(screen, white, tuberiaBottom)
    
    pygame.display.flip()
    clock.tick(120)