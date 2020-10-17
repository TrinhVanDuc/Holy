# coding: utf-8
# license: GPLv3
from gameunit import *
class Hero(Attacker):
    def __init__(self, name):
        self._health = 100
        self._attack = 50
        self._espenriense = 0
    def attack(self, target):
        target._health = target_health - self._attack
        Hero += 1
    def gameOver(self):
        return self._health <= 0


#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
