from mars import MarsMatrix


def get_probe_inputs():
    probe_landing_coordinates = input()
    if probe_landing_coordinates == '':
        return None, None
    probe_movement_coordinates = input()
    return probe_landing_coordinates, probe_movement_coordinates


line_column = input()
lines_number = int(line_column[0])
columns_number = int(line_column[2])
mars_matrix = MarsMatrix(lines_number, columns_number)

while True:
    probe_landing_coordinates, probe_movement_coordinates = get_probe_inputs()
    if probe_landing_coordinates:
        line, column, pointing_to = probe_landing_coordinates.split()
        mars_matrix.insert_probe(int(line), int(column), pointing_to, probe_movement_coordinates)
    else:
        mars_matrix.print_probes()
        break
