"""
This is a very rough implementation of how a simulated battle should go.
"""

from random import randint as rand
import numpy as np

ntrials = 1
N = 10000
frac = []
for j in range(ntrials):
    iwins, awins = 0,0
    for i in range(N):
        hi = 1
        ha = 1
        di = 0
        da = 0
        gi = 1 #gun level on the interceptor (1 is ion, 2 is plasma)
        ga = 1 #gun level on the ancients

        while di <= hi and da <= ha:
            si = 3 #interceptor speed
            sa = 2 #ancient speed
            ri = [rand(1,6)] #interceptor shot
            ra = [rand(1,6),rand(1,6)] #ancient shots
            ci = 0 #interceptor computer
            ca = 1 #ancient computer
            if si > sa:
                for r in ri:
                    if r+ci >=6:
                        da+=gi
                        if da > ha:
                            iwins+=1
                            break
                    continue
                for r in ra:
                    if r+ca >= 6:
                        di+=ga
                        if di > hi:
                            awins+=1
                            break
                    continue
            else:
                for r in ra:
                    if r+ca >= 6:
                        di+=1
                        if di > hi:
                            awins+=1
                            break
                    continue
                for r in ri:
                    if r+ci >=6:
                        da+=1
                        if da > ha:
                            iwins+=1
                            break
                    continue

    #print iwins, awins
    frac.append(float(iwins)/N*100)
frac = np.array(frac)
meanratio = np.mean(frac)
stddev = np.std(frac)
print meanratio,
