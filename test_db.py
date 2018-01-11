# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

import db

db.init()

rows = db.get_records2(date(2018,1,1), '162545180')
for i, r in enumerate(rows):
    #_r = map(lambda x: x.decode('GB2312'), r)
    print i, r[0:-1], r[-1]


x = [1, 2, 3, 4, 5]
y1 = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 3, 5, 7, 9]

y = np.vstack([y1, y2, y3])

labels = ["Fibonacci ", "Evens", "Odds"]

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3, labels=labels)
ax.legend(loc=2)
plt.show()

fig, ax = plt.subplots()
ax.stackplot(x, y)
plt.show()