import dictionary, hashtable, singly_linked_list
import sorted_list_of_tuples, sorted_singly_linked_list
import trie, binary_search_tree
# import time

def analyseGenerationOfDictionary(textfile):
	_sum = 0
	for i in range(100):
		_sum += dictionary.generateHistogramFromFile(textfile)
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfDictionary(textfile):
	_sum = 0
	dictionaryHistogram = dictionary.generateHistogramFromFile(textfile)
	for i in range(100):
		_sum += dictionaryHistogram.count(word, dictionaryHistogram)
	avg = _sum / 100
	return avg 

def analyseGenerationOfSortedListOfTuples(textfile):
	_sum = 0
	for i in range(100):
		_sum += sorted_list_of_tuples.generateHistogramFromFile(textfile)
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfSortedListOfTuples(textfile):
	_sum = 0
	dictionaryHistogram = dictionary.generateHistogramFromFile(textfile)
	for i in range(100):
		_sum += dictionaryHistogram.count(word, dictionaryHistogram)
	avg = _sum / 100
	return avg 

if __name__ == "__main__":
	print "Analysing dictionary ... \n\n"
	avgDict = analyseGenerationOfDictionary(textfile)
	print "--- Generation of dictionary - %s seconds ---" % avgDict
	avgDict = analyseCountFunctionOfDictionary(textfile)
	print "--- Count function of dictionary - %s seconds ---" % avgDict

	print "\n\n"

	print "Analysing sorted list of tuples ... \n\n"
	avgSortedTuples = analyseGenerationOfSortedListOfTuples(textfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedTuples
	avgSortedTuples = analyseCountFunctionOfDictionary(textfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % a

	print "\n\n"

	

	