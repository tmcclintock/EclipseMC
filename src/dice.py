"""
This contains a six sided dice object.
"""

import random

class Dice(object):

    def __init__(self,color="Yellow",value=0):
        self.color = color
        self.value = value

    def __str__(self):
        if self.value==0:
            return "%s dice has not been rolled yet"%self.color
        return "%s dice rolled a %d"%(self.color,self.value)

    def roll(self):
        self.value = random.randint(1,6)
        return self
    
if __name__ == '__main__':
    testdice = Dice("Red")
    print testdice
    testdice.roll()
    print testdice
    testdice = Dice().roll()
    print testdice
