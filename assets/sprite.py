import pyray

class Sprite:
    def __init__(self, sprite: str):
        self.sprite = pyray.load_texture(sprite)