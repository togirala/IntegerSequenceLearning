import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

testData = pd.read_csv('C:\Users\I854540\WorkSpace\IntegerSequenceLearning\data\\train.csv')

# count = 0
# for i in testData.iterrows():
# 	count = count+1

# print count


for eachRow in range(len(testData)):
	completeString = testData.Sequence[eachRow]
	splitString = completeString.split(',')
	for eachElement in range(len(splitString)-1):
		difference = splitString[(eachElement+1)] - splitString[eachElement]
		print difference
print(splitString)
#   splitString = completeString.split("/")


# testData.Sequence


# pd.set_option('display.max_colwidth',-1)
# print testData.Sequence