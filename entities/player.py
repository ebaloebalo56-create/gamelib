from gamelib.assets.camera import Camera
from gamelib.entities.entity import Entity
from gamelib.assets.controller import Controller

class Player(Entity):
    def __init__(self, entityID, entityName, entityTransform, entitySprite, entityHitbox, playerHp: int | None = None, playerCamera: Camera | None = None, playerController: Controller | None = None):
        super().__init__(entityID, entityName, entityTransform, entitySprite, entityHitbox)
        self.playerHp = playerHp
        self.playerCamera = playerCamera
        self.playerController = playerController   
    def update(self, deltaTime):
        return super().update(deltaTime)