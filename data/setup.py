__author__ = 'Robson_Marinho'

import os   #centraliza tela com essa classe que é usada em IOS/Android
import pygame  as pg            #importa pygame
from . import tools             #importa calsse tools
from . import constants as c    #importa a constants

    ### CRIANDO A TELA E DIRETÓRIOS DE RECURSOS ###

TITLE = c.TITLE #get Título do jogo

os.environ['SDL VIDEO CENTERED']    #centraliza a tela
pg.ini()    #inicializa

#Eventos de abaixar, parar, e sair
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])

pg.display.set_caption(c.TITLE)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect() #Recebe área retangular

FINTS = ''  #Variável constante
MUSIC = ''  #Variável de musicas
GFX = ''    #Variável de imagens/gráfico
SFX = ''    #Variável de som