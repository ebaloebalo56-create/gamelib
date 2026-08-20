from gamelib.assets.transform import Transform
import pyray

class Camera:
    def __init__(self, cameraTransform: Transform, cameraWindowWidth: int, cameraWindowHeight: int, spriteWidth: int | None = None, spriteHeight: int | None = None):
        self.cameraTransform = cameraTransform
        self.camera: pyray.Camera2D = pyray.Camera2D()
        self.cameraWindowWidth =  cameraWindowWidth
        self.cameraWindowHeight = cameraWindowHeight
        self.spriteWidth = spriteWidth
        self.spriteHeight = spriteHeight
    def update(self):
        self.camera.target = pyray.Vector2(
            self.cameraTransform.posX + self.spriteWidth / 2, 
            self.cameraTransform.posY + self.spriteHeight / 2
            )
        self.camera.offset = pyray.Vector2(
            pyray.get_screen_width() / 2,
            pyray.get_screen_height() / 2
        )
        self.camera.rotation = 0
        self.camera.zoom = 1