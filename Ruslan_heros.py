import random
from time import sleep
from Hero import Strength
from Hero import Agility
from Hero import Intelligence


class Wolfova(Strength):
    def __init__(self, team):
        super().__init__(25, 1, 24)
        self.skills = [self.siren, self.avoid]
        # как сделать шанс прокания?

    def siren(self, enemy_hero):
        enemy_hero.health -= 10 * random.uniform(1, 4)
        sleep(5)
        # все, включая её замирают в радиусе, враги получают урон

    def avoid(self, enemy_hero):
        # как проверить ударил ли противник?
        self.health += enemy_hero.damage
        # шанс полностью игнорировать урон от атаки, шанс зависит от кол-ва здоровья
        # (больше здоровья, меньше шанс)


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
        # шанс выстрелить молнией в случайного противника в радиусе


class Oleg(Intelligence):
    def __init__(self, team):
        super().__init__(8, 15, 27)
        self.skills = [self.sharads, self.punk_hair]

    def sharads(self, enemy_hero):
        enemy_hero.p_mag -= self.damage * random.uniform(0.1, 0.126)

    def guitar(self, teammate):
        # все союзники хиляться
        teammate.health += (teammate.damage / random.randint(25, 40)) * self.p_mag
