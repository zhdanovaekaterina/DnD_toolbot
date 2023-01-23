import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class Condition(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __bool__(self):
        """
        Возвращает флаг, считается ли экземпляр данного класса живым (т.е. продолжает ли участие в бою).
        """
        pass

    @classmethod
    def get_classname(cls):
        return cls.__name__


class AliveCreature(Condition):

    def __init__(self, hp: int):
        self.hp = hp

    def __bool__(self):
        return True

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

    def __bool__(self):
        return True

    def __repr__(self):
        return 'Dead'

    def add_success(self):
        self.success_throws += 1

    def add_fail(self, critical: bool = False):
        self.fail_throws += 2 if critical else 1


class StableCreature(Condition):

    def __init__(self):
        pass

    def __bool__(self):
        return True

    def __repr__(self):
        return 'Stable'


class DeadCreature(Condition):

    def __init__(self):
        pass

    def __bool__(self):
        return False

    def __repr__(self):
        return 'Not stable'


class InactiveCreature(Condition):

    def __init__(self):
        pass

    def __bool__(self):
        return False

    def __repr__(self):
        return 'Inactive'


if __name__ == '__main__':
    pass
