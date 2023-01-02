import pygame as pg
from pygame.locals import *

size = largeur, hauteur = (1000, 1000)

pg.init()
run = True
screen = pg.display.set_mode(size)
pg.display.set_caption("Jeu de bille")

while run:
  for event in pg.event.get():
    if event.type == QUIT:
      run = False

pg.quit()