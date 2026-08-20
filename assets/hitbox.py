from gamelib.assets.transform import Transform
import pyray

class Hitbox:
    def __init__(self, hitboxPos: Transform, hitboxWidth: float, hitboxHeight: float):
        self.hitboxPosX = hitboxPos.posX
        self.hitboxPosY = hitboxPos.posY
        self.hitboxWidth = hitboxWidth
        self.hitboxHeight = hitboxHeight
    def hitboxInit(self):
        return pyray.Rectangle(self.hitboxPosX, self.hitboxPosX, self.hitboxWidth, self.hitboxHeight)
    def isHit(self, other):
        return pyray.check_collision_recs(self.hitboxInit(), other.hitboxInit())
        