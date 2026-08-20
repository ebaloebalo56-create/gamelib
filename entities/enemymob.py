from gamelib.entities.mob import Mob

class EnemyMob(Mob):
    def __init__(self, hp, entityID, entityName, entitySprite, entityHitbox, entityTransform, drop, enemyMobDamage):
        super().__init__(hp, entityID, entityName, entitySprite, entityHitbox, entityTransform, drop)
        self.enemyMobDamage = enemyMobDamage