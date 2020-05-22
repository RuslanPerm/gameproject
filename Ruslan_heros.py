import random
from time import sleep
from Hero import Strength
from Hero import Agility
from Hero import Intelligence


class Wolfova(Strength):
    def __init__(self, team):
        super().__init__(25, 1, 24)
        self.skills = [self.jump, self.avoid]

    def jump(self):
        pass

    def avoid(self, enemy_hero):
        # как проверить ударил ли противник?
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


class Trushechkinov(Agility):
    def __init__(self, team):
        super().__init__(20, 25, 5)
        self.skills = [self.victoria, self.finish_him]

    def victoria(self, enemy_hero):
        enemy_hero.health -= self.damage + random.uniform(-0.5, 2)
        self.health += random.uniform(-0.5, 2)
        # у героя увиличивается урон и хп

    def finish_him(self, enemy_hero):
        if enemy_hero.health < 100:
            enemy_hero.health = 0
        # добивание случайного противника со здоровьем меньше 100 в радиусе


class Oleg(Intelligence):
    def __init__(self, team):
        super().__init__(8, 15, 27)
        self.skills = [self.sharads, self.guitar]

    def sharads(self, enemy_hero):
        k = random.uniform(0.1, 0.126)
        enemy_hero.int -= self.damage * k
        self.int += self.damage * k
        # крадёт врага части интелекта

    def guitar(self, lst_of_heroes):
        teammates = []
        for h in lst_of_heroes:
            if h.team == self.team:
                teammates.append(h)
        # все союзники хиляться
        for hero in teammates:
            hero.health += (hero.damage / random.randint(25, 40)) * self.p_mag


class Dogg(Agility):
    def __init__(self, team):
        super().__init__(17, 18, 15)
        self.skills = [self.kick, self.dual_life]

    def kick(self, enemy_hero):
        enemy_hero.health -= self.damage

    def dual_life(self):
        if (self.health >= 0) or (self.health <= 20):
            self.health += self.ag * 10
