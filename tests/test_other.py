import logging

from src import config as c
from src.components.battle import Battle
from src.components.conditions import AliveCreature, NotStableCreature, StableCreature, DeadCreature
from src.components.creatures import Player, Monster

logger = logging.getLogger(__name__)
c.enable_logging()


def test_1():
    """Проверяет, что создается только один экземпляр Battle при вызове конструктора несколько раз"""

    x = Battle()
    y = Battle()

    assert x is y
