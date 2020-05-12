import random
from time import sleep
from Hero import Agility
from Hero import Intelligence


class Trushechkinov(Agility):
    def __init__(self, team):
        super().__init__(20, 25, 5)
        self.skills = [self.victoria, self.finish_him]

    def deducted_squeal(self, enemy_hero):
        enemy_hero.health -= self.damage + random.uniform(-0.5, 2)
        self.health += random.uniform(-0.5, 2)
        # у героя увиличивается урон и хп

    def finish_him(self, enemy_hero):
        if enemy_hero.health < 100:
            enemy_hero.health = 0
        # шанс выстрелить молнией в случайного противника в радиусе