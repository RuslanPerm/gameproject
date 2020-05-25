class Hero(object):

    def __init__(self, _str, _agl, _int, name, team, x_cell, y_cell):
        self.strange, self.agility, self.intellect = _str, _agl, _int
        self.health = self._str * 50
        self.evasion = self._agl * 2
        self.actuation = self._int * 1.6
        self.team = team
        self.name = name
        self.stun_status = 0
        self.x_cell, self.y_cell = x_cell - 1, y_cell - 1
        if self.perk == 'int':
            self.damage_min = _int * 3 - 4
            self.damage_max = _int * 3 + 5
        elif self.perk == 'str':
            self.damage_min = self._str * 2 - 3
            self.damage_max = self._str * 2 + 4
        elif self.perk == 'ag':
            self.damage_min = self._agl * 3 - 5
            self.damage_max = self._agl * 3 + 6

        if team != 'red' and team != 'blue':

            self.team = None

        else:

            self.team = team

        if team == 'red':

            self.color = (255, 0, 0)

        elif team == 'blue':

            self.color = (0, 0, 255)

        else:

            self.color = (125, 125, 125)

    def move_to_pos(self, x_cell, y_cell):

        self.x_cell, self.y_cell = x_cell - 1, y_cell - 1

    def draw_params(self):

        return self.x_cell, self.y_cell, self.color