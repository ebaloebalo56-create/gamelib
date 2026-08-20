import pyray
from gamelib.core.logic import Logic

class Visual:
    def __init__(self):
        pass
    def initwindow(self, windowWidth, windowHeight, windowName):
        pyray.set_config_flags(pyray.ConfigFlags.FLAG_WINDOW_RESIZABLE)
        pyray.init_window(windowWidth, windowHeight, windowName)
        pyray.set_target_fps(60)
    
    def draw(self, logic: Logic):
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        def initcamera():
            camera = logic.camera
            pyray.begin_mode_2d(camera.camera)
        def initcursor():
            cursor = logic.cursor
            pyray.draw_texture_v(cursor.cursorSprite.sprite, 
                                 pyray.Vector2(cursor.mousePos.x, cursor.mousePos.y), 
                                 pyray.WHITE)
        def drawworld():
                for row in logic.world.generatedWorld:
                    for block in row:
                        pyray.draw_texture_v(
                            block.blockSprite.sprite,
                            pyray.Vector2(block.blockTransform.posX, block.blockTransform.posY),
                            pyray.WHITE
                        )

        initcamera()
        initcursor()
        drawworld()
        for p in logic.players:
            pyray.draw_texture_v(p.entitySprite.sprite, pyray.Vector2(p.entityTransform.posX, p.entityTransform.posY), pyray.WHITE)
        for m in logic.mobs:
            pyray.draw_texture_v(m.entitySprite.sprite, pyray.Vector2(m.entityTransform.posX, m.entityTransform.posY), pyray.WHITE)

        pyray.end_mode_2d
        pyray.end_drawing()
