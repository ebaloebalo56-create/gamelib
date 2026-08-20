from gamelib.core.world.generators.worldgenerator import WorldGenerator
from perlin_noise import PerlinNoise
import random
import copy

class PerlinNoiseGenerator(WorldGenerator):
    def __init__(self, worldWidth, worldHeight, worldBlocks: dict):
        super().__init__(worldWidth, worldHeight)
        self.worldBlocks = worldBlocks
        self.generatedWorld = []
        self.noise = PerlinNoise(octaves=4, seed=random.randint(0, 999999))
    def perlinnoisegenerator(self):
        scale = 20.0

        for wh in range(self.worldHeight):
            row = []
            for ww in range(self.worldWidth):
                noiseValue = self.noise([wh / scale, ww / scale])

                blockTemplate = self.pickBlock(noiseValue)
                newblock = copy.copy(blockTemplate)
                newblock.blockTransform = copy.deepcopy(blockTemplate.blockTransform)
                newblock.blockTransform.posX = wh * 32
                newblock.blockTransform.posY = ww * 32
                row.append(newblock)
            self.generatedWorld.append(row)
            
    def pickBlock(self, noiseValue):
        for block, threshold in self.worldBlocks:
            if noiseValue <= threshold:
                    return block
        return block
