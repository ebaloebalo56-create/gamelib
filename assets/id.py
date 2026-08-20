import random

class ID:
    def __init__(self, customid: int | None = None):
        self.customid = customid
        self.idmgmt()
    def idmgmt(self):
        if self.customid is not None:
            self.customid = self.customid
        else:
            self.customid = random.randint(10000000, 99999999)
        return self.customid