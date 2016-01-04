"""
This contains a base class for a ship, and its base attributes, including hull, and loadouts.
"""

import re #Regular expression has better string splitting

class Ship(object):
    
    def __init__(self,name="ship",hull=0,speed=0,power=0):
        self.name = name
        self.hull = int(hull)
        self.speed = int(speed)
        self.power = int(power)
        
    def __str__(self):
        return "%s: hull=%d, speed=%d, power=%d"%(self.name,self.hull,self.speed,self.power)

    def copy(ship):
        parts = re.split(":|,|=",str(ship))
        return Ship(parts[0],parts[2],parts[4],parts[6])
        
if __name__ == '__main__':
    testship = Ship("interceptor",0,1,3)
    print testship
    testship2 = Ship.copy(testship)
    print testship2
