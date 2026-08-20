import pyray
from gamelib.assets.sprite import Sprite

class Cursor:
    def __init__(self, cursorSprite: Sprite):
        self.cursorSprite = cursorSprite
        self.mousePos = pyray.get_mouse_position()
        pyray.hide_cursor