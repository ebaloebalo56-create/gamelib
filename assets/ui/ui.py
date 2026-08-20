import pyray
from pyray import *
from gamelib.assets.sprite import Sprite
from gamelib.assets.transform import Transform

class UI:
    def __init__(self, UISprite: Sprite, UITransform: Transform):
        self.UISprite = UISprite
        self.UITransform = UITransform
        self.isVisible = True
        self.isEnable = True    
        self.isHovered = False
        self.UIRect = Rectangle(self.UITransform.posX, self.UITransform.posY, self.UIWidth, self.UIHeight)
    def uiupdate(self, mousePos):
        if not self.isVisible or not self.isEnable:
            self.isHovered = False
            return
        self.UIRect.x = self.UITransform.posX
        self.UIRect.y = self.UITransform.posY
        self.isHovered = check_collision_point_rec(mousePos, self.UIRect)