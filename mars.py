from probe import Probe


class MarsMatrix:
    def __init__(self, lines, columns):
        self.lines_number = lines
        self.columns_number = columns
        self.probes_list = []

    def insert_probe(self, line, column, pointing, movements):
        probe = Probe(line, column, pointing, movements, self.lines_number, self.columns_number)
        self.probes_list.append(probe.get_probe_coordinates())

    def print_probes(self):
        for probe in self.probes_list:
            print(*probe)
