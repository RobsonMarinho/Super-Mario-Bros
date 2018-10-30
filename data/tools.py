__author__ = 'Robson_Marinho && Isabela Oliveira'

import pygame as pg
import os

#Configuracoes principais do jogo

    #CONFIGURANDO TECLADO

keybiding = {

    'action':pg.K_s,    #Tecla de ação
    'jump'  :pg.K_SPACE,  #Tecla de Pulo
    'left'  :pg.K_LEFT,   #Tecla de esquerda
    'right' :pg.K_RIGHT,  #Tecla de direita
    'down'  :pg.K_DOWN    #Tecla de abaixar
}

### CLASSE PRINCIPAL QUE CONTROLA O JOGO, CONTÉM O LOOP DO JOGO E OS EVENTOS ###

##Iniciando a classe Control com método init
class Control(object):
    def __init__(self, caption):
        self.screen = pg.display.get_surface()  #Verifica a posição da tela
        self.done = False   #Verifica se está jogando ou não
        self.Clock = pg.time.Clock()    #verifica o tempo do jogo
        self.caption = caption
        self.fdp = 60   #Controla a velocidade do jogo
        self.show_fps = False
        self.current_time = 0.0 #Tempo zerado ao (re)iniciar
        self.keys = pg.key.get_pressed()    #Verifica se tem alguma tecla pressionada
        self.state_dict = {}    #Verifica em qual estado está o jogo
        self.state_name = None  #Verifica id, acento entre outras informações
        self.state = None   #Exibe o estado jogando ou não jogando

def setup_states(self, state_dict, start_state):
    self.state_dict = state_dict    #Recebe o state_dict
    self.state_name = start_state   #Recebe o nome do estado inicial
    self.state = self.state_dict[self.state_name]

def update(self):
    self.current_time = pg.time.get_ticks()
    if self.state.quit: #se fecha a tela do jogo, se torna True
        sel.done = True
    elif self.state.done:
        self.flip_state()   
    self.state.update(self.screen, self.keys, self.current_time)

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state   #Recebe o nome do estado inicial
        self.state = self.state_dict[self.state_name]

    #Função de atualização que utiliza o clock atual
    def update(self):
        self.current_time = pg.time.get_ticks() #Define os segundos da fase
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)

    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
