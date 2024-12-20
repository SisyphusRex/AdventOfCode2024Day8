"""map module"""


class Map:
    """map class"""

    class Location:
        """location class"""

        def __init__(self, original_value: str, x_index: int, y_index: int):
            self.antenna = None
            self.antinode: bool = False
            self.evaluate_original_value(original_value)
            self.x_index = x_index
            self.y_index = y_index

        def __str__(self):
            if self.antenna:
                return f"{self.antenna}"
            else:
                return "."

        def get_coords(self):
            """return x and y index"""
            return self.x_index, self.y_index

        def evaluate_original_value(self, original_value: str) -> None:
            """takes the input string and assigns antenna"""
            if original_value != ".":
                self.antenna = original_value

    def __init__(self, map_input: list[list[str]]):
        self.antennas: dict[str, list] = {}
        self.map = self.transform_input_to_location_map(map_input)

    def transform_input_to_location_map(
        self, my_input: list[list[str]]
    ) -> list[list[Location]]:
        """takes 2d array and produces 2d array of locations"""
        location_map = []
        for y_index, row in enumerate(my_input):
            new_row = []
            for x_index, value in enumerate(row):
                new_location = self.Location(value, x_index, y_index)
                if new_location.antenna:
                    self.add_antenna_to_dict(new_location)
                new_row.append(new_location)
            location_map.append(new_row)
        return location_map

    def __str__(self):
        """string method"""
        map_str = ""
        for row in self.map:
            row_str = ""
            for location in row:
                row_str = row_str + str(location)
            row_str = row_str + "\n"
            map_str = map_str + row_str
        return map_str

    def print_antinodes(self):
        """show antinodes on map"""
        map_str = ""
        for row in self.map:
            row_str = ""
            for location in row:
                if location.antinode:
                    row_str = row_str + "#"
                else:
                    row_str = row_str + "."
            row_str = row_str + "\n"
            map_str = map_str + row_str
        print(map_str)

    def add_antenna_to_dict(self, location: Location) -> None:
        """adds location to dict"""
        if location.antenna in self.antennas:
            current_list = self.antennas.get(location.antenna)
            current_list.append(location)
            self.antennas[location.antenna] = current_list
        else:
            new_list = [location]
            self.antennas[location.antenna] = new_list

    def find_antinodes_for_each_antenna_part_1(self):
        """finds pairs and adds antinodes to location"""
        for key in self.antennas:
            locations_of_antenna = self.antennas.get(key)
            for location in locations_of_antenna:
                for location2 in locations_of_antenna:
                    if location.get_coords() != location2.get_coords():
                        self.find_antinodes_and_assign(location, location2)

    def find_antinodes_and_assign(
        self, location1: Location, location2: Location
    ) -> None:
        """find antinode of two locations"""
        diff_y = location2.y_index - location1.y_index
        diff_x = location2.x_index - location1.x_index
        first_antinode_y = location1.y_index - diff_y
        first_antinode_x = location1.x_index - diff_x
        second_antinode_y = location2.y_index + diff_y
        second_antinode_x = location2.x_index + diff_x
        first_antinode_location = self.get_location(first_antinode_x, first_antinode_y)
        second_antinode_location = self.get_location(
            second_antinode_x, second_antinode_y
        )
        if first_antinode_location:
            first_antinode_location.antinode = True
        if second_antinode_location:
            second_antinode_location.antinode = True

    def get_location(self, x_index, y_index) -> Location:
        """gets location from indexes"""
        if y_index >= 0 and x_index >= 0:
            try:
                my_location = self.map[y_index][x_index]
            except IndexError:
                return None
            return my_location
        else:
            return None

    def count_antinodes(self) -> int:
        """count antinodes in map"""
        count = 0
        for row in self.map:
            for location in row:
                if location.antinode:
                    count += 1
        return count

    def find_antinodes_for_each_antenna_part_2(self):
        """finds pairs and adds antinodes to location"""
        for key in self.antennas:
            locations_of_antenna = self.antennas.get(key)
            for location in locations_of_antenna:
                for location2 in locations_of_antenna:
                    if location.get_coords() != location2.get_coords():
                        self.find_antinodes_and_assign_2(location, location2)

    def find_antinodes_and_assign_2(
        self, location1: Location, location2: Location
    ) -> None:
        """find antinode of two locations"""
        first_antinodes = []
        second_antinodes = []

        diff_y = location2.y_index - location1.y_index
        diff_x = location2.x_index - location1.x_index

        first_count = 1
        first_counting = True
        while first_counting:
            first_antinode_y = location1.y_index - (diff_y * first_count)
            first_antinode_x = location1.x_index - (diff_x * first_count)
            first_antinode_location = self.get_location(
                first_antinode_x, first_antinode_y
            )
            if first_antinode_location:
                first_antinodes.append(first_antinode_location)
                first_count += 1
            else:
                first_counting = False

        second_count = 1
        second_counting = True
        while second_counting:
            second_antinode_y = location2.y_index + (diff_y * second_count)
            second_antinode_x = location2.x_index + (diff_x * second_count)
            second_antinode_location = self.get_location(
                second_antinode_x, second_antinode_y
            )
            if second_antinode_location:
                second_antinodes.append(second_antinode_location)
                second_count += 1
            else:
                second_counting = False

        for antinode_location in first_antinodes:
            antinode_location.antinode = True
        for antinode_location in second_antinodes:
            antinode_location.antinode = True

        self.get_non_singular_antenna_antinodes()

    def get_non_singular_antenna_antinodes(self):
        """assign antinodes to antenna locations that arent singular"""
        for key in self.antennas:
            locations_of_antenna = self.antennas.get(key)
            if len(locations_of_antenna) > 1:
                for location in locations_of_antenna:
                    location.antinode = True
