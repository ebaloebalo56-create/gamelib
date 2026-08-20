from item import Item

class Tool(Item):
    def __init__(self, itemID, itemName, itemCount, maxCount, description, itemSprite, actionRadius, breakingPower: int):
        super().__init__(itemID, itemName, itemCount, maxCount, description, itemSprite, actionRadius)
        self.breakingPower = breakingPower