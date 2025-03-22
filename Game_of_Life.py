import time
import pygame
import random
import sys

pygame.init()

width= 400; height=600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Grid of 10/10")

def draw_grid():
    
    row = col =100
    row_width= width//row
    col_height = height//col
    
    x=y=0
    
    for i in range(row):
        x+=row_width
        
        pygame.draw.line(screen, pygame.Color("white"), (x,0), (x, height))
        
    for i in range(col):
        y+=col_height
        pygame.draw.line(screen, pygame.Color("white"), (0,y), (width, y))
        
def main():
    
    fps=60
    fps_clock =pygame.time.Clock()
    
    while True:
        
        screen.fill(pygame.Color("black"))
        
        draw_grid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        
        pygame.display.update()
        
main()