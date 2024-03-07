# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:41:52 2024

@author: gentleH
"""

import sys
import pygame
from settings import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        #creat a display window
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (self.settings.bg_color)
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()