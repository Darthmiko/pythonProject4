#créé par Enzo Sanchez Valero et Mikolai Szychowski
#créé le 10\01\24
#TP4


import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Balle():
    def __init__(self, x,y,change_x, change_y):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        x = random.randint(0,50)
        y = random.randint(0,50)
        change_x = 1
        change_y = 1


    def on_draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


    class MyGame(arcade.Window):
        def __init__(self):
            super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Exercice #1')
            self.liste_balle = []

        def setup(self):

            pass

        def on_draw(self):
            arcade.start_render()
            for i in self.liste_balle:
                i.on_draw()

        def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
            ball = Balle(x,y, random(0,50), random(0,50))
            self.liste_balle.append(ball)

Balle(1, 1, 1, 1)

