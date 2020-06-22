import numpy as np
import pandas as pd
from pandas import Series,DataFrame


recipe_dframe = DataFrame(np.arange(10).reshape((2,5)),columns=['apple','grape','bannana','orange','peach'])
print(recipe_dframe)

# print(recipe_dframe['apple'][1])
l = []

#amount:
# 0:全く入っていない〜10:100%入っている。　これを比で表す
