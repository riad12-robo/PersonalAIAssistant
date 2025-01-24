import pandas as pd
a = [3,2,7]
myvar = pd.Series(a,index =['x','y','z'])
print(myvar)
print(myvar['x'])
