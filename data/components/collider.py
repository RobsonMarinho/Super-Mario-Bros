__author__ = 'www.hugocursos.com.br'

import pygame as pg
from .. import constants as c

class Collider(pg.sprite.Sprite):
    """Sprites invisíveis colocados por cima de peças de fundo
que pode ser colidiu com (tubos, passos, chão, etc."""
    def __init__(self, x, y, width, height, name='collider'):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        #self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None

