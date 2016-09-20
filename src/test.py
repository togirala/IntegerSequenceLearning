import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

testData = pd.read_csv('C:\Users\I854540\WorkSpace\IntegerSequenceLearning\data\\train.csv')

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

for eachRow in range(len(testData)):
	completeString = testData.Sequence[eachRow]
	splitString = completeString.split(',')
	testData['SequenceArray'].loc[eachRow]  = splitString
	testData['difference'].loc[eachRow] = computeDifference(splitString)



regr = linear_model.LinearRegression()


AIM - get x and y axes for the test and train data and try to see the results of  LinearRegression





	
