#%%
#importing relevant libraries
import pandas as pd
import numpy as np

#%%
## np.ndarray <<<

xx = [3, 8, 9 , 23]
type(xx)

xx + [100]

#%%
heights = [1.75, 1.89, 1.61, 1.58]

heights_arr = np.array(heights)

#%%
heights_arr*100

#%%

type(heights_arr)
#%%
# pandas DataFrames - Data containers, pt 4

# Get a DataFrame when impoting a file

# Or from a dict:
foo1 = [True, False, False, True, True, False]
foo2 = ["Liver", "Brain", "Testes", "Muscle", "Intestine", "Heart"]
foo3 = [13, 88, 1233, 55, 233, 18]

#%%
# Collect list into a dataframe
foo_df = pd.DataFrame({'healthy': foo1, 'tissue': foo2, 'quantity': foo3})
foo_df

#%%
type(foo_df)

#%%
# Or from a list of keys and values:
list_names = ['healthy', 'tissue', 'quantity']
# A list of lists
list_cols = [foo1, foo2, foo3]
# zip put the key/value pairs together
pd.DataFrame(dict(zip(list_names, list_cols)))

#%%
foo_df


#%%
# Access information by:
# Name (here)
# Position (later, indexing)

# columns
foo_df.columns

#%%
# rows
foo_df.index

#%%
foo_df['healthy'] # Series

#%%
type(foo_df['healthy'])

#%%
foo_df[['healthy', 'tissue']]

#%%
foo_df[['healthy']] # DataFrame
type(foo_df[['healthy']])

#%%

type(foo_df.healthy) # a Series

# foo_df[['quantity', 'healthy']] # DataFrame

#%%
# each column is a Series
# DataFrames are build upon np.arrays
# i.e.
#  Series can only be ONE type!
#%%
foo_df.info()

# null
# np.nan << short for not a number 

#%%
foo_df.shape

#%%
foo_df.head(2)
foo_df.tail(2)
foo_df.sample(2)

#%%
foo_df.describe()

#%%
foo_df[['quantity']].describe()

#%%
foo_df.healthy.isnull()

#%%
foo_df.duplicated()

#%%
foo_df.tissue.shape
#%%
foo_df.quantity.mean()
foo_df.tissue.size

#%%
foo_df.tissue.hasnans

#%%
foo_df

foo_df['new_column'] = 0 

#%%
foo_df.drop('new_column', axis=1, in_place=True)
#OR
foo_df = foo_df.drop('new_column', axis=1)

#%%
foo_df['new_column'] = 'one'

#%%
foo_df.dtypes

#%%
## datetime << 18/01/2022 : 00:00:12

date_df  = pd.DataFrame({
'date': ['1920-07-25', '1876-06-13'],
'name': ['Rosaline Franklin', 'William Gosset']
})

#%%

date_df

#%%
date_df.info()

#%%

date_df['date'] = pd.to_datetime(date_df['date'])

#%%

date_df.info()

#%%
date_df['day'] = date_df['date'].dt.day

#%%
date_df
#%%
foo_df

#%%

#how can we access rows of the dataframe?
# 1- using the indices 
# 2- specific conditions (values of the fields)

foo_df.iloc[[2]]

#%%
# df.iloc[rows, columns]
foo_df.iloc[[0, 1], :2]

#%%
##loc 

#%%

foo_df[foo_df.healthy == True]

#%%

foo_df[foo_df.quantity > 233]

#%%

## return dataframe with rows that have
#  value in quantity filed of 233 and less

foo_df[foo_df.quantity <= 233]

#%%
## return dataframe with rows that have
# value in quantity filed of 233 and less
# AND value of True in healthy field

foo_df[(foo_df.quantity <= 233) & (foo_df.healthy == True)]

# AND >>> &
# OR >>> |

## return dataframe with rows that have
# value in quantity filed of 233 and less
# OR value of True in healthy field

foo_df[(foo_df.quantity <= 233) | (foo_df.healthy == True)]

#%%
tissues = ['Brain', 'Heart', 'Liver']

#%%

# is in

foo_df[foo_df['tissue'].isin(tissues)]

foo_df[foo_df['tissue'].isnull()]

foo_df['tissue'].astype('str')
























#%%
quantity_list = foo3.copy()
# quantity_list.mean() # no!
np.mean(quantity_list) # yes :)
# quantity_list/100 # no!

quantity_array = np.array(foo3)
quantity_array.mean()
quantity_array/100
quantity_array.astype("str")
# quantity_array.name # no!

quantity_Series = foo_df['quantity']
quantity_Series.mean()
quantity_Series/100
quantity_Series.astype("str")
quantity_Series.name

test_Series = pd.Series(quantity_array)
test_Series.name = "hello"
test_Series