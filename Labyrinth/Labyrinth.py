from Direction import Direction
from Point import Point


class Labyrinth:

    def __init__(self, data, width, height):
        self.__data = data
        self.__width = width
        self.__height = height
        index_of_start = self.__data.index('S')
        self.__start_pos = Point(index_of_start % self.__width, index_of_start // self.__width)
        index_of_end = self.__data.index('X')
        self.__end_pos = Point(index_of_end % self.__width, index_of_end // self.__width)

        self.__directions = [Point(0, 1), Point(-1, 0), Point(1, 0), Point(0, -1)]
        self.__movements = [Direction.Down, Direction.Left, Direction.Right, Direction.Up]

    def get_allowed_directions(self, mouse):
        mouse_position = mouse.get_position()

        allowed_directions = []
        for direction, movement in zip(self.__directions, self.__movements):
            if not self.is_wall(mouse_position + direction):
                allowed_directions.append(movement)

        return allowed_directions

    def get_end_position(self):
        return self.__end_pos

    def get_start_position(self):
        return self.__start_pos

    def is_wall(self, position):
        return self.__data[position.get_x() + position.get_y() * self.__width] == '#'

    def move(self, mouse, direction):
        mouse.set_position(mouse.get_position() + self.__directions[self.__movements.index(direction)])

    @staticmethod
    def load_from_file(file_path):
        width = None
        height = 0
        data = []
        with open(file_path) as f:
            for line in f:
                line = line.strip()
                for c in line:
                    data.append(c)
                width = len(line)
                height += 1

        return Labyrinth(data, width, height)

    def __str__(self, mouse=None):
        result = []
        for i in range(self.__height):
            result.append(self.__data[self.__width * i: self.__width * (i + 1)])

        if mouse is not None:
            mouse_position = mouse.get_position()
            result[mouse_position.get_y()][mouse_position.get_x()] = '^'

        string_result = ""
        for row in result:
            string_result += "".join(row)
            string_result += "\n"
        return string_result
