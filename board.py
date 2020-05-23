from typing import Union
from Hero import Hero


class Board:
    def __init__(self, x_size, y_size):
        self.field = [[0] * y_size for _ in range(x_size)]
        self.x_size = x_size
        self.y_size = y_size
        self.hero_list = []
        self.team_list = []
        self.team_dict = {}
        self.status_move = 0

    def fight(self, hero, enemy, first_attack):
        if first_attack is True:
            if activate_skill(Hero) is True:
                # юзает рандомный из своих скиллов
                ...
                pass
            else:
                enemy.health -= (hero.damage - enemy.ag * 0.23)
                # обычный удар "enemy.ag * 0.23" - броня
        elif first_attack is False:
            if activate_skill(Hero) is True:
                # юзает рандомный из своих скиллов
                pass
            else:
                hero.health -= (enemy.damage - hero.ag * 0.23)
        pass
    # эскиз для драки выше

    def add(self, hero, x, y):
        self.hero_list.append(hero)
        if x > (self.x_size - 1) or x < 0 or y > (self.y_size - 1) or y < 0:
            print('емае, чё делаешь, выйди и зайди нормально')
            return False
        elif self.field[x][y] != 0:
            print('тут занято')
            return False
        else:
            self.field[x][y] = hero
            hero.x = x
            hero.y = y
            return True

    def team_add(self):
        for hero in self.hero_list:
            if hero.team not in self.team_dict:
                self.team_dict[hero.team] = [hero]
            else:
                self.team_dict[hero.team].append(hero)
            if hero.team not in self.team_list:
                self.team_list.append(hero.team)

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
                        result = self.fight(hero, enemy, first_attack)
                        # последний перешедщий в клетку атакает (возвращает True, если свой атакает и False если враг)
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