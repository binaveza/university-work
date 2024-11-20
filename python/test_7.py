# import pandas as pd
# import numpy as np

# df = pd.DataFrame([[35, 36.6, '37.3', np.nan, 40]], dtype=int)
# print(df[2].dtype)



# import pandas as pd
# import numpy as np

# df = pd.DataFrame([[35, 36.6, '37.3', np.nan, 40]], dtype=float)
# print(df[2].dtype)



# import pandas as pd
# import numpy as np

# df = pd.DataFrame([35, 36.6, '37.3', np.nan, 40])
# print(df.iloc[3].dtype)



# import pandas as pd
# import numpy as np

# df = pd.DataFrame(['35', np.nan, '40'])

# for i in df[0]:
#     print(type(i))




# import pandas as pd

# df = pd.DataFrame([0, 0])
# first_row = df.iloc[0]

# print(first_row)



# import pandas as pd

# df = pd.DataFrame([[0, '0']]).iloc[0]
# print(df.dtype)



# import pandas as pd

# df = pd.DataFrame([[0, '0']]).iloc[0]
# object_type = type(df)

# print(object_type)



#понедельникам, средам и вторникам

import pandas as pd

start_date = '2024-10-28'  
dates = pd.date_range(start=start_date, periods=10, freq='2B')

print(dates)
