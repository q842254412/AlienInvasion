# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:14:42 2024

@author: gentleH
"""

import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load("image/ship.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)