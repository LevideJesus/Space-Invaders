import pygame
from sys import exit
import os
pygame.init()

WIDTH = 512
HEIGHT = 512
X_POSITION_PLAYER = 224
Y_POSITION_PLAYER = 448
HEIGHT_PLAYER = 64
WIDTH_PLAYER = 64
PLAYER_DISTANCE = 5

PLAYER_X = 224
PLAYER_Y = 448
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64

#images
def load_images(image_name, scale=None):
  image = pygame.image.load(os.path.join("images", image_name))
  if scale is not None:
    image = pygame.transform.scale(image, scale)
  return image  


background_image = load_images("background.png")
player_image = load_images("space-ship.png")

pygame.display.set_caption("Space Invader")
window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


def draw ():
  window.blit(background_image, (0,0))
  window.blit(player.image, player)
  

class Player (pygame.Rect):
  def __init__(self):
    pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
    self.image = player_image

player = Player()


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    player.x = max(player.x - PLAYER_DISTANCE, 0)

  if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    player.x = min(player.x + PLAYER_DISTANCE, WIDTH - PLAYER_WIDTH) 
  

  
  draw()
  pygame.display.update()
  clock.tick(60)    