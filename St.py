import random
from time import sleep
from Hero import Strength
from Hero import Intelligence



class Tank(Strength):

    def __init__(self, _st, _ag, _int):
        super(Strengtha).__init__(_st, _ag, _int):
        self.skills =[self.protection,self.madman]

    def protection(self):
        self.health += enemy_hero.damage
    # 100% защита от удара

    def madman(self):
        bool = random.uniform(0, 100)
        self.health -= bool
        self.damage += bool
        # сносит рандомно кол-во хп протиивнку и при этом наност себе слолько же


class ShieldDearer(Intelligence):

     def __init__(self, _st, _ag, _int):
         super(Strengtha).__init__(_st, _ag, _int):
         self.skills = [self.potion, pass ]

     def potion(self, _int):
         enemy_hero._int -= random.uniform(0, 10)
     # Понижает шанс выпода скла у противнка
