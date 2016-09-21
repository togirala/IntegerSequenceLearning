import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

testData = pd.read_csv('C:\Users\I854540\WorkSpace\IntegerSequenceLearning\data\short.csv')

testData['difference'] = ''
testData['SequenceArray'] = ''
def createZerosArray(arraySize):
	difference = np.zeros(arraySize)
	return difference

def computeDifference(splitString):
	differenceArray = createZerosArray(len(splitString)-1)
	for eachElement in range(len(splitString)-1):
	 	differenceArray[eachElement] = round(int(splitString[eachElement+1]) - int(splitString[eachElement]))
	return differenceArray

x = pd.DataFrame(columns=['A'])
y = pd.DataFrame(columns=['A'])
for eachRow in range(len(testData)):
	completeString = testData.Sequence[eachRow]
	splitString = completeString.split(',')
	splitString =[float(i) for i in splitString]
	testData['SequenceArray'].loc[eachRow]  = splitString
	testData['difference'].loc[eachRow] = computeDifference(splitString)
	# print splitString[-1]
	# print splitString[:-1]
	y['A'].loc[eachRow] = splitString[5]

	x['A'].loc[eachRow] = splitString[:5]
	
	# print x['A'].loc[eachRow]
	print eachRow


print x['A']
print y['A']
regr = linear_model.LinearRegression()
regr.fit(x['A'], y['A'])
regr.score(x['A'], y['A'])

