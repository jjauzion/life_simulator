import pygame
import math

from src.component import Position
from src.component import Velocity
from src.component import Physic
from src.component import Health
from src import module_fct


class Cell(pygame.sprite.Sprite):

    def __init__(self, cell_id, position, size, vector, life, regen, image):
        pygame.sprite.Sprite.__init__(self)
        self.id = cell_id
        self.component = {
            "position": Position.Position(position),
            "velocity": Velocity.Velocity(vector=vector),
            "physic": Physic.Physic(size),
            "health": Health.Health(life, regen)
        }
        heading = self.component["velocity"].get_heading_rad()
        self.image, self.rect = module_fct.create_cell_image((255, 255, 255), (255, 0, 0), size, heading)
        self.rect.center = position

    def __str__(self):
        return "Cell {}: component : [{}]".format(self.id, self.component)

    def update(self, *args):
        self.rect.center = self.component["position"].get_position()
