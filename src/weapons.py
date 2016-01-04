"""
This is a template for the weapons. They can be added onto other parts.
"""

from dice import *

class Weapon(object):
    def __init__(self,name="",damage=0,shots=0,dice_color=None):
        self.name = name
        self.damage = damage
        self.shots = shots
        self.dice = Dice(color=dice_color)

    def __str__(self):
        return "%s: %d damage %d shots"%(self.name,self.damage,self.shots)

    def fire(self):
        barrage = []
        for i in range(self.shots):
            barrage.append([self.dice.roll().value,self.damage])
        return barrage

class Antimatter_cannon(Weapon):
    def __init__(self):
        Weapon.__init__(self,"Antimatter Cannon",4,1,"Red")

class Ion_cannon(Weapon):
    def __init__(self):
        Weapon.__init__(self,"Ion Cannon",1,1,"Yellow")

class Ion_turret(Weapon):
    def __init__(self):
        Weapon.__init__(self,"Ion Turret",1,2,"Yellow")

class Plasma_cannon(Weapon):
    def __init__(self):
        Weapon.__init__(self,"Plasma Cannon",2,1,"Orange")

class Plasma_missiles(Weapon):
    def __init__(self):
        Weapon.__init__(self,"Plasma Missiles",2,2,"Orange")

if __name__ == '__main__':
    ic = Ion_cannon()
    print ic.fire()
    it = Ion_turret()
    print it.fire()
    pc = Plasma_cannon()
    print pc.fire()
    ac = Antimatter_cannon()
    print ac.fire()
    pm = Plasma_missiles()
    print pm.fire()
