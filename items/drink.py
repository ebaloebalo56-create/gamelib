from item import Item

class Drink(Item):
    def __init__(self, itemID, itemName, itemCount, maxCount, description, itemSprite, actionRadius, thirstRecovery):
        super().__init__(itemID, itemName, itemCount, maxCount, description, itemSprite, actionRadius)
        self.thirstRecovery = thirstRecovery