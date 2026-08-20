from gamelib.assets.sprite import Sprite

class Item:
    def __init__(self, itemID: int, itemName: str, itemCount: int, maxCount: int, description, itemSprite: Sprite, actionRadius):
        self.itemID = itemID
        self.itemName = itemName
        self.itemCount = itemCount
        self.maxCount = maxCount
        self.description = description
        self.actionRadius = actionRadius     
        self.itemSprite = itemSprite