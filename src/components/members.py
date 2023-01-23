import logging
from abc import ABC, abstractmethod
from typing import List

from src.components.creatures import Creature

logger = logging.getLogger(__name__)


class Members(ABC):

    @abstractmethod
    def __init__(self):
        self.members: List[Creature] = []
        self.iterator = iter(self.members)

    def __iter__(self):
        return self.iterator

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.members)
            return next(self.iterator)

    def __repr__(self):
        return ', '.join([str(obj) for obj in self.members])

    def __len__(self):
        """
        Возвращает количество живых существ в команде.
        """

        return len([
            creature for creature in self.members if creature.condition
        ])

    def clear(self):
        self.members = []

    def add(self, obj: Creature):
        self.members.append(obj)


class MembersTeam(Members):

    def __init__(self):
        Members.__init__(self)
        self.player_team = PlayerTeam()
        self.monster_team = MonsterTeam()

    def clear(self):
        Members.clear(self)
        self.player_team.clear()
        self.monster_team.clear()

    def add(self, obj):
        Members.add(self, obj)

        match obj.get_classname():
            case 'Player':
                self.player_team.members.append(obj)
            case 'Monster':
                self.monster_team.members.append(obj)
            case _:
                pass  # raise error

    def sort(self):
        self.members.sort(key=lambda x: x.initiative, reverse=True)


class PlayerTeam(Members):

    def __init__(self):
        Members.__init__(self)


class MonsterTeam(Members):

    def __init__(self):
        Members.__init__(self)
