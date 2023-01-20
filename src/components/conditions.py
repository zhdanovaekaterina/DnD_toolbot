import logging
from abc import ABCMeta

logger = logging.getLogger(__name__)


class Condition(metaclass=ABCMeta):
    pass


class AliveCreature(Condition):

    def __init__(self, hp: int):
        self.current_hp = hp

    def __repr__(self):
        return f'Alive, current hp: {self.hp}'

    def hit(self, hp: int):
        self.hp -= hp

    def heal(self, hp: int):
        self.hp += hp


class NotStableCreature(Condition):

    def __init__(self):
        self.success_throws = 0
        self.fail_throws = 0

    def __repr__(self):
        return 'Dead'

    def add_success(self):
        self.success_throws += 1

    def add_fail(self, critical: bool = False):
        self.fail_throws += 2 if critical else 1


class StableCreature(Condition):

    def __repr__(self):
        return 'Stable'


class DeadCreature(Condition):

    def __repr__(self):
        return 'Not stable'


class InactiveCreature(Condition):

    def __repr__(self):
        return 'Inactive'


if __name__ == '__main__':
    pass
