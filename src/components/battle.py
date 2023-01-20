import logging
from queue import Queue
from typing import List, Type

from conditions import AliveCreature
from creatures import Creature

logger = logging.getLogger(__name__)


class Battle:

    members: list = []
    queue: Queue = Queue()

    def add_creature(self, creature, add_hp, initiative):

        hp = creature.start_hp + add_hp
        creature.change_condition(AliveCreature(hp))
        creature.set_initiative(initiative)

        Battle.members.append(creature)

    def finish(self):

        Battle.members = []
        Battle.queue = Queue()

    def sort(self):
        Battle.members.sort(key=lambda x: x.initiative)
