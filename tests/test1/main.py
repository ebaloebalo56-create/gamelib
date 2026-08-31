from gamelib.core.world.worldcreator import WorldCreator
from gamelib.core.world.generators.perlinnoisegenerator import PerlinNoiseGenerator
from gamelib.blocks.block import Block
from gamelib.assets.transform import Transform
from gamelib.assets.id import ID
from gamelib.assets.sprite import Sprite

def main():
    testblocktransform = Transform(100, 100)
    testblocksprite = Sprite('gamelib\tests\testsprites\testsquare.png')
    testblockid = ID()
    testblock = Block(blockID=testblockid, blockName='testblock', blockTransform=testblocktransform, blockSprite=testblocksprite)

    num = 0
    testworldgenerator = PerlinNoiseGenerator(50, 50, testblock)
    testworldcreator = WorldCreator(dirToSave='gamelib\tests\test1\testsavedworlds', worldDirName=f'world{num+1}', worldGenerator=testworldgenerator)
main()