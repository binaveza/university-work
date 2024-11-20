# import numpy
# numpy.array([])


# from numpy import *


import datetime as dt

NY = dt.datetime(2025, 1, 1)
d = dt.timedelta(days=50)

result = (NY - d).strftime('%d/%m/%y, %a')
print(result)

