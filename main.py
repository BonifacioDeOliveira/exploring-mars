from mars import MarsMatrix


def get_probe_inputs():
    probe_landing_coordinates = input()
    if probe_landing_coordinates:
        probe_movement_coordinates = input()
        return probe_landing_coordinates, probe_movement_coordinates
    else:
        return None, None


def insert_probe(probe_landing_coordinates, probe_movement_coordinates, mars_matrix):
    landing_line, landing_column, pointing_to = probe_landing_coordinates.split()
    mars_matrix.insert_probe(int(landing_line), int(landing_column), pointing_to, probe_movement_coordinates)


line_column = input()
lines_number, columns_number = line_column.split()
mars_matrix = MarsMatrix(int(lines_number), int(columns_number))

while True:
    probe_landing_coordinates, probe_movement_coordinates = get_probe_inputs()
    if probe_landing_coordinates:
        insert_probe(probe_landing_coordinates, probe_movement_coordinates, mars_matrix)
    else:
        mars_matrix.print_probes()
        break
