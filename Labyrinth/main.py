from Labyrinth import Labyrinth
from Mouse import Mouse


def main(argv):
    argv = ['', 'Labyrinths/Laby7.txt']
    labyrinth = Labyrinth.load_from_file(argv[1])
    mouse = Mouse(labyrinth)

    while not mouse.has_reached_exit():
        mouse.move()
        print(mouse)


if __name__ == '__main__':
    import sys
    main(sys.argv)
