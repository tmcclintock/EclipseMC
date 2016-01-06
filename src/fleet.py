"""
This file contains the fleet class, which is a collection
for many ships. This has facilities for firing from all ships,
and calculating whether they hit. In addition, it can return
arrays containing information about the ships in the fleet.
"""

import copy as copy_module #Needed to make deep copies of fleets
import parts as ship_parts
import ships

class Fleet(object):
    def __init__(self,name="",shiplist=[]):
        self.name=name
        self.shiplist=shiplist

    def __str__(self):
        shipstring = ""
        if self.shiplist is not None:
            for i,s in zip(range(len(self.shiplist)),self.shiplist):
                shipstring = shipstring+"\t"+str(i)+". "+s.name+"\n"
        return "%s:\n%s"%(self.name,shipstring)

    def add(self,ship):
        self.shiplist.append(ship)

    def copy(self):
        return copy_module.deepcopy(self)

    def remove(self,index):
        self.shiplist.pop(index)

    def sort(self):
        self.shiplist = sorted(self.shiplist)

if __name__ == '__main__':
    fleeta = Fleet("Player A",[ships.Interceptor(),ships.Interceptor()])
    print fleeta
