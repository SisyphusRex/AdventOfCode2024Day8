"""program module"""

# System Imports

# First Party Imports
from mapper import Map

# Third Party Imports


def main(*args):
    """main method"""
    data_list = get_data("data.txt")
    my_map = Map(data_list)
    print(my_map)
    my_map.find_antinodes_for_each_antenna_part_2()
    my_map.print_antinodes()
    print(my_map.count_antinodes())


def get_data(filename):
    """Reads a maze from a text file and returns it as a list of lists."""
    data = []
    with open(filename, "r") as f:
        for line in f:
            strip_line = line.strip()
            line_list = []
            for element in strip_line:
                line_list.append(element)
            data.append(line_list)
    return data
