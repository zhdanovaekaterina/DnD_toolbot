import logging
from queue import Queue
from abc import ABC, abstractmethod
from typing import Type

from conditions import Condition, InactiveCreature, AliveCreature, DeadCreature

logger = logging.getLogger(__name__)


class Creature(ABC):

    @abstractmethod
    def __init__(self,
                 name,
                 hp,
                 armour_class,
                 ):
        self.name = name
        self.condition = InactiveCreature()
        self.start_hp = hp
        self.armour_class = armour_class
        self.initiative = 0

    def __repr__(self):
        return f'type: {type(self)}\n' \
               f'name: {self.name}\n' \
               f'condition: {self.condition}\n' \
               f'start_hp: {self.start_hp}\n' \
               f'armour_class: {self.armour_class}\n' \
               f'initiative: {self.initiative}\n\n'

    @staticmethod
    def _add_alive(cls):
        cls.alive_members += 1

    @staticmethod
    def _remove_alive(cls):
        cls.alive_members -= 1

    def change_condition(self, new_condition):
        if isinstance(new_condition, AliveCreature):
            if not isinstance(self.condition, AliveCreature):
                self._add_alive(self.__class__)

        elif isinstance(new_condition, DeadCreature):
            if not isinstance(self.condition, DeadCreature):
                self._remove_alive(self.__class__)

        else:
            logging.error(f'Unknown condition {new_condition}')

    def set_initiative(self, initiative):
        self.initiative = initiative


class Player(Creature):
    alive_members = 0

    def __init__(self, **kwargs):
        Creature.__init__(self, **kwargs)


class Monster(Creature):
    alive_members = 0

    def __init__(self, **kwargs):
        Creature.__init__(self, **kwargs)
        self.name = self.name + str(Monster.alive_members)


if __name__ == '__main__':
    # player1 = Player(name='Karlin', hp=20, armour_class=17, initiative=20)
    # player2 = Player(name='Petr', hp=25, armour_class=18, initiative=15)
    # player3 = Player(name='Miriel', hp=22, armour_class=18, initiative=18)
    # monster1 = Monster(name='Werwolf', hp=22, armour_class=18, initiative=18)
    # monster2 = Monster(name='Werwolf', hp=22, armour_class=18, initiative=18)
    #
    # print(Player.alive_members)
    # print(Monster.alive_members)
    # print(Creature.members)

    # player1 = Player(name='Karlin', hp=20, armour_class=17, initiative=20)
    # print(player1)

    player0 = Player(name='Karlin', hp=20, armour_class=17)
    print(Player.alive_members)

    player0.change_condition(AliveCreature(20))
    print(Player.alive_members)

    player1 = Player(name='Petr', hp=25, armour_class=18)
    print(Player.alive_members)

    player1.change_condition(AliveCreature(20))
    print(Player.alive_members)
