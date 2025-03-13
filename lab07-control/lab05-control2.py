import arcade
import random

from arcade.examples.sprite_face_left_or_right import MOVEMENT_SPEED

# --- Constants ---
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
NUM_STARS = 1000  # Número de estrellas
MOVEMENT_SPEED = 3

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius = 0, color = "White"):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 200, 50, arcade.color.WHITE_SMOKE, -30)
        arcade.draw_ellipse_filled(self.position_x - 75, self.position_y - 75, 400, 75, arcade.color.WHITE)
        arcade.draw_ellipse_filled(self.position_x - 150, self.position_y - 150, 200, 50, arcade.color.WHITE_SMOKE, -30)

    def on_update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x


# Funciones de dibujo (colocadas antes de la clase)
def draw_stars(stars):
    """ Draw stars in the sky """
    for x, y in stars:
        arcade.draw_circle_filled(x, y, 3, arcade.color.STAR_COMMAND_BLUE)


def draw_sun():
    """ Draw the sun """
    arcade.draw_circle_filled(0, SCREEN_HEIGHT, 150, arcade.color.SUNSET)


def draw_plane():
    """ Draw a plane """



def draw_torres():
    """ Draw towers """
    arcade.draw_rectangle_filled(1700, 0, 200, 1700, arcade.color.BATTLESHIP_GREY)
    arcade.draw_rectangle_filled(1600, 0, 200, 1500, arcade.color.ASH_GREY)


def draw_ventanas(x01, y01, x02, y02):
    """ Draw windows on the towers """
    for i in range(10):
        for j in range(4):
            arcade.draw_rectangle_filled(x01 + (j * 40), i * y01, 35, 35, arcade.color.DAVY_GREY)

    for k in range(8):
        arcade.draw_rectangle_filled(x02 + (k * 40), y02, 25, 25, arcade.color.WHITE_SMOKE)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
        self.set_mouse_visible(False)
        # Generar las posiciones de las estrellas una vez
        self.stars = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(NUM_STARS)]
        self.plane = Ball(575, 575, 0, 0)
    def on_draw(self):
        """ Render the screen. """
        self.clear()
        draw_stars(self.stars)
        draw_sun()
        draw_plane()
        draw_torres()
        draw_ventanas(1533, 75, 350, 500)
        self.plane.draw()
    def on_update(self, delta_time):
        self.plane.on_update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.plane.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.plane.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.plane.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.plane.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.plane.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.plane.change_y = 0

def main():
    window = MyGame()
    arcade.run()


main()
