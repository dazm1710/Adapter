import pygame, sys
from pygame.locals import *
from Clases.jugador import *

class PersonajeAbstracto():
    def dispara(self,posx,posy): pass
    def dibujar(self): pass
    

pj = Personaje()
class AdapterPersonaje(PersonajeAbstracto):

    def __init__(self, persona):
        self.pj = persona
        self.rect = self.pj.imgPersonaje.get_rect()
        self.rect.centerx=150
        self.rect.centery=550
        #self.listaDisparo=self.pj.imgPersonaje.listaDisparo

    def dispara(self,posx,posy):
        self.pj.disparar(posx,posy)
        self.pj.rect.right+=self.pj.velocidad
    
    def dibujar (self,superficie):
        superficie.blit(pj.imgPersonaje,self.rect)

