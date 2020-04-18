import random
from Hero import Strength
from Hero import Intelligence



class Tank(Strength):

    def __init__(self, _st, _ag, _int):
        super(Strength).__init__(_st, _ag, _int):
        self.skills =[self.protection,self.madman]

    def protection(self):
        pass
    # доделаю завтра

    def madman(self,enemy_hero):
        if enemy_hero.health < self.health:
        self.health -= random.uniform(0, 100)
        else:
        self.damage += random.uniform(0, 100)
        # сносит рандомно кол-во хп протиивнку и при этом наност себе слолько же


class ShieldDearer(Intelligence):

     def __init__(self, _st, _ag, _int):
         super(Intelligence).__init__(_st, _ag, _int):
         self.skills = [self.potion, self.tebe_hana ]

     def potion(self, enemy_hero):
         enemy_hero.int -= random.uniform(0, 10)
         if enemy_hero.st < self.int and  random.uniform(0, 10) < 4:
             self.health += 200
        #если у противникаа _st больше чем твой _int то +ХП



     def tebe_hana(self):

    # если _st = 30 и выподает рандомм то противник умрает


