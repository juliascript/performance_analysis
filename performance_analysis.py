import dictionary, list_of_tuples, sorted_list_of_tuples
import hashtable, singly_linked_list#, sorted_singly_linked_list
import doubly_linked_list, trie, binary_search_tree
import re, time

def analyseGenerationOfDictionary(iterable):
	start_time = time.time()
	_sum = 0
	for i in range(100):
		dictogram = dictionary.Dictogram(iterable)
		_sum += time.time() - start_time
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfDictionary(iterable, word):
	_sum = 0
	dictionaryHistogram = dictionary.Dictogram(iterable)
	for i in range(100):
		_sum += dictionaryHistogram.count(word)
	avg = _sum / 100
	return avg 

def analyseGenerationOfListOfTuples(iterable):
	start_time = time.time()
	_sum = 0
	for i in range(100):
		listogram = list_of_tuples.Listogram(iterable)
		_sum += time.time() - start_time
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfListOfTuples(iterable, word):
	_sum = 0
	listOfTuplesHistogram = list_of_tuples.Listogram(iterable)
	for i in range(100):
		_sum += listOfTuplesHistogram.count(word)
	avg = _sum / 100
	return avg 

def analyseGenerationOfSortedListOfTuples(iterable):
	start_time = time.time()
	_sum = 0
	for i in range(100):
		histogram = sorted_list_of_tuples.generateHistogramFromFile(iterable)
		_sum += time.time() - start_time
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfSortedListOfTuples(iterable, word):
	_sum = 0
	dictionaryHistogram = dictionary.Dictogram(iterable)
	for i in range(100):
		_sum += dictionaryHistogram.count(word)
	avg = _sum / 100
	return avg 

def analyseGenerationOfHashTable(iterable):
	start_time = time.time()
	_sum = 0
	hashtableHistogram = hashtable.HashTable()
	for i in range(100):
		for word in iterable:
			histogram = hashtableHistogram.set(word)
			_sum += time.time() - start_time
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfHashTable(iterable, word):
	_sum = 0
	hashtableHistogram = hashtable.HashTable()
	for i in range(100):
		_sum += hashtableHistogram.get(word)
	avg = _sum / 100
	return avg 

def analyseGenerationOfSinglyLinkedList(iterable):
	start_time = time.time()
	_sum = 0
	for i in range(100):
		histogram = singly_linked_list.LinkedList(iterable)
		_sum += time.time() - start_time
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfSinglyLinkedList(iterable, word):
	_sum = 0
	singlyLinkedListHistogram = singly_linked_list.LinkedList(iterable)
	for i in range(100):
		_sum += singlyLinkedListHistogram.find(lambda node: node[0] == word)
	avg = _sum / 100
	return avg 

# def analyseGenerationOfSortedSinglyLinkedList(iterable):
	# start_time = time.time()
# 	_sum = 0
# 	for i in range(100):
# 		histogram = singly_linked_list.LinkedList(iterable)
		# _sum += time.time() - start_time
# 	avg = _sum / 100
# 	return avg 

# def analyseCountFunctionOfSortedSinglyLinkedList(iterable, word):
# 	_sum = 0
# 	sortedSinglyLinkedListHistogram = singly_linked_list.LinkedList(iterable)
# 	for i in range(100):
# 		_sum += hashtableHistogram.find(lambda node: node[0] == word)
# 	avg = _sum / 100
# 	return avg

def analyseGenerationOfDoublyLinkedList(iterable):
	start_time = time.time()
	_sum = 0
	for i in range(100):
		histogram = doubly_linked_list.DoublyLinkedList(iterable)
		_sum += time.time() - start_time
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfDoublyLinkedList(iterable, word):
	_sum = 0
	doublyLinkedListHistogram = doubly_linked_list.DoublyLinkedList(iterable)
	for i in range(100):
		_sum += doublyLinkedListHistogram.find(lambda node: node[0] == word)
	avg = _sum / 100
	return avg 

def analyseGenerationOfTrie(iterable):
	start_time = time.time()
	_sum = 0
	for i in range(100):
		histogram = trie.generateTrieFromWordsArrayAndCountRepititions(iterable)
		_sum += time.time() - start_time
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfTrie(iterable, word):
	_sum = 0
	trieHistogram = trie.generateTrieFromWordsArrayAndCountRepititions(iterable)
	for i in range(100):
		_sum += trie.isWordPresentInTrie(word, trieHistogram)
	avg = _sum / 100
	return avg 

if __name__ == "__main__":
	# todo: use timeit module instead of time
	# todo: implement and test sorted linked list
	# todo: implement and test binary search tree
	# todo: implement binary search on all sorted data structures -- beware that you sorted list of tuples by count, not alphabetically

	smallTextfile = open("small_sample_text.txt", "r").read()
	largeTextfile = open("large_sample_text.txt", "r").read()

	cleanSmallText = re.sub("^a-zA-Z", "", smallTextfile)
	smallTextArray = cleanSmallText.strip().join(" ")

	cleanLargeText = re.sub("^a-zA-Z", "", largeTextfile)
	largeTextArray = cleanLargeText.strip().join(" ")

	print "Analysing dictionary ... \n\n"
	print "With a small text file ... \n\n"
	avgDict = analyseGenerationOfDictionary(smallTextArray)
	print "--- Generation of dictionary - %s seconds ---" % avgDict
	avgDict = analyseCountFunctionOfDictionary(smallTextArray, "mind")
	print "--- Count function of dictionary - %s seconds --- \n" % avgDict
	print "With a large text file ... \n\n"
	avgDict = analyseGenerationOfDictionary(largeTextArray)
	print "--- Generation of dictionary - %s seconds ---" % avgDict
	avgDict = analyseCountFunctionOfDictionary(largeTextArray, "living")
	print "--- Count function of dictionary - %s seconds ---" % avgDict


	print "\n\n"

	print "Analysing list of tuples ... \n\n"
	print "With a small text file ... \n\n"
	avgTuples = analyseGenerationOfListOfTuples(smallTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgTuples
	avgTuples = analyseCountFunctionOfListOfTuples(smallTextArray, "mind")
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgTuples
	print "With a large text file ... \n\n"
	avgTuples = analyseGenerationOfListOfTuples(largeTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgTuples
	avgTuples = analyseCountFunctionOfListOfTuples(largeTextArray, "living")
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgTuples

	print "\n\n"

	print "Analysing sorted list of tuples ... \n\n"
	print "With a small text file ... \n\n"
	avgSortedTuples = analyseGenerationOfSortedListOfTuples(smallTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedTuples
	avgSortedTuples = analyseCountFunctionOfSortedListOfTuples(smallTextArray, "mind")
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgSortedTuples
	print "With a large text file ... \n\n"
	avgSortedTuples = analyseGenerationOfSortedListOfTuples(largeTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedTuples
	avgSortedTuples = analyseCountFunctionOfSortedListOfTuples(largeTextArray, "living")
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgSortedTuples

	print "\n\n"

	print "Analysing hash table ... \n\n"
	print "With a small text file ... \n\n"
	avgHashtable = analyseGenerationOfHashTable(smallTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgHashtable
	avgHashtable = analyseCountFunctionOfHashTable(smallTextArray, "mind")
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgHashtable
	print "With a large text file ... \n\n"
	avgHashtable = analyseGenerationOfHashTable(largeTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgHashtable
	avgHashtable = analyseCountFunctionOfHashTable(largeTextArray, "living")
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgHashtable

	print "\n\n"

	print "Analysing singly linked list ... \n\n"
	print "With a small text file ... \n\n"
	avgSinglyLinkedList = analyseGenerationOfSinglyLinkedList(smallTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSinglyLinkedList
	avgSinglyLinkedList = analyseCountFunctionOfSinglyLinkedList(smallTextArray, "mind")
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgSinglyLinkedList
	print "With a large text file ... \n\n"
	avgSinglyLinkedList = analyseGenerationOfSinglyLinkedList(largeTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSinglyLinkedList
	avgSinglyLinkedList = analyseCountFunctionOfSinglyLinkedList(largeTextArray, "living")
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgSinglyLinkedList

	print "\n\n"

	# print "Analysing sorted singly linked list ... \n\n"
	# print "With a small text file ... \n\n"
	# avgSortedSinglyLinkedList = analyseGenerationOfSortedSinglyLinkedList(smallTextArray)
	# print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedSinglyLinkedList
	# avgSortedSinglyLinkedList = analyseCountFunctionOfSortedSinglyLinkedList(smallTextArray, "mind")
	# print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgSortedSinglyLinkedList
	# print "With a large text file ... \n\n"
	# avgSortedSinglyLinkedList = analyseGenerationOfSortedSinglyLinkedList(largeTextArray)
	# print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedSinglyLinkedList
	# avgSortedSinglyLinkedList = analyseCountFunctionOfSortedSinglyLinkedList(largeTextArray, "living")
	# print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgSortedSinglyLinkedList

	# print "\n\n"

	print "Analysing doubly linked list ... \n\n"
	print "With a small text file ... \n\n"
	avgDoublyLinkedList = analyseGenerationOfDoublyLinkedList(smallTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgDoublyLinkedList
	avgDoublyLinkedList = analyseCountFunctionOfDoublyLinkedList(smallTextArray, "mind")
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgDoublyLinkedList
	print "With a large text file ... \n\n"
	avgDoublyLinkedList = analyseGenerationOfDoublyLinkedList(largeTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgDoublyLinkedList
	avgDoublyLinkedList = analyseCountFunctionOfDoublyLinkedList(largeTextArray, "living")
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgDoublyLinkedList

	print "\n\n"

	print "Analysing trie ... \n\n"
	print "With a small text file ... \n\n"
	avgTrie = analyseGenerationOfTrie(smallTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgTrie
	avgTrie = analyseCountFunctionOfTrie(smallTextArray, "mind")
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgTrie
	print "With a large text file ... \n\n"
	avgTrie = analyseGenerationOfTrie(largeTextArray)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgTrie
	avgTrie = analyseCountFunctionOfTrie(largeTextArray, "living")
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgTrie

	print "\n\n"

	# print "Analysing binary search tree ... \n\n"
	# print "With a small text file ... \n\n"
	# avgBinarySearchTree = analyseGenerationOfHashTable(smallTextArray)
	# print "--- Generation of sorted list of tuples - %s seconds ---" % avgBinarySearchTree
	# avgBinarySearchTree = analyseCountFunctionOfHashTable(smallTextArray, "mind")
	# print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgBinarySearchTree
	# print "With a large text file ... \n\n"
	# avgBinarySearchTree = analyseGenerationOfHashTable(largeTextArray)
	# print "--- Generation of sorted list of tuples - %s seconds ---" % avgBinarySearchTree
	# avgBinarySearchTree = analyseCountFunctionOfHashTable(largeTextArray, "living")
	# print "--- Count function of sorted list of tuples - %s seconds ---" % avgBinarySearchTree

	# print "\n\n"

	