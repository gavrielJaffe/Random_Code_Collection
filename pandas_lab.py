# import pandas as pd 

# words = pd.Series(['The','quick','fox','jumps','over','the','lazy','dogs'])
# print(words)


import pandas as pd

data = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dogs']
indices = [8, 2, 6, 1, 7, 5, 4, 0, 3]

# Create a Pandas Series with words and indices
s = pd.Series(data, index=indices)

print(s.iloc[0])
print(s.loc[1])
print(s.loc[3]) # dogs 
print(s.iloc[-1]) # dogs 
# print(s.loc[-1]) # dogs 
