class Board:
    def __init__(self, x_size=15, y_size=15):
        self.field = [[0] * y_size for _ in range(x_size)]
        self.x_size = x_size
        self.y_size = y_size
        self.hero_list = []
        self.team_list = []
        self.team_dict = {}
        self.status_move = 0

    def add(self, hero, x, y):
        self.hero_list.append(hero)
        self.field[x][y] = hero
        hero.x = x
        hero.y = y
        return True

    def fight(self, hero, enemy_hero):
        while True:
            hero.degree_of_dying -= 1 if hero.degree_of_dying > 0 else hero.strike(enemy_hero)
            if (hero.health < 0) and (enemy_hero.health < 0):
                if self.check_hero_health() == 'конец':
                    return None
                return False
            hero, enemy_hero = enemy_hero, hero

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
            print(f"{hero.name} из команды {hero.team}: в точке [{hero.x}, {hero.y}], "
                  f"запас здоровья{hero.health} единиц", sep="\n")

    def check_team(self):
        for i in range(len(self.hero_list) - 1):
            for j in range(i + 1, len(self.hero_list)):
                if (self.hero_list[i].x == self.hero_list[j].x) and (self.hero_list[i].y == self.hero_list[j].y):
                    if self.hero_list[i].team == self.hero_list[j].team:
                        return 'занято'
                    condition = self.fight(self.hero_list[i], self.hero_list[j])
                    if condition is None:
                        return 'стоп'
                    return False
        return True

    def check_hero_health(self):
        for hero in self.hero_list:
            if hero.health < 0:
                print(f'{hero.name} ({hero.team}) погибает.\n')
                print(f'F.\n')
                self.hero_list.remove(hero)
                self.team_dict[hero.team].remove(hero)
                if self.game() is None:
                    return 'конец'
            else:
                return f'{hero.name} имеет {hero.health} хп'

    def move(self, hero):
        command = input().lower()
        while True:
            if command == 'вверх':
                if hero.x < 1:
                    print('Тут так-то стена.', end="\n")
                else:
                    hero.x = hero.x - 1
                    step_status = self.check_team()
                    if step_status == 'занято':
                        print('Тут уже союзник стоит.', end="\n")
                    else:
                        return step_status
            elif command == 'вниз':
                if hero.x == self.x_size:
                    print('Тут так-то стена.', end="\n")
                else:
                    hero.x = hero.x + 1
                    step_status = self.check_team()
                    if step_status == 'занято':
                        print('Тут уже союзник стоит.', end="\n")
                    else:
                        return step_status
            elif command == 'вправо':
                if hero.y == self.y_size:
                    print('Тут так-то стена')
                else:
                    hero.y = hero.y + 1
                    step_status = self.check_team()
                    if step_status == 'занято':
                        print('Тут уже союзник стоит.\n')
                    else:
                        return step_status

            elif command == 'влево':
                if hero.y < 1:
                    print('Тут так-то стена.', end="\n")
                else:
                    hero.y = hero.y - 1
                    step_status = self.check_team()
                    if step_status == 'занято':
                        print('Тут уже союзник стоит.', end="\n")
                    else:
                        return step_status
            elif command == 'остановочка':
                return False
            elif command == 'камаз камаз я на целый час':
                return 'стоп'
            else:
                print('Используйте команды "вверх", "вниз", "влево", "вправо", '
                      '"камаз камаз я на целый час", "остановочка", "здоровье"')

    def game(self):
        self.team_add()
        while True:
            step_status = True
            for hero in self.hero_list:
                step_status = True
                print(f'{hero.name} выбирает куда ступить\n')
                step_status = self.move(hero)
                self.status_move = 0
                if step_status is False:
                    break
            if step_status is False:
                break
