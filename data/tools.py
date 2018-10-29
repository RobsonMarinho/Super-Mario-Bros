__author__ = 'Robson_Marinho'

import pygame as pg
import os

#Configuracoes principais do jogo

    #CONFIGURANDO TECLADO

keybiding = {

    'action':pg.K_s,    #Tecla de ação
    'jump':pg.K_SPACE,  #Tecla de Pulo
    'left':pg.K_LEFT,  #Tecla de esquerda
    'right':pg.K_RIGHT  #Tecla de direita

}

#CLASSE PRINCIPAL QUE CONTROLA O JOGO, CONTÉM O LOOP DO JOGO E OS EVENTOS

def __init__(self, caption):
    self.screen = pg.display.get_surface()  #Verifica a posição da tela
    self.done = False   #Verifica se está jogando ou não
    self.Clock = pg.time.Clock()    #verifica o tempo do jogo
    self.caption = caption
    self.fdp = 60   #Controla a velocidade do jogo
    self.show_fps = False
    self.current_time = 0.0 #Tempo zerado ao (re)iniciar
