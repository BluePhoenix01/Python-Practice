import pygame
import sys
import random
import copy

pygame.init()

WINDOW_SIZE = 800

CELL_SIZE = WINDOW_SIZE // 80


def main():
    FPS = 5
    CLOCK = pygame.time.Clock()

    WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Conway's Game of Life")

    game_matrix = (
        []
    )  # 2d Array that stores current state                                                               #2d Array that stores next state
    for i in range(WINDOW_SIZE // CELL_SIZE):
        game_matrix.append([])
        for _ in range(WINDOW_SIZE // CELL_SIZE):
            game_matrix[i].append(random.choices([0, 1], weights=[0.7, 0.3], k=1)[0])

    game_matrix_next = copy.deepcopy(game_matrix)  # 2d Array that stores next state

    paused = False

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

        if not paused:
            for i in range(len(game_matrix)):
                for j in range(len(game_matrix[i])):
                    rectangle = pygame.Rect(
                        i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE
                    )
                    pygame.draw.rect(
                        WINDOW, "black" if game_matrix[i][j] else "white", rectangle
                    )

            for i in range(len(game_matrix)):
                for j in range(len(game_matrix[i])):
                    neighbour_cells = 0
                    for k in range(3):
                        if (i == 0 and k == 0) or (
                            i == len(game_matrix) - 1 and k == 2
                        ):  # edge cases to leave edge cells for rows
                            continue
                        for l in range(3):
                            if (j == 0 and l == 0) or (
                                j == len(game_matrix[i]) - 1 and l == 2
                            ):  # edge cases to leave edge cells for cols
                                continue
                            if k == 1 and l == 1:
                                continue
                            if game_matrix[i + k - 1][j + l - 1]:
                                neighbour_cells += 1
                    if neighbour_cells == 3 and game_matrix[i][j] == 0:
                        game_matrix_next[i][j] = 1
                    elif neighbour_cells > 3 or neighbour_cells < 2:
                        game_matrix_next[i][j] = 0
                    else:
                        game_matrix_next[i][j] = game_matrix[i][j]

            for i in range(len(game_matrix)):
                for j in range(len(game_matrix[i])):
                    game_matrix[i][j] = game_matrix_next[i][j]

        pygame.display.update()


if __name__ == "__main__":
    main()
