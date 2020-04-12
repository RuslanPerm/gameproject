from random import randint


class Hero:
    def __init__(self, _st, _ag, _int, team):
        self.st = _st
        self.ag = _ag
        self.int = _int
        self.team = team # как распределяются по командам?
        self.health = self.st * 25
        self.p_iv = self.ag / 50 * 80
        self.p_mag = self.int / 50 * 70

    def enemy_detection(self, hero):
        if hero.team == self.team:
            return False
        else:
            return True

    def activate_skill(self):
        if randint.random(100) <= self.p_mag:
            return True
        else:
            return False


class Strength(Hero):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.p_num = 3
        self.damage = _st


class Agility(Hero):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.p_num = 2
        self.damage = _ag


class Intelligence(Hero):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.p_num = 4
        self.damage = _int
