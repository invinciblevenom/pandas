import numpy as np
import pandas as pd

np_array = np.array([2012, 2008, 2004, 2006])
dict_ndarray = {'year':np_array}
df_ndarray = pd.DataFrame(dict_ndarray)
print(df_ndarray)
