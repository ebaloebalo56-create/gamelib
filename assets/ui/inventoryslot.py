from gamelib.assets.ui.ui import UI
from gamelib.items.item import Item

class InventorySlot(UI):
    def __init__(self, UISprite, UITransform, inventoryItem: Item):
        super().__init__(UISprite, UITransform)
        self.inventoryItem = inventoryItem