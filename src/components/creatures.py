import logging
from abc import ABC, abstractmethod

from src.components.conditions import Condition, InactiveCreature

logger = logging.getLogger(__name__)


class Creature(ABC):

    @abstractmethod
    def __init__(self,
                 name,
                 hp,
                 armour_class,
                 ):
        self.name = name
        self.condition: Condition = InactiveCreature()
        self.start_hp = hp
        self.armour_class = armour_class
        self.initiative = 0
        self.is_chosen = False

    def __repr__(self):
        return f'type: {type(self)}, ' \
               f'name: {self.name}, ' \
               f'condition: {self.condition}, ' \
               f'start_hp: {self.start_hp}, ' \
               f'armour_class: {self.armour_class}, ' \
               f'initiative: {self.initiative}'

    @classmethod
    def get_classname(cls):
        return cls.__name__

    def change_condition(self, new_condition: Condition):

        if type(self.condition) == type(new_condition):
            logging.warning(f'Creature already have condition {new_condition}')
            return

        self.condition = new_condition

    def set_initiative(self, initiative):
        self.initiative = initiative


class Player(Creature):

    def __init__(self, **kwargs):
        Creature.__init__(self, **kwargs)


class Monster(Creature):

    def __init__(self, **kwargs):
        Creature.__init__(self, **kwargs)  # add monster number here with its name


if __name__ == '__main__':
    pass
