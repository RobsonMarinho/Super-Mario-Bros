__author__ = 'Robson_Marinho && Isabela Oliveira'

from . import setup, tools
import constants as c

def main():
    ## Adicionar os estados e a classe de controle ##
    run_it = tools.Control(setup.TITLE) #Chama o título

    run_it.main()