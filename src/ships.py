"""
This file contains the ship parent class as well as child classes for each of the the ships.
"""

import parts as ship_parts

class Ship(object):
    def __init__(self,name="",parts=None):
        self.name = name
        self.parts = parts

    def __str__(self):
        partsstring = "\t"
        if self.parts is not None:
            for i,p in zip(range(len(self.parts)),self.parts):
                partsstring = partsstring+str(i)+". "+p.name+"\n\t"
        return "%s:\n%s"%(self.name,partsstring)

    def swap(self,part,index):
        if self.parts is None:
            raise Exception("Swap attempted with no parts.")
        if index > len(self.parts) or index < 0:
            raise Exception("Swapped part index is invalid.")
        self.parts[index] = part
        return

    def attack(self):
        if self.parts is None:
            raise Exception("Cannot fire with no parts.")
        aim = 0
        weaponlist = []
        barrage = []
        for part in self.parts:
            aim+=part.aim
            if part.weapons is not None:
                for weapon in part.weapons:
                    weaponlist.append(weapon)
        for weapon in weaponlist:
            shot = weapon.fire()
            shot.append(shot[0]+aim)
            barrage.append(shot)
        return barrage

class Interceptor(Ship):
    def __init__(self):
        Ship.__init__(self,name="Interceptor",parts=[ship_parts.Blank(),ship_parts.Ion_cannon(),ship_parts.Nuclear_drive(),ship_parts.Nuclear_source()])


if __name__ == '__main__':
    ship = Ship(name="test",parts=[ship_parts.Blank(),ship_parts.Ion_cannon()])
    print ship
    ic = Interceptor()
    print ic
    ic.swap(ship_parts.Ion_cannon(),0)
    print ic
    print ic.attack()
