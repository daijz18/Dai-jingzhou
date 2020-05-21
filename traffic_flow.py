import numpy as np
from sklearn.preprocessing import LabelEncoder
x=['a','b','b','c']
x=LabelEncoder().fit_transform(x)
print(x)