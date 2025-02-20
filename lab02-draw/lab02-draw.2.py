# Import the "arcade" library
import arcade



# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(1800, 1000, "Mi-dibujo")

# Set the background color
arcade.set_background_color(arcade.color.FRENCH_SKY_BLUE)
# Get ready to draw
arcade.start_render()

# Sun
def sun():
    arcade.draw_circle_filled(0, 1000, 150, arcade.color.SUNSET)

# Plane
def plane():
    arcade.draw_ellipse_filled(575, 550, 200, 50, arcade.color.WHITE_SMOKE, -30)
    arcade.draw_ellipse_filled(500, 500, 400, 75, arcade.color.WHITE)
    arcade.draw_ellipse_filled(425, 425, 200, 50, arcade.color.WHITE_SMOKE, -30)

# Torres
def torres():
    arcade.draw_rectangle_filled(1700, 0, 200, 1700, arcade.color.BATTLESHIP_GREY)
    arcade.draw_rectangle_filled(1600, 0, 200, 1500, arcade.color.ASH_GREY)

# Ventanas de torres
def ventanas(x01, y01, x02, y02):
    for i in range(10):
        for j in range(4):
            arcade.draw_rectangle_filled(x01 + (j * 40), i * y01, 35, 35, arcade.color.DAVY_GREY)

    for k in range(8):
        arcade.draw_rectangle_filled(x02 + (k*40), y02, 25, 25, arcade.color.WHITE_SMOKE)

def draw_image_hulk():
    # Carga la textura de la imagen (asegúrate de cambiar la ruta a la imagen correcta)
    texture = arcade.load_texture("hulk.png")
    # Dibuja la imagen en una posición específica
    arcade.draw_texture_rectangle(1400, 850, texture.width // 4, texture.height // 4, texture)

draw_image_hulk()
sun()
plane()
torres()
ventanas(1533, 75, 350, 500)
arcade.run()