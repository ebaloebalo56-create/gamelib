from gamelib.assets.id import ID
from gamelib.assets.hitbox import Hitbox
from gamelib.assets.sprite import Sprite
from gamelib.assets.transform import Transform
from gamelib.assets.dropfromanything import DropFromAnything

class Block:
    def __init__(self, blockID: ID, blockName: str, blockTransform: Transform | None = None, blockSprite: Sprite | None = None, blockHitbox: Hitbox | None = None, isPlaceble: bool | None = None, isPlacebleOnOtherBlock: bool | None = None, blockDrop: DropFromAnything | None = None):
        self.blockID = blockID
        self.blockName = blockName
        self.blockTransform = blockTransform
        self.blockSprite = blockSprite
        self.blockHitbox = blockHitbox
        self.blockDrop = blockDrop