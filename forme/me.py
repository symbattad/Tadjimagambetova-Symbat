import pygame
pygame.init()
window_size=(300,300)
pygame.display.set_caption("Синий фон")
screen = pygame.display.set_mode(window_size)
background_color = (0, 0, 255) 
screen.fill(background_color)
pygame.display.flip()
