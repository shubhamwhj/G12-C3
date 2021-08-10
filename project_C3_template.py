import pygame

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((600,600))

BLUE=(0,0,255)

player=pygame.Rect(150,200,200,200)

player_image = pygame.image.load("spinning.png").convert_alpha()

angle=0
speed=0

while True:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        
      # check if key has been released
        if event.key == pygame.K_ESCAPE:
            speed= 0
             
      if event.type == pygame.KEYDOWN:      
        if event.key == pygame.K_LEFT:
            speed=3
        # check if right arrow key is pressed
            speed=-3
     
    angle += speed  
     
    newimage # transform the player_image with respect to angle 
    
    screen.blit(newimage ,player)
    
    pygame.display.update()
    clock.tick(30)
