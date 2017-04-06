from enum import Enum


class Direction(Enum):
    Down = 1,
    Left = 2,
    Right = 3,
    Up = 4

    @staticmethod
    def next_left(value):
        if value == Direction.Down:
            return Direction.Right
        elif value == Direction.Left:
            return Direction.Down
        elif value == Direction.Up:
            return Direction.Left
        else:
            return Direction.Up

    @staticmethod
    def next_right(value):
        if value == Direction.Down:
            return Direction.Left
        elif value == Direction.Left:
            return Direction.Up
        elif value == Direction.Up:
            return Direction.Right
        else:
            return Direction.Down
