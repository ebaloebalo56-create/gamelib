from gamelib.entities.entity import Entity
from gamelib.assets.dropfromanything import DropFromAnything
from gamelib.assets.ai.autocontroller import Autocontroller

class Mob(Entity):
    def __init__(self, hp, entityID, entityName, entityTransform, entitySprite, entityHitbox, mobAutocontroller: Autocontroller | None = None, drop: list[DropFromAnything] | None = None):
        super().__init__(entityID, entityName, entityTransform, entitySprite, entityHitbox)
        self.mobAutocontroller =  mobAutocontroller
        self.drop = drop
        self.hp = hp