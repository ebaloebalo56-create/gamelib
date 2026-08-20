from item import Item

class Weapon(Item):
    def __init__(self, itemID, itemName, itemCount, maxCount, description, itemSprite, actionRadius, weaponDamage: int):
        super().__init__(itemID, itemName, itemCount, maxCount, description, itemSprite, actionRadius)
        self.weaponDamage = weaponDamage