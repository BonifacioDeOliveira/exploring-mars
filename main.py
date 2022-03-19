import numpy as np


MOVEMENTS = {'N': {'line': (lambda line: line), 'column': (lambda column: column+1), 'L': 'W', 'R': 'E'},
             'S': {'line': (lambda line: line), 'column': (lambda column: column-1), 'L': 'E', 'R': 'W'},
             'W': {'line': (lambda line: line-1), 'column': (lambda column: column), 'L': 'S', 'R': 'N'},
             'E': {'line': (lambda line: line+1), 'column': (lambda column: column), 'L': 'N', 'R': 'S'}
             }


class Probe():
    def __init__(self, line, column, pointing, movements, line_number, columns_number):
        self.starting_line = line
        self.starting_column = column
        self.starting_pointing = pointing
        self.final_line = None
        self.final_column = None
        self.final_pointing = None
        self.move(movements, line_number, columns_number)

    def move(self, sequence, line_number, columns_number):
        line = self.starting_line
        column = self.starting_column
        pointing = self.starting_pointing

        for movement in sequence:
            if movement in ['L', 'R']:
                pointing = MOVEMENTS[pointing][movement]
            elif movement == 'M':
                iter_line = MOVEMENTS[pointing]['line'](line)
                line = iter_line if iter_line <= line_number else line

                iter_column = MOVEMENTS[pointing]['column'](column)
                column = iter_column if iter_column <= columns_number else column

        self.final_line = line
        self.final_column = column
        self.final_pointing = pointing

    def get_tuple(self):
        return (self.final_line, self.final_column, self.final_pointing)


class MarsMatrix():
    def __init__(self, lines, columns):
        self.zeros_matrix = np.zeros((lines, columns), dtype=int).tolist()
        self.lines_number = lines
        self.columns_number = columns
        self.probes = []

    def insert_probe(self, line, column, pointing, movements):
        probe = Probe(line, column, pointing, movements, self.lines_number, self.columns_number)
        self.probes.append(probe.get_tuple())

    def print_probes(self):
        for probe in self.probes:
            line, column, pointing = probe
            print(line, column, pointing)


def get_inputs():
    probe_position_pointing = input()
    if probe_position_pointing == '0':
        return None, None
    movements = input()
    return probe_position_pointing, movements


line_column = input()
lines_number = int(line_column[0])
columns_number = int(line_column[2])
mars_matrix = MarsMatrix(lines_number, columns_number)

while True:
    probe_position, movements = get_inputs()
    if probe_position:
        line, column, pointing = probe_position.split()
        mars_matrix.insert_probe(int(line), int(column), pointing, movements)
    else:
        mars_matrix.print_probes()
        break