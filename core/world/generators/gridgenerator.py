from gamelib.core.world.generators.worldgenerator import WorldGenerator
import copy

class GridGenerator(WorldGenerator):
    def __init__(self, worldWidth, worldHeight, floorblock1):
        super().__init__(worldWidth, worldHeight, floorblock1)
        self.generatedWorld = []
    def gridGenerator(self):
        for wh in range(self.worldWidth):
            row = []
            for ww in range(self.worldHeight):
                newfloorblock1 = copy.copy(self.floorblock1)
                newfloorblock1.blockTransform = copy.deepcopy(self.floorblock1.blockTransform)
                newfloorblock1.blockTransform.posX = ww * 32
                newfloorblock1.blockTransform.posY = wh * 32
                row.append(newfloorblock1)
                ww += 1
            self.generatedWorld.append(row)
            wh += 1
