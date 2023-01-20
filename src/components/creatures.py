import conditions
from queue import Queue
from abc import ABCMeta


class Creature(metaclass=ABCMeta):
    members = []
    battle_queue = Queue()

    def __init__(self, name, hp, armour_class, initiative):
        self.name = name
        self.condition = conditions.AliveCreature(hp)
        self.start_hp = hp
        self.armour_class = armour_class
        self.initiative = initiative

        self._add_member(self)
        Creature._add_alive(self.__class__)

    @classmethod
    def _add_member(cls, obj):
        cls.members.append(obj)

    @staticmethod
    def _add_alive(cls):
        cls.alive_members += 1

    @staticmethod
    def _remove_alive(cls):
        cls.alive_members -= 1

    def __repr__(self):
        return f'type: {type(self)}\n' \
               f'name: {self.name}\n' \
               f'condition: {self.condition}\n' \
               f'start_hp: {self.start_hp}\n' \
               f'armour_class: {self.armour_class}\n' \
               f'initiative: {self.initiative}\n\n'


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
    player1 = Player(name='Karlin', hp=20, armour_class=17, initiative=20)
    player2 = Player(name='Petr', hp=25, armour_class=18, initiative=15)
    player3 = Player(name='Miriel', hp=22, armour_class=18, initiative=18)
    monster1 = Monster(name='Werwolf', hp=22, armour_class=18, initiative=18)
    monster2 = Monster(name='Werwolf', hp=22, armour_class=18, initiative=18)

    print(Player.alive_members)
    print(Monster.alive_members)
    print(Creature.members)
