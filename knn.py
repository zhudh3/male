from numpy import *
import operator

def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels


def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]

	print(dataSet)
	print(dataSetSize)

	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat**2

	print(diffMat)
	print(sqDiffMat)

	sqDistances = sqDiffMat.sum(axis=1)

	print(sqDistances)

	distances = sqDistances**0.5

	print(distances)

	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
		print(classCount)
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse=True)
	print(classCount.items())
	print(classCount.iteritems())
	print(sortedClassCount)
	return sortedClassCount[0][0]
