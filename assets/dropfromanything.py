from gamelib.items.item import Item

class DropFromAnything:
    def __init__(self, dropItems: list[Item] | None = None): 
        self.dropItems = dropItems