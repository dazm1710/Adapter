import pygame
from pygame.sprite import Sprite
from pygame import *

class Villano(pygame.sprite.Sprite):

    def __init__(self, posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA = pygame.image.load('Imagenes/lagartoInicial1.png')
        self.imagenB = pygame.image.load('Imagenes/lagartoSalto1.png')
        self.imagenC = pygame.image.load('Imagenes/lagartoSalto2.png')
        self.imagenD = pygame.image.load('Imagenes/lagartoSFinal.png')

        self.listaImagenes = [self.imagenA,
                              self.imagenB,
                              self.imagenC,
                              self.imagenD]
        self.posImagen=0
        
        self.imagenVillano = self.listaImagenes[self.posImagen]
        self.rect = self.imagenVillano.get_rect()
        
        self.rect.top=posy
        self.rect.left=posx
        
        self.tiempoCambio = 1

    def dibujar(self, superficie):
        self.imagenVillano = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenVillano,self.rect)
        
    def comportamiento(self,tiempo):
        
        if self.tiempoCambio == tiempo:
            self.posImagen +=1
            self.tiempoCambio +=1
            
            if self.posImagen > len(self.listaImagenes)-1:
                self.posImagen=0
