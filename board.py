from typing import Union
from Hero import Hero


class Board:
    def __init__(self, x_size, y_size):
        self.field = [[0] * y_size for _ in range(x_size)]
        self.x_size = x_size
        self.y_size = y_size
        self.status_move = 0

    def add(self, hero, x, y):
        if x >= self.x_size or x < 0 or y > self.y_size or y < 0:
            print("Bad indexes!")
            return False
        elif self.field[x][y] != 0:
            print("Cell not is empty!")

    def move(self, x, y, x_now, y_now):
        hero = self.field[x][y]
        hero: Union[Hero, int]
        if hero != 0:
            if hero.team == self.status_move:
                enemy = self.field[x_now, y_now]
                enemy: Hero
                if enemy != 0:
                    if enemy.team == self.status_move:
                        return False
                    else:
                        result = self.fight(hero, enemy)
                        self.field[x_now][y_now] = result
                        return True
                else:
                    self.field[x][y] = 0
                    self.field[x_now][y_now] = hero
                    if self.status_move == 0:
                        self.status_move = 1
                    else:
                        self.status_move = 0
                    return True
            else:
                return False
        return False

    def game(self):
        while True:
            print(f"Ходит команда{self.status_move}")
            x, y = map(int, input().split())
            x_now, y_now = map(int, input().split())
            self.move(x, y, x_now, y_now)
            count_0 = 0
            count_1 = 0
            for i in range(self.x_size):
                for j in range(self.y_size):
                    if self.field[i][j] != 0:
                        if self.field[i][j].team == 0:
                            count_0 += 1
                        else:
                            count_1 += 1
            if count_0 == 0:  # доработать со скилами и способностями
                print('Team 1 win!')
                break
            elif count_1 == 0:
                print('Team 0 win!')
                break

