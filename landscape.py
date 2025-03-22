# landscape-assignment

# pygame template
import math
import pygame
import random


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 10
circle_y = 50

frames=0

moon = 35
star=5
shrink=False
sun_b=255
# ---------------------------
night=False
running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    frames+=1

    # changes the colour of the sun gradually
    sun_b-=1.1
    if sun_b<=0:
        sun_b=225
    

    # DRAWING
    screen.fill((135, 206, 235))  # always the first drawing command

    # sun
    speed=1/60
    width = 325
    offset = width
    sun_x=-math.sin(frames*speed)*width + offset
    sun_y=math.cos(frames*speed)*250 + offset
    pygame.draw.circle(screen, (255,255,sun_b), (sun_x, sun_y), 30)

    # house and grass
    pygame.draw.rect(screen, (38, 139, 7), (0, 350, 680, 200))
    pygame.draw.polygon(screen, (170, 51, 106), ((230,250),(310,190), (390,250)))
    pygame.draw.rect(screen, (250, 218, 221), (260, 250, 100, 100))
    pygame.draw.rect(screen, (170,51,106), (270, 300, 20, 50))
    pygame.draw.circle(screen, (250,218,221), (275, 325), 2)

    # trees
    pygame.draw.ellipse(screen, (58,79,63), (27,310,40,90))
    pygame.draw.rect(screen, (101,67,33), (40,370, 15, 60))
    pygame.draw.ellipse(screen, (58,79,63), (557,340,40,90))
    pygame.draw.rect(screen, (101,67,33), (570,400, 15, 60))
    pygame.draw.polygon(screen, (58,79,63), ((130, 370), (155, 330), (180, 370)))
    pygame.draw.polygon(screen, (58,79,63), ((137, 335), (155, 310), (173, 335)))
    pygame.draw.rect(screen, (101,67,33), (150,350, 10, 45))

    # puddle
    pygame.draw.circle(screen, (83, 104, 120), (365, 400), 30)
    pygame.draw.circle(screen, (83, 104, 120), (360, 437), 27)
    pygame.draw.circle(screen, (83, 104, 120), (393, 415), 25)
    
    # like a "switch" for when night is "on or off"
    if sun_y>=370:
        night=True
    else:
        night = False
    
    # draws clouds and ensures that if the cloud reaches the edge of the screen (on the right) it goes back to the left
    if night==False:
        # clouds
        circle_x+=3
        pygame.draw.circle(screen, (255,255,255), (circle_x,circle_y), 25)
        pygame.draw.circle(screen, (255, 255, 255), (circle_x+25, circle_y+25), 24)
        pygame.draw.circle(screen, (255, 255, 255), (circle_x-35, circle_y+25), 25)
        pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y+31), 20)
        if circle_x>=640:
            circle_x=0
            
        
    
    elif night==True:
        screen.fill((10,52,100))
      
        # house and grass
        pygame.draw.rect(screen, (38, 139, 7), (0, 350, 680, 200))
        pygame.draw.polygon(screen, (170, 51, 106), ((230,250),(310,190), (390,250)))
        pygame.draw.rect(screen, (250, 218, 221), (260, 250, 100, 100))
        pygame.draw.rect(screen, (170,51,106), (270, 300, 20, 50))
        pygame.draw.circle(screen, (250,218,221), (275, 325), 2)

        # trees
        pygame.draw.ellipse(screen, (58,79,63), (27,310,40,90))
        pygame.draw.rect(screen, (101,67,33), (40,370, 15, 60))
        pygame.draw.ellipse(screen, (58,79,63), (557,340,40,90))
        pygame.draw.rect(screen, (101,67,33), (570,400, 15, 60))
        pygame.draw.polygon(screen, (58,79,63), ((130, 370), (155, 330), (180, 370)))
        pygame.draw.polygon(screen, (58,79,63), ((137, 335), (155, 310), (173, 335)))
        pygame.draw.rect(screen, (101,67,33), (150,350, 10, 45))

        # moon and stars
        pygame.draw.circle(screen, (246,246,246), (520,65), moon)
        pygame.draw.circle(screen, (246,246,246), (50,55), star)
        pygame.draw.circle(screen, (246,246,246), (70,125), star)
        pygame.draw.circle(screen, (246,246,246), (140,65), star)
        pygame.draw.circle(screen, (246,246,246), (200,20), star)
        pygame.draw.circle(screen, (246,246,246), (350,75), star)
        pygame.draw.circle(screen, (246,246,246), (300,30), star)
        pygame.draw.circle(screen, (246,246,246), (245,100), star)
        pygame.draw.circle(screen, (246,246,246), (450,25), star)
        pygame.draw.circle(screen, (246,246,246), (470,145), star)
        pygame.draw.circle(screen, (246,246,246), (570,15), star)
        pygame.draw.circle(screen, (246,246,246), (620,95), star)

        # puddle
        pygame.draw.circle(screen, (83, 104, 120), (365, 400), 30)
        pygame.draw.circle(screen, (83, 104, 120), (360, 437), 27)
        pygame.draw.circle(screen, (83, 104, 120), (393, 415), 25)

        # enlarges the moon and stars
        while shrink==False:
            if  6<=star<=8:
                shrink=True
            if moon>36:
                moon=35
            moon+=random.randrange(2)
            star+=random.randrange(3)

        # shrinks the moon and stars 
        while shrink==True:
            if 4<=star<=5:
                shrink=False
            if moon<34:
                moon=35
            moon-=random.randrange(2)
            star-=random.randrange(3)

    # prints a message and automatically closes the pygame window once a certain number of frames has been reached
    if frames>671:
        print("yipee")
        running= False      


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
