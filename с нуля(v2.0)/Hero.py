class Hero(object):

    def __init__(self, _st, _ag, _int, _pwr, x_cell, y_cell, team):

        self.stamina, self.agility, self.intelect = _st, _ag, _int
        self.healh = 100 + self.stamina * 10
        self.evasion = 10 + self.agility * 7
        self.actuation = 10 + self.intelect * 6
        self.x_cell, self.y_cell = x_cell - 1, y_cell - 1

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
