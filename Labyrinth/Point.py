class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __add__(self, other):
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __str__(self):
        return "({0}, {1})".format(self.__x, self.__y)