from Direction import Direction


class Mouse:

    def __init__(self, labyrinth):
        self.__labyrinth = labyrinth
        self.__current_position = self.__labyrinth.get_start_position()
        self.__direction = Direction.Up
        self.__follow_wall = False
        self.__angular = 0

    def get_position(self):
        return self.__current_position

    def has_reached_exit(self):
        return self.__current_position == self.__labyrinth.get_end_position()

    def move(self):
        if self.__follow_wall and self.__angular == 0:
            self.__follow_wall = False

        allowed_directions = self.__labyrinth.get_allowed_directions(self)
        if not self.__follow_wall:
            if self.__direction in allowed_directions:
                self.__labyrinth.move(self, self.__direction)
            else:
                self.__follow_wall = True
                self.turn_right()
        else:
            left = Direction.next_left(self.__direction)
            if left in allowed_directions:
                self.__labyrinth.move(self, left)
                self.turn_left()
            else:
                loop = 0
                while loop != 3:
                    if self.__direction in allowed_directions:
                        self.__labyrinth.move(self, self.__direction)
                        break
                    else:
                        self.turn_right()
                    loop += 1
                if loop == 3:
                    raise Exception("Infinite loop !")

    def set_position(self, new_position):
        self.__current_position = new_position

    def turn_left(self):
        self.__direction = Direction.next_left(self.__direction)
        self.__angular -= 1

    def turn_right(self):
        self.__direction = Direction.next_right(self.__direction)
        self.__angular += 1

    def __str__(self):
        return self.__labyrinth.__str__(self)
