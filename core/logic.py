from gamelib.entities.player import Player
from gamelib.entities.entity import Entity
from gamelib.entities.mob import Mob
from gamelib.core.world.generators.worldgenerator import WorldGenerator
from gamelib.core.world.generators.gridgenerator import GridGenerator
from gamelib.core.world.generators.perlinnoisegenerator import PerlinNoiseGenerator
from gamelib.assets.camera import Camera
from gamelib.assets.ui.ui import UI
from gamelib.assets.ui.cursor import Cursor

class Logic():
    def __init__(self):
        pass
    def cursorlogic(self, cursor: Cursor):
        self.cursor = cursor
    def playerslist(self, players: list[Player]):
        self.players = players
    def mobslist(self, mobs: list[Mob]):
        self.mobs = mobs
    def entitieslist(self, entities: list[Entity]):
        self.entities = entities
    def cameralogic(self, camera: Camera):
        self.camera = camera
    def UIlist(self, ui: list[UI]):
        self.ui = ui
    def worldlogic(self, world: WorldGenerator | GridGenerator | PerlinNoiseGenerator):
        self.world = world
    def update(self, deltaTime):
        self.camera.update()
        for p in self.players:
            p.playerController.update(deltaTime)
        for m in self.mobs:
            m.mobAutocontroller.update(deltaTime)
