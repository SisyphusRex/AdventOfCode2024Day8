"""map module"""


class Map:
    """map class"""

    class Location:
        """location class"""

        def __init__(self, original_value: str):
            self.antenna = None
            self.antinode = None
            self.evaluate_original_value(original_value)

        def __str__(self):
            if self.antenna:
                return f"{self.antenna}"
            else:
                return "."

        def evaluate_original_value(self, original_value: str) -> None:
            """takes the input string and assigns antenna"""
            if original_value != ".":
                self.antenna = original_value

    def __init__(self, map_input: list[list[str]]):
        self.map = self.transform_input_to_location_map(map_input)

    def transform_input_to_location_map(
        self, my_input: list[list[str]]
    ) -> list[list[Location]]:
        """takes 2d array and produces 2d array of locations"""
        location_map = []
        for y_index, row in enumerate(my_input):
            new_row = []
            for x_index, value in enumerate(row):
                new_location = self.Location(value)
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
