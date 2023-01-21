import logging
from queue import Queue
from typing import List, Type

from src.components.conditions import AliveCreature

logger = logging.getLogger(__name__)


class Members:

    def __init__(self):
        self.members = []
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

    def clear(self):
        self.members = []

    def add(self, obj):
        self.members.append(obj)

    def sort(self):
        self.members.sort(key=lambda x: x.initiative, reverse=True)


class Battle:

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(Battle, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.members = Members()
        self.active_member = None

    def add(self, creature, initiative, add_hp=0):

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
        self.members = Members()
        self.active_member = None
        print('Battle finished!')
