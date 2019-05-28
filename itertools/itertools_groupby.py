#!/usr/bin/env python3
"""Using groupby()
"""

#end_pymotw_header
from itertools import *
from operator import itemgetter

d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
di = sorted(d.iteritems(), key=itemgetter(1))
for k, g in groupby(di, key=itemgetter(1)):
    print(k, map(itemgetter(0), g))
