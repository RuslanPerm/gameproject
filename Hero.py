import random


class Hero:
    def __init__(self, _st, _ag, _int, team, name):
        self.st = _st
        self.ag = _ag
        self.int = _int
        self.team = team
        self.name = name
        self.damage = _st / 6
        self.degree_of_dying = 0
        self.health = self.st * 25
        self.p_iv = self.ag / 50 * 80
        self.p_mag = self.int / 50 * 70

    def activate_skill(self, enemy):
        if random.randint(100) <= self.p_mag:
            if bool(random.randint(0, 1)):
                self.skills[0](self, enemy)
            else:
                self.skills[1](self, enemy)


class Strength(Hero):
    def __init__(self, _st, _ag, _int, team, name):
        super().__init__(_st, _ag, _int, team, name)
        self.p_num = 3
        self.damage = _st
        self.skills = [self.avoid, self.madman]

    def avoid(self, enemy_hero):
        chance = 6
        if chance >= random.randint(0, 10):
            if self.health <= 500:
                self.health += enemy_hero.damage
            elif self.health <= 1000:
                self.health += enemy_hero.damage // 2
        else:
            self.health += enemy_hero.damage // 5
        # шанс полностью игнорировать урон от атаки, если здоровья не больше 500
        # шанс игнорировать половину урона от атаки, если здоровья не больше 1000
        # гарантировано блокируется 1/5 урона от атаки

    def madman(self, enemy_hero):
        damage = random.uniform(0, 100)
        if enemy_hero.health < self.health:
            self.health -= damage
        else:
            enemy_hero.health -= damage
            # сносит рандомно кол-во хп протиивнку и при этом наност себе слолько же


class Agility(Hero):
    def __init__(self, _st, _ag, _int, team, name):
        super().__init__(_st, _ag, _int, team, name)
        self.p_num = 2
        self.damage = _ag
        self.skills = [self.victoria, self.finish_him]

    def finish_him(self, enemy_hero):
        if enemy_hero.health < 100:
            enemy_hero.health = 0
        # добивание случайного противника со здоровьем меньше 100 в радиусе

    def victoria(self, enemy_hero):
        enemy_hero.health -= self.damage + random.uniform(-0.5, 2)
        self.health += random.uniform(-0.5, 2)
        # у героя увиличивается урон и хп


class Intelligence(Hero):
    def __init__(self, _st, _ag, _int, team, name):
        super().__init__(_st, _ag, _int, team, name)
        self.p_num = 4
        self.damage = _int
        self.skills = [self.protection, self.sharads]

    def sharads(self, enemy_hero):
        k = random.uniform(0.1, 0.126)
        enemy_hero.int -= self.damage * k
        self.int += self.damage * k
        # крадёт врага части интелекта

    def protection(self, _int):
        example_for_girls = {"1 + 1": 2., "4 - 2": 2., "2 ** 1": 2.}
        example_for_boys = {"log12232,3(323039)": 1.34783, "exp(sin(45°))": 2.02811,
                            "0**0 (с док-вом)": "я пошёл разбираться"}
        name = input('Привет, я заместитель Владимира Алексеевича Трушникова,'
                     'каким бы героем этой мини-игры ты хотел(а) бы быть (Дима/Влад/Руслан/Полина)')
        rate = random.uniform(1, 11)
        if name == 'Полина':
            key, value = example_for_girls.popitem()
            print("Реши пример: ", key)
            if float(input()) == value:
                self.int += rate
                print(f'Ответ верный, ты получаешь {rate} интеллекта .')
            else:
                self.int -= rate * 0.000000001
                print(f'Ответ не верный, ты теряешь {rate * 0.000000001} интеллекта .')
        elif name == 'Дима' or name == 'Влад' or name == "Руслан":
            key, value = example_for_boys.popitem()
            print("Реши пример: ", key)
            if float(input()) == value:
                self.int -= rate * 2
                print(f'Ты списал(а), я видел, ты теряешь {rate * 2} интеллекта .')
            else:
                self.int -= rate
                print(f'Иди разбирайся, теряешь {rate} интеллекта .')
