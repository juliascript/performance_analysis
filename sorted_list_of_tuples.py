import sys
import time
start_time = time.time()

def generateHistogramFromFile(textfile):
	# open text file 
	f = open(textfile, 'r')

	# read the file
	fileContent = f.read()

	# fileContent = fileContent.encode('utf-8', 'ignore')

	# generate array from file content
	wordsArray = fileContent.strip().replace('\n', ' ').split(' ')

	# generate histogram from words array
	histogram = {}
	for word in wordsArray:
		if word in histogram:
			histogram[word] = histogram[word] + 1
		else:
			histogram[word] = 1

	# function called zip --> tuple
	# hash function used to implement dictionaries
	sortedListOfTuples = sorted(histogram.items(), key=operator.itemgetter(1))
	# print("--- %s seconds ---" % (time.time() - start_time))
	# return sortedListOfTuples
	return time.time() - start_time

def count(word, histogram):
	print("--- %s seconds ---" % (time.time() - start_time))
	num = [v for i, v in histogram if i == word]
	# return num
	return time.time() - start_time

if __name__ == "__main__":
	generateHistogramFromFile(sys.argv[1])