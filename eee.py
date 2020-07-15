import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'EEAAEEEA Arcade'
RADIUS = 150

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

arcade.draw_circle_filled(150, 150, 150, arcade.color.PINK)
arcade.draw_circle_filled(SCREEN_WIDTH - 150, 150, 150, arcade.color.PINK)
arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50, 400, arcade.color.PINK)
arcade.draw_triangle_filled(
    SCREEN_WIDTH / 2 - 50, 600,
    SCREEN_WIDTH / 2 + 50, 600,
    SCREEN_WIDTH / 2, 750,
    arcade.color.PINK
)

arcade.finish_render()

arcade.run()
