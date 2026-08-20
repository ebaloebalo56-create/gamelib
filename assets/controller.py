import pyray
from gamelib.assets.transform import Transform

class Controller:
    def __init__(self, movementSpeed: float, playerTransform: Transform):
        self.movementSpeed = movementSpeed
        self.playerTransform = playerTransform    
    def update(self, deltaTime):
        if pyray.is_key_down(83):
            self.playerTransform.posY += self.movementSpeed * deltaTime
        if pyray.is_key_down(87):
            self.playerTransform.posY -= self.movementSpeed * deltaTime
        if pyray.is_key_down(68):
            self.playerTransform.posX += self.movementSpeed * deltaTime
        if pyray.is_key_down(65):
            self.playerTransform.posX -= self.movementSpeed * deltaTime

    