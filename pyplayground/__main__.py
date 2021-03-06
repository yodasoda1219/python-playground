import os, sys
import pygame, pygame.font, pygame.mixer, pygame.event
import pygame.locals as pygame_constants
from pyplayground import *
if not pygame.font: print("fonts have been disabled; whoops")
if not pygame.mixer: print("sound has been disabled; whoops")
pygame.init()
window_size = (800, 600)
display = Display(window_size, "pyplayground window")
scene = Scene()
manager = TileManager(display)
manager.load("assets/scenes/initial-scene.yml")
test_object = GameObject((50, 50))
test_object.pos = (50, 0)
sprite_component = AnimatedSpriteComponent.create_from_yaml("paladin", display)
sprite_component.play(sprite_component.get_animation_by_name("walk-horizontal"), True)
test_object.add_component(sprite_component)
scene.add(test_object)
while True:
    for event in pygame.event.get():
        if event.type in (pygame_constants.QUIT, pygame_constants.KEYDOWN):
            sys.exit()
    scene.update()
    manager.update()
    scene.render(display)
    manager.render(display)
    display.update()