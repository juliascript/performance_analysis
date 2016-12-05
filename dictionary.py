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
	# print("--- %s seconds ---" % (time.time() - start_time))
	# return histogram
	return time.time() - start_time

def count(word, histogram):
	# print("--- %s seconds ---" % (time.time() - start_time))
	num = histogram[word]
	# return num
	return time.time() - start_time

if __name__ == "__main__":
	generateHistogramFromFile(sys.argv[1])

