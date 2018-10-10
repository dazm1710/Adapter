import pygame, sys
from pygame.locals import *
from Villano import *
from adapterPersonaje import *
from Clases.jugador import *

#pygame.display.set_mode((ancho,alto))
def controladorJuego():
    pygame.init()
    
    colorTexto = (0,212,52)

    fuente = pygame.font.SysFont('Calibri',30)
    texto = fuente.render("Nota: Presiona barra espaciadora para disparar",0,colorTexto)

    ventana = pygame.display.set_mode((1000,700))
    fondo = pygame.image.load('imagenes/fondoEsp.jpg')
    fondo = pygame.transform.scale(fondo, (1000,700))
    pygame.display.set_caption("All Clean")
    personajeViejo= Personaje()
    
    enemigo = Villano(750,450)
    persona = AdapterPersonaje(personajeViejo)
    reloj = pygame.time.Clock()
    
    while True:
        reloj.tick(60)
        tiempo = pygame.time.get_ticks()/1000
        ventana.blit(fondo,(0,0))
        ventana.blit(texto,(50,100))
        
        enemigo.comportamiento(tiempo)
        persona.dibujar(ventana)
        enemigo.dibujar(ventana)
        if len(persona.pj.listaDisparo)>0:
            for x in persona.pj.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.left<-10:
                    persona.pj.listaDisparo.remove(x)
                    
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key ==K_SPACE:
                    x,y = persona.rect.center
                    persona.dispara(x,y)
                    
        pygame.display.update()


controladorJuego()
