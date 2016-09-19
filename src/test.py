import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

testData = pd.read_csv('C:\Users\I854540\WorkSpace\IntegerSequenceLearning\data\\train.csv')

# count = 0
# for i in testData.iterrows():
# 	count = count+1

# print count

testData['difference'] = ''
def createDifferenceFeature(arraySize):
	difference = np.zeros(arraySize-1)
	return difference


# def convertDefference(numpyArray):

# 	return concatedString

# difference = np.zeros(range(len(testData)))
for eachRow in range(len(testData)):
	completeString = testData.Sequence[eachRow]
	splitString = completeString.split(',')
	difference = createDifferenceFeature(len(splitString))
	# print len(splitString)
	for eachElement in range(len(splitString)-1):
		difference[eachElement] = round(int(splitString[eachElement+1]) - int(splitString[eachElement]))
	print difference
	# difference = np.chararray(difference)
	# np.array(difference.tolist())
	# print difference
	# print pd.Series.str.len()
	testData.loc[eachRow, 'difference'] = difference
	# testData['differene'] = difference
	print testData.difference







# print(splitString)
#   splitString = completeString.split("/")


# testData.Sequence


# pd.set_option('display.max_colwidth',-1)
# print testData.Sequence