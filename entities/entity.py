import pyray
from gamelib.assets.transform import Transform
from gamelib.assets.hitbox import Hitbox
from gamelib.assets.sprite import Sprite
from gamelib.assets.id import ID

class Entity:
    def __init__(self, entityID: ID | None = None, entityName: str | None = None, entityTransform: Transform | None = None, entitySprite: Sprite | None = None, entityHitbox: Hitbox | None = None):
        self.entityID = entityID
        self.entityName = entityName
        self.entitySprite = entitySprite
        self.entityHitbox = entityHitbox
        self.entityTransform = entityTransform
    def update(self, deltaTime):
        pass