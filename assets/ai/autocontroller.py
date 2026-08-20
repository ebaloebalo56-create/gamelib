from gamelib.assets.transform import Transform
import random

class Autocontroller:
    def __init__(self, movementSpeed: float, autocontrollerTransform: Transform, autocontrollerTimerSeconds: int | None = None):
        self.movementSpeed = movementSpeed
        self.autocontrollerTransform = autocontrollerTransform
        self.maxTimerSeconds = autocontrollerTimerSeconds
        self.currentTimer = autocontrollerTimerSeconds
    def update(self, deltaTime):
        self.currentTimer -= deltaTime

        if self.currentTimer <= 0:
            self.autocontrollerTransform.posX += random.randint(-self.movementSpeed, self.movementSpeed) * deltaTime
            self.autocontrollerTransform.posY += random.randint(-self.movementSpeed, self.movementSpeed) * deltaTime
            self.currentTimer = self.maxTimerSeconds
    