# class Condition:
#
#     VALID_NAMES = ['alive', 'dead', 'stabled', 'not_stabled']
#
#     def __init__(self, name):
#
#         if name not in Condition.VALID_NAMES:
#             error_text = f'Param "name" should be one of these items: {Condition.VALID_NAMES}'
#             raise TypeError(error_text)
#
#         self.name = name
#         print(self.name)


from abc import ABCMeta


class Condition(metaclass=ABCMeta):
    pass


class AliveCreature(Condition):

    def __init__(self, hp: int):
        self.hp = hp

    def __repr__(self):
        return f'Alive, current hp: {self.hp}'

    def hit(self, hp: int):
        self.hp -= hp

    def heal(self, hp: int):
        self.hp += hp


class NotStabledCreature(Condition):

    def __init__(self):
        self.success_throws = 0
        self.fail_throws = 0

    def __repr__(self):
        return 'Dead'

    def add_success(self, num):
        self.success_throws += num

    def add_fail(self, num):
        self.fail_throws += num


class StabledCreature(Condition):

    def __repr__(self):
        return 'Stable'


class DeadCreature(Condition):

    def __repr__(self):
        return 'Not stable'


if __name__ == '__main__':
    pass
