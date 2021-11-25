import numpy as np
import pandas as pd

arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], 
                
                [1, 2, 50], [2, 1, 150], [2, 2, 200], 
                
                [2, 3, 78], [2, 2, 100]])

df = pd.DataFrame(arr, columns=["id_vendedor", "id_cliente", "valor"])

print(df)

print(df['valor'].groupby(df['id_vendedor']).sum())

# print(np.ndim(arr))

# print(arr.T)
# print(arr.reshape((8,3), order='F'))

# contador = np.arange(10)

# print(contador)
# print(contador.reshape((2,5), order='F'))
# print(contador.reshape((5,2), order='C'))
# print(contador)