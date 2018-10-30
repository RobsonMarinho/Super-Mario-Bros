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
            self.flip_state()   #Verificando o estado do menu (a troca de player 1 para player 2)
        self.state.update(self.screen, self.keys, self.current_time)

    ''' TROCA DE ESTADOS DO MENU '''
    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous

    #Função onde se apertar o 'x' para sair, o done fica True e executa a função event_loop
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:  #Verifica se alguma telca foi pressionada
                self.keys = pg.key.get_pressed()
                self.toggle_show_fps(event.key)
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
                self.state.get_event(event)

    def toggle_show_fps(self, key):
        if key == pg.K_F5:
            self.show_fps = not self.show_fps   #Não exibe o título
            if not self.show_fps:
                pg.display.set_caption(self.caption)

    def main(self):
        """Main lloop for entire program"""
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            if self.show_fps:   #Se for True executa o clock e exibe os frames por segundo
                fps = self.clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
                pg.display.set_caption(with_fps)