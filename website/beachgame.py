import sys
sys.path.insert(-1, "C:\\Users\\sfo\\AppData\\Local\\Programs\\Python\\Python37-32\\include")
import pygame
sys.path.insert(-1, "C:\\Users\\sfo\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages")
import arcade
import random
import os
import time
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_trash = 0.2
trash_COUNT = 4
straw_COUNT = 4

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Beach Game"


class MyGame(arcade.Window):


    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


        self.player_list = None
        self.trash_list = None
        self.straw_list=None


        self.player_sprite = None
        self.score = 0


        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SAND)

    def setup(self):
        """ Set up the game and initialize the variables. """


        self.player_list = arcade.SpriteList()
        self.trash_list = arcade.SpriteList()
        self.straw_list = arcade.SpriteList()


        self.score = 0

        self.player_sprite = arcade.Sprite("bear.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)


        for i in range(trash_COUNT):

            trash = arcade.Sprite("bottle.png", SPRITE_SCALING_trash)
            trash.center_x = random.randrange(SCREEN_WIDTH)
            trash.center_y = random.randrange(SCREEN_HEIGHT)
            self.trash_list.append(trash)

        for i in range (straw_COUNT):
            straw = arcade.Sprite("straw.png", SPRITE_SCALING_trash)
            straw.center_x = random.randrange(SCREEN_WIDTH)
            straw.center_y = random.randrange(SCREEN_HEIGHT)
            self.straw_list.append(straw)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.trash_list.draw()
        self.player_list.draw()
        self.straw_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        self.trash_list.update()
        self.straw_list.update()
        trashs_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.trash_list)
        straw_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.straw_list)
        for trash in trashs_hit_list:
            trash.kill()
            self.score += 1
            if self.score == 8:
                time.sleep(1)
                window.close()
                break
        for straw in straw_hit_list:
            straw.kill()
            self.score+= 1
            if self.score == 8:
                time.sleep(1)
                window.close()
                break


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
