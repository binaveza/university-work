# import numpy as np

# arr = np.array([35, 36.6, '37.3', 38.5, 40], dtype=np.float16)

# print(arr.dtype)



# import numpy as np

# arr = np.array([35, 36.6, '37.3', 38.5, 40], dtype=np.int16)

# print(arr.dtype)



# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for i in range(arr.shape[0]):
#     print(arr[i])  



# import numpy as np

# vector_row = np.array([1, 2, 3])

# vector_column = vector_row.reshape(-1, 1)



# import numpy as np

# arr = np.arange(10, dtype=int).reshape((10, 1))

# result = arr[3]

# print(result)



# import numpy as np

# arr = np.eye(5) 

# result = arr[0, 0] / arr[1, 0] or 0
# print(result)




# import numpy as np

# arr = np.arange(30)

# matrix_reshape = arr.reshape((5, 6))

# arr.shape = (5, 6)

# arr.resize((5, 6))

# print("Matrix from reshape:\n", matrix_reshape)
# print("Matrix from shape attribute:\n", arr)


import numpy as np

arr = np.arange(10)
result = arr[(arr > 5) & (arr < 8)]  