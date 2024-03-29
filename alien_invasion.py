# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:41:52 2024

@author: gentleH
"""

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        #creat a display window
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()
        
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()