# -*- coding: utf-8 -*-

import pandas as pd
import time
from datetime import datetime



def datetime_to_epoch(d):
    return int(time.mktime(d.timetuple()))

def epoch_to_datetime(epoch):
    return datetime(*time.localtime(epoch)[:6])


now = datetime.now()
print (now)

epoch = datetime_to_epoch(now)
print (epoch)

print ( epoch_to_datetime(epoch) )

df1 = pd.DataFrame(
    {'No': ['1', '2', '3', '4', '5'],
     'epoch': [1485812560, 1485812961, 1485813000, 1485813020, 1485813100]
     })
