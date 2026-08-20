from gamelib.entities.mob import Mob

class PeacefulMob(Mob):
    def __init__(self, hp, entityID, entityName, entityTransform, entitySprite, entityHitbox, mobAutocontroller, drop):
        super().__init__(hp, entityID, entityName, entityTransform, entitySprite, entityHitbox, mobAutocontroller, drop)