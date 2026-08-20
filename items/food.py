from item import Item

class Food(Item):
    def __init__(self, itemID, itemName, itemCount, maxCount, description, itemSprite, actionRadius, satietyRecovery):
        super().__init__(itemID, itemName, itemCount, maxCount, description, itemSprite, actionRadius)
        self.satietyRecovery = satietyRecovery