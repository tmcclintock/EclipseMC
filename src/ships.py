"""
This file contains the ship parent class as well as child classes for each of the the ships.
"""

import copy as copy_module #Needed to make deep copies of ships
import parts as ship_parts

class Ship(object):
    def __init__(self,name="",aim=0,initiative=0,power=0,shield=0,parts=[]):
        self.name = name
        self.parts = parts
        self.aim = aim
        self.initiative = initiative
        self.power = power
        self.shield = shield

    def __str__(self):
        partsstring = ""
        if self.parts is not None:
            for i,p in zip(range(len(self.parts)),self.parts):
                partsstring = partsstring+"\t"+str(i)+". "+p.name+"\n"
        return "%s:\n%s"%(self.name,partsstring)

    def __cmp__(self, obj):
        if obj is None or not isinstance(obj,Ship):
            raise Exception("Cannot compare to type "+str(obj)+".")
        return cmp(-self.get_initiative(),-obj.get_initiative())

    def attack(self):
        aim = self.aim
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

    def copy(self):
        return copy_module.deepcopy(self)

    def get_initiative(self):
        init = self.initiative
        for part in self.parts:
            init+=part.initiative
        return init

    def swap(self,part,index):
        if self.parts is None:
            raise Exception("Swap attempted with no parts.")
        if index > len(self.parts) or index < 0:
            raise Exception("Swapped part index is invalid.")
        self.parts[index] = part
        return

class Interceptor(Ship):
    def __init__(self):
        Ship.__init__(self,name="Interceptor",initiative=1,parts=[ship_parts.Blank(),ship_parts.Ion_cannon(),ship_parts.Nuclear_drive(),ship_parts.Nuclear_source()])

if __name__ == '__main__':
    ic = Interceptor()
    print ic
    ic.swap(ship_parts.Plasma_cannon(),0)
    print ic
    cic = ic.copy()
    cic.swap(ship_parts.Electron_computer(),0)
    print ic
    print cic
    print cic.attack()
    print cmp(ic,cic)
