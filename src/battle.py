"""
This file contains the battle class. A battle class contains two fleets
and facilities to have them both fire, calculate potential damage, and then
state which ships are destroyed.

One day, this will be modified to have a list of fleets that then battle
in a given order according to the game rules, as opposed to simply
comparing two fleets.
"""

import copy as copy_module
import ships
import fleet as fleet_object

class Battle(object):
    def __init__(self,name="",Ofleet=None,Dfleet=None):
        self.name = name
        self.Ofleet = Ofleet
        self.Dfleet = Dfleet
        self.Ofleet_backup = copy_module.deepcopy(Ofleet)
        self.Dfleet_backup = copy_module.deepcopy(Dfleet)

    def __str__(self):
        return "%s:\nOffense: %sDefense: %s"%(self.name,str(self.Ofleet),str(self.Dfleet))

    def get_attacks(self):
        all_attacks = []
        if self.Ofleet is not None:
            all_attacks.append(self.Ofleet.attack())
        if self.Dfleet is not None:
            all_attacks.append(self.Dfleet.attack())
        return all_attacks

if __name__ == '__main__':
    Ofleet = fleet_object.Fleet("Player A",[ships.Interceptor(),ships.Interceptor()])
    Dfleet = fleet_object.Fleet("Player A",[ships.Interceptor()])
    battle = Battle("Test battle",Ofleet,Dfleet)
    print battle
    print battle.get_attacks()
