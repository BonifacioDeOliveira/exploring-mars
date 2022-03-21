MOVEMENTS = {'N': {'line': (lambda line_index: line_index),
                   'column': (lambda column_index: column_index+1), 'L': 'W', 'R': 'E'},
             'S': {'line': (lambda line_index: line_index),
                   'column': (lambda column_index: column_index-1), 'L': 'E', 'R': 'W'},
             'W': {'line': (lambda line_index: line_index-1),
                   'column': (lambda column_index: column_index), 'L': 'S', 'R': 'N'},
             'E': {'line': (lambda line_index: line_index+1),
                   'column': (lambda column_index: column_index), 'L': 'N', 'R': 'S'}
             }


class Probe():
    def __init__(self, landing_line, landing_column, pointing_to, movements, line_number, columns_number):
        self.starting_line = landing_line
        self.starting_column = landing_column
        self.starting_pointing_to = pointing_to.upper()

        self.final_line = None
        self.final_column = None
        self.final_pointing_to = None

        self.move_probe(movements, line_number, columns_number)

    def move_probe(self, sequence, line_number, columns_number):
        line = self.starting_line
        column = self.starting_column
        points_to = self.starting_pointing_to

        for movement in sequence:
            movement = movement.upper()
            if movement in ['L', 'R']:
                points_to = MOVEMENTS[points_to][movement]
            elif movement == 'M':
                iter_line = MOVEMENTS[points_to]['line'](line)
                line = iter_line if iter_line <= line_number else line

                iter_column = MOVEMENTS[points_to]['column'](column)
                column = iter_column if iter_column <= columns_number else column

        self.final_line = line
        self.final_column = column
        self.final_pointing_to = points_to

    def get_probe_coordinates(self):
        return self.final_line, self.final_column, self.final_pointing_to
