__author__ = 'Robson_Marinho && Isabela Oliveira'

import os                #centraliza tela com essa classe que é usada em bastante em jogos
import pygame as pg      #importa pygame e "apelida/referencia" por 'pg'
import tools             #importa classe tools
import constants as c    #importa a constants "apelida/referencia" por 'c'

    ### CRIANDO A TELA E DIRETÓRIOS DE RECURSOS ###

TITLE = c.TITLE #get Título do jogo

os.environ['SDL_VIDEO_CENTERED'] = '1'   #Centraliza a tela podemos fazer uma validação pela numeração 1 ou 0
pg.init()    #inicializa o pygame

## Eventos de abaixar, parar, e sair ##
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.TITLE)             #get título da tela
SCREEN = pg.display.set_mode(c.SCREEN_SIZE) #get tamanho da tela  largura e altura
SCREEN_RECT = SCREEN.get_rect()             #Recebe área retangular

FONTS = ''  #Variável constante
MUSIC = ''  #Variável de musicas
GFX   = ''  #Variável de imagens/gráfico
SFX   = ''  #Variável de som