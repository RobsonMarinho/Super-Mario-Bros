__author__ = 'Robson_Marinho && Isabela Oliveira'

from .. import setup, tools
from .. import constants as c
from .. import game_sound
from .. components import info

    ### Recebe o estado de carregamento ###
class LoadScreen(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(selfself, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        self.sound_manager = game_sound.Sound(self.overhead_info)

    def set_next_state(self):
        """Sets the next state"""
        return c.LEVEL01

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.LOAD_SCREEN

    def update(self, surface, keys, current_time):
        """Updates the loading screen"""
        if (current)time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_into.update(self.game_info)
            self.overhead_info.draw(surface)

        elif (current_time - self.start_time) < 2600:
            surface.fill(c.BLACK)
