class Board(object):

    def __init__(self, len_side, size_cell):

        lst = []

        for y in range(len_side):

            for x in range(len_side):

                lst.append([x * size_cell, y * size_cell])

        self.board_list = lst
        self.len_side, self.size_cell = len_side, size_cell

    def board_cells(self):

        return self.board_list, self.len_side, self.size_cell
