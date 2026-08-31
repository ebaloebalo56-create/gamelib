from gamelib.core.world.generators.worldgenerator import WorldGenerator
import json
import os

class WorldCreator:
    def __init__(self, dirToSave: str, worldDirName: str, worldGenerator: WorldGenerator):
        self.dirToSave = dirToSave
        self.worldDirName = worldDirName
        self.worldGenerator = worldGenerator
    def worldgeneration(self):
        self.worldGenerator.generation()
    def creationfiles(self):
        fullPath = os.path.join(self.dirToSave, self.worldDirName)
        os.mkdir(fullPath)
        with open('world_data.json', 'a', encoding='utf-8') as wd:
            json.dump(self.worldGenerator.generatedWorld)
    def maincreation(self):
        self.worldgeneration()
        self.creationfiles()