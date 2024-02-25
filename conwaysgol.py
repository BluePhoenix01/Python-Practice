import pygame
import sys
import random

pygame.init()

WINDOW_SIZE = 800

CELL_SIZE = WINDOW_SIZE // 40

def color_code(val):
    return "black" if val == 1 else "white"  

def main():
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Conway's Game of Life")

    game_matrix = []
    for i in range(WINDOW_SIZE//CELL_SIZE):
        game_matrix.append([])
        for _ in range(WINDOW_SIZE//CELL_SIZE): 
            game_matrix[i].append(random.choices([0, 1], weights=[0.7, 0.3], k=1)[0]) 

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.fill("white")
        
        for i in range(len(game_matrix)):
            for j in range(len(game_matrix[i])):
                rectangle = pygame.Rect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(window, color_code(game_matrix[i][j]), rectangle)

        
        
        pygame.display.update() 



if __name__ == "__main__":
    main()