from pyray import *
from gamelib.assets.ui.ui import UI
from gamelib.assets.sprite import Sprite
from gamelib.assets.transform import Transform

class Button(UI):
    def __init__(self, UISprite: Sprite, buttonSpriteHovered: Sprite, UITransform, mouseButton, buttonAction):
        super().__init__(UISprite, UITransform)
        self.buttonSpriteHovered = buttonSpriteHovered
        self.buttonAction = buttonAction
        self.mouseButton = mouseButton
    def buttonupdate(self):
        if self.isHovered and is_mouse_button_pressed(self.mouseButton):
            self.buttonAction





