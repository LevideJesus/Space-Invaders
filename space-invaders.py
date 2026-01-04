import pygame
from sys import exit
pygame.init()

WIDTH = 512
HEIGHT = 512
X_POSITION_PLAYER = 224
Y_POSITION_PLAYER = 448
HEIGHT_PLAYER = 64
WIDTH_PLAYER = 64


background_image = pygame.image.load("images/background.png")
pygame.display.set_caption("Space Invader")
window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

player = pygame.Rect(X_POSITION_PLAYER,Y_POSITION_PLAYER, HEIGHT_PLAYER, WIDTH_PLAYER)

def draw ():
  pygame.draw.rect(window,("blue"), player)



while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  window.blit(background_image, (0,0))
  draw()
  pygame.display.update()
  clock.tick(60)    