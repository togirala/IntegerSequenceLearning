import numpy as np
import pandas as pd
from sklearn import datasets, linear_model


testData = pd.read_csv('test.csv')




pd.set_option('display.max_colwidth',-1)
print testData.Sequence