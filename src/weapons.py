"""
This is a template for the weapons. They can be added onto other parts.
"""

from dice import *

class Weapon(object):
    def __init__(self,name="",damage=0,shots=0,dice_color=None):
        self.name = name
        self.damage = damage
        self.dice = Dice(color=dice_color)

    def __str__(self):
        return "%s: %d damage"%(self.name,self.damage)

    def fire(self):
        return [self.dice.roll().value,self.damage]

class Antimatter_cannon(Weapon):
    def __init__(self):
        Weapon.__init__(self,"Antimatter Cannon",4,"Red")

class Ion_cannon(Weapon):
    def __init__(self):
        Weapon.__init__(self,"Ion Cannon",1,"Yellow")

class Plasma_cannon(Weapon):
    def __init__(self):
        Weapon.__init__(self,"Plasma Cannon",2,"Orange")

if __name__ == '__main__':
    ic = Ion_cannon()
    print ic.fire()
    pc = Plasma_cannon()
    print pc.fire()
    ac = Antimatter_cannon()
    print ac.fire()
