class Board:
    def __init__(self, x_size, y_size):
        self.field = [[0] * y_size for _ in range(x_size)]
        self.x_size = x_size
        self.y_size = y_size
        self.hero_list = []
        self.team_list = []
        self.team_dict = {}
        self.field = [[], []]
        self.status_move = 0

    def fight(self, hero, enemy):
        while True:
            hero.stun_status -= 1 if hero.stun_status > 0 else hero.strike(enemy)
            if (hero.health < 0) and (enemy.health < 0):
                condition = self.check_hero_health()
                if condition == 'конец':
                    return None
                return False
            hero, enemy = enemy, hero

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

    def heroes_status(self):
        for hero in self.hero_list:
            print(f"{hero.name} ({hero.team}): [{hero.x}, {hero.y}], {hero.health} HP", sep="\n")

    def check_team(self):
        for i in range(len(self.hero_list) - 1):
            for j in range(i + 1, len(self.hero_list)):
                if (self.hero_list[i].x == self.hero_list[j].x) and (self.hero_list[i].y == self.hero_list[j].y):
                    if self.hero_list[i].team == self.hero_list[j].team:
                        return 'ally'
                    condition = self.fight(self.hero_list[i], self.hero_list[j])
                    if condition is None:
                        return 'break'
                    return False
        return True

    def check_hero_health(self):
        for hero in self.hero_list:
            if hero.health < 0:
                print(f'{hero.name} ({hero.team}) was killed.\n')
                self.hero_list.remove(hero)
                self.team_dict[hero.team].remove(hero)
                condition = self.game()
                if condition is None:
                    return 'end'

    def move(self, hero):
        command = input().lower()
        while True:
            if command == 'вверх':
                if hero.x < 1:
                    print('Тут так-то стена.', end="\n")
                else:
                    hero.x = hero.x - 1
                    step_status = self.check_team()
                    if step_status == 'ally':
                        print('Тут уже союзник стоит.', end="\n")
                    else:
                        return step_status
            elif command == 'вниз':
                if hero.x == self.x_size:
                    print('Тут так-то стена.', end="\n")
                else:
                    hero.x = hero.x + 1
                    step_status = self.check_team()
                    if step_status == 'ally':
                        print('Тут уже союзник стоит.', end="\n")
                    else:
                        return step_status
            elif command == 'вправо':
                if hero.y == self.y_size:
                    print('Тут так-то стена')
                else:
                    hero.y = hero.y + 1
                    step_status = self.check_team()
                    if step_status == 'ally':
                        print('Тут уже союзник стоит.\n')
                    else:
                        return step_status

            elif command == 'влево':
                if hero.y < 1:
                    print('Тут так-то стена.', end="\n")
                else:
                    hero.y = hero.y - 1
                    step_status = self.check_team()
                    if step_status == 'ally':
                        print('Тут уже союзник стоит.', end="\n")
                    else:
                        return step_status
            elif command == "здоровье":
                self.heroes_status()
            elif command == 'остановочка':
                return False
            elif command == 'закрыть':
                return 'break'
            else:
                print('Используйте команды "вверх", "вниз", "влево", "вправо"')

    # def game(self):
    #     while True:
    #         print(f"Ходит команда{self.status_move}")
    #         x, y = map(int, input().split())
    #         x_now, y_now = map(int, input().split())
    #         self.move(x, y, x_now, y_now)
    #         count_0 = 0
    #         count_1 = 0
    #         for i in range(self.x_size):
    #             for j in range(self.y_size):
    #                 if self.field[i][j] != 0:
    #                     if self.field[i][j].team == 0:
    #                         count_0 += 1
    #                     else:
    #                         count_1 += 1
    #         if count_0 == 0:  # доработать со скилами и способностями
    #             print('Team 1 win!')
    #             break
    #         elif count_1 == 0:
    #             print('Team 0 win!')
    #             break

    def game(self):
        self.team_add()
        while True:
            step_status = True
            for hero in self.hero_list:
                step_status = True
                print(f'\nTeam {hero.team} turn. \n{hero.name} has started moving.\n')
                while (self.status_move < 3) and step_status:
                    self.status_move += 1
                    step_status = self.move(hero)
                    if step_status is False:
                        step_status = False
                        break
                self.status_move = 0
                if step_status is False:
                    break
            if step_status is False:
                break