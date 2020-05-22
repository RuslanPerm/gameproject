import random
from Hero import Strength
from Hero import Intelligence


class Tank(Strength):
    def __init__(self, team):
        super().__init__(35, 10, 5)
        self.skills = [self.protection, self.madman]

    def protection(self):
        pass
    # доделаю завтра

    def madman(self,enemy_hero):
        damage = random.uniform(0, 100)
        if enemy_hero.health < self.health:
            self.health -= damage
        else:
            enemy_hero.health -= damage
        # сносит рандомно кол-во хп протиивнку и при этом наност себе слолько же


class ShieldDearer(Intelligence):

    def __init__(self, _st, _ag, _int):
        super().__init__(11, 17, 22)
        self.skills = [self.potion, self.tebe_hana ]

    def potion(self, enemy_hero):
        enemy_hero.int -= random.uniform(0, 10)
        if (enemy_hero.st < self.int) and (random.uniform(0, 10) < 4):
            self.health += 200
        # если у противникаа _st больше чем твой _int то +ХП

    def tebe_hana(self):
        pass
    # если _st = 30 и выподает рандомм то противник умрает
