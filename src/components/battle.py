import logging
from queue import Queue
from typing import List, Type

from src.components.conditions import AliveCreature
from src.components.members import MembersTeam
from src.components.creatures import Creature

logger = logging.getLogger(__name__)


class Battle:

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(Battle, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.members = MembersTeam()
        self.player_team = self.members.player_team
        self.monster_team = self.members.monster_team

        self.active_member = None

    def add(self, creature: Creature, initiative, add_hp=0):

        hp = creature.start_hp + add_hp
        creature.change_condition(AliveCreature(hp))
        creature.set_initiative(initiative)

        self.members.add(creature)

    def start(self):
        self.members.sort()

        count = 0
        while count < 5:
            self.active_member = next(self.members)
            print(self.active_member)
            count += 1

    def finish(self):
        self.members = MembersTeam()
        self.active_member = None
        print('Battle finished!')
