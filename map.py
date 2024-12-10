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

    def __init__(self, map_input: list[list[str]]):
        self.map = self.transform_input_to_location_map(map_input)

    def transform_input_to_location_map(
        self, my_input: list[list[str]]
    ) -> list[list[Location]]:
        """takes 2d array and produces 2d array of locations"""
        location_map = []
        for y_index, row in my_input:
            new_row = []
            for x_index, value in row:
                new_location = self.Location(value)
                new_row[x_index]
