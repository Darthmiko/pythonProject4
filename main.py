#créé par Enzo Sanchez Valero et Mikolai Szychowski
#créé le 10\01\24
#TP4


import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Exercice #1')
        pass

    def setup(self):

        pass

    def on_draw(self):
        arcade.start_render()

        pass

    def main():
        my_game = MyGame()
        my_game.setup()

        arcade.run()

        main()

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Tutoriel Arcade')

    arcade.run()

main()
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Tutoriel Arcade')

    arcade.run()


main()
import arcade


class Balle(arcade.window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

def main():

    window = Balle(640, 480, "Drawing Example")

    arcade.run()


main()

def on_draw(self):
    """
    
    """

    arcade.start_render()

    arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))