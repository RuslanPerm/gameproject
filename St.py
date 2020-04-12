import random
from time import sleep
from Hero import Strength
from Hero import Intelligence



class Tank(Strength):

    def __init__(self, _st, _ag, _int):
        super(Strengtha).__init__(_st, _ag, _int):
        self.skills =[self.protection,self.madman]

    def protection(self):
        pass
    # 100% защита от удара

    def madman(self):
        pass
    # сносит рандомно кол-во хп протиивнку и при этом наност себе слолько же


class ShieldDearer(Intelligence):

     def __init__(self, _st, _ag, _int):
         super(Strengtha).__init__(_st, _ag, _int):
         self.skills = [self.potion,

     def potion(self):
         pass
     # Понижает шанс выпода скла у противнка
