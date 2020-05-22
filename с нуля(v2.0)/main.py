import pygame
import Board
import Hero
import random


WINDOW_SIZE = WIDTH, HEIGHT = 800, 800
BOARD_SIZE, CELL_SIZE = 10, 50
GAME_BOARD = Board.Board(BOARD_SIZE, CELL_SIZE)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

running = True
all_heroes = [Hero.Hero(0, 0, 0, 0, random.randint(1, GAME_BOARD.board_cells()[1]),
                        random.randint(1, GAME_BOARD.board_cells()[1]), 'red'),
              Hero.Hero(0, 0, 0, 0, random.randint(1, GAME_BOARD.board_cells()[1]),
                        random.randint(1, GAME_BOARD.board_cells()[1]), 'blue'),
              Hero.Hero(0, 0, 0, 0, random.randint(1, GAME_BOARD.board_cells()[1]),
                        random.randint(1, GAME_BOARD.board_cells()[1]), 'red'),
              Hero.Hero(0, 0, 0, 0, random.randint(1, GAME_BOARD.board_cells()[1]),
                        random.randint(1, GAME_BOARD.board_cells()[1]), 'blue'),
              Hero.Hero(0, 0, 0, 0, random.randint(1, GAME_BOARD.board_cells()[1]),
                        random.randint(1, GAME_BOARD.board_cells()[1]), 'red'),
              Hero.Hero(0, 0, 0, 0, random.randint(1, GAME_BOARD.board_cells()[1]),
                        random.randint(1, GAME_BOARD.board_cells()[1]), 'blue')]

team_blue = team_red = []

for hero in all_heroes:

    if hero.draw_params()[2] == (255, 0, 0):

        team_red.append(hero)

    elif hero.draw_params()[2] == (0, 0, 255):

        team_blue.append(hero)

random.shuffle(team_blue)
random.shuffle(team_red)
turn = 'red'
index_red = index_blue = 0


def draw_objects():

    screen.fill((0, 0, 0))

    for hero in all_heroes:

        pygame.draw.rect(screen, hero.draw_params()[2], (hero.draw_params()[0] * GAME_BOARD.board_cells()[2],
                         hero.draw_params()[1] * GAME_BOARD.board_cells()[2],
                         GAME_BOARD.board_cells()[2], GAME_BOARD.board_cells()[2]))

    for cell in GAME_BOARD.board_cells()[0]:

        pygame.draw.rect(screen, (255, 255, 255), (cell[0], cell[1],
                         GAME_BOARD.board_cells()[2],
                         GAME_BOARD.board_cells()[2]), 1)

    pygame.display.flip()


def change_turn(chturn):

    if chturn == 'red':

        return 'blue'

    else:

        return 'red'


while running:

    red_hero = team_red[index_red]
    blue_hero = team_blue[index_blue]

    if turn == 'red':

        hero = red_hero

    else:

        hero = blue_hero

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_DOWN:

                hero.move_to_pos(hero.draw_params()[0] + 1, hero.draw_params()[1] + 2)

            if event.key == pygame.K_RIGHT:

                hero.move_to_pos(hero.draw_params()[0] + 2, hero.draw_params()[1] + 1)

            if event.key == pygame.K_LEFT:

                hero.move_to_pos(hero.draw_params()[0], hero.draw_params()[1] + 1)

            if event.key == pygame.K_UP:

                hero.move_to_pos(hero.draw_params()[0] + 1, hero.draw_params()[1])

    if turn == 'red':

        if index_red == len(team_red) - 1:

            index_red = 0

        else:

            index_red += 1

    else:

        if index_blue == len(team_blue) - 1:

            index_blue = 0

        else:

            index_blue += 1

    turn = change_turn(turn)
    draw_objects()


pygame.quit()
