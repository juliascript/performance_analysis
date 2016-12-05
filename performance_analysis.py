import dictionary, list_of_tuples, sorted_list_of_tuples
import hashtable, singly_linked_list, sorted_singly_linked_list
import doubly_linked_list, trie, binary_search_tree
import large_sample_text, small_sample_text
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

def analyseGenerationOfListOfTuples(textfile):
	_sum = 0
	for i in range(100):
		_sum += list_of_tuples.Listogram(textfile)
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfListOfTuples(textfile):
	_sum = 0
	listOfTuplesHistogram = list_of_tuples.Listogram(textfile)
	for i in range(100):
		_sum += listOfTuplesHistogram.count(word)
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

def analyseGenerationOfHashTable(textfile):
	_sum = 0
	hashtableHistogram = hashtable.HashTable()
	# todo: format words in textfile so that get and set can be called properly
	for i in range(100):
		_sum += hashtableHistogram.set(words)
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfHashTable(textfile):
	_sum = 0
	hashtableHistogram = hashtable.HashTable()
	for i in range(100):
		_sum += hashtableHistogram.get(word)
	avg = _sum / 100
	return avg 

def analyseGenerationOfSinglyLinkedList(textfile):
	_sum = 0
	# todo: format words in textfile so that get and set can be called properly
	for i in range(100):
		_sum += singly_linked_list.LinkedList(words)
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfSinglyLinkedList(textfile):
	_sum = 0
	singlyLinkedListHistogram = singly_linked_list.LinkedList(words)
	for i in range(100):
		_sum += hashtableHistogram.find(lambda node: node[0] == word)
	avg = _sum / 100
	return avg 

# def analyseGenerationOfSortedSinglyLinkedList(textfile):
# 	_sum = 0
# 	# todo: format words in textfile so that get and set can be called properly
# 	for i in range(100):
# 		_sum += singly_linked_list.LinkedList(textfile)
# 	avg = _sum / 100
# 	return avg 

# def analyseCountFunctionOfSortedSinglyLinkedList(textfile):
# 	_sum = 0
# 	sortedSinglyLinkedListHistogram = singly_linked_list.LinkedList(textfile)
# 	for i in range(100):
# 		_sum += hashtableHistogram.find(lambda node: node[0] == word)
# 	avg = _sum / 100
# 	return avg

def analyseGenerationOfDoublyLinkedList(textfile):
	_sum = 0
	# todo: format words in textfile so that get and set can be called properly
	for i in range(100):
		_sum += doubly_linked_list.DoublyLinkedList(words)
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfDoublyLinkedList(textfile):
	_sum = 0
	doublyLinkedListHistogram = doubly_linked_list.DoublyLinkedList(words)
	for i in range(100):
		_sum += doublyLinkedListHistogram.find(lambda node: node[0] == word)
	avg = _sum / 100
	return avg 

def analyseGenerationOfTrie(textfile):
	_sum = 0
	# todo: format words in textfile so that get and set can be called properly
	for i in range(100):
		_sum += trie.generateTrieFromWordsArrayAndCountRepititions(words)
	avg = _sum / 100
	return avg 

def analyseCountFunctionOfTrie(textfile):
	_sum = 0
	trieHistogram = trie.generateTrieFromWordsArrayAndCountRepititions(words)
	for i in range(100):
		_sum += trieHistogram.count(word)
	avg = _sum / 100
	return avg 

if __name__ == "__main__":

	# todo: edit performance analysis for small and large texts
	# todo: fix bug of having the init function of some files return an int instead of a histogram (will affect the testing of the count function)
	# todo: implement and test sorted linked list
	# todo: implement and test binary search tree
	# todo: implement binary search on all sorted data structures 

	smallTextfile = small_sample_text
	largeTextfile = large_sample_text

	print "Analysing dictionary ... \n\n"
	print "With a small text file ... \n\n"
	avgDict = analyseGenerationOfDictionary(smallTextfile)
	print "--- Generation of dictionary - %s seconds ---" % avgDict
	avgDict = analyseCountFunctionOfDictionary(smallTextfile)
	print "--- Count function of dictionary - %s seconds --- \n" % avgDict
	print "With a large text file ... \n\n"
	avgDict = analyseGenerationOfDictionary(largeTextfile)
	print "--- Generation of dictionary - %s seconds ---" % avgDict
	avgDict = analyseCountFunctionOfDictionary(largeTextfile)
	print "--- Count function of dictionary - %s seconds ---" % avgDict


	print "\n\n"

	print "Analysing list of tuples ... \n\n"
	print "With a small text file ... \n\n"
	avgTuples = analyseGenerationOfListOfTuples(smallTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgTuples
	avgTuples = analyseCountFunctionOfListOfTuples(smallTextfile)
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgTuples
	print "With a large text file ... \n\n"
	avgTuples = analyseGenerationOfListOfTuples(largeTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgTuples
	avgTuples = analyseCountFunctionOfListOfTuples(largeTextfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgTuples

	print "\n\n"

	print "Analysing sorted list of tuples ... \n\n"
	print "With a small text file ... \n\n"
	avgSortedTuples = analyseGenerationOfSortedListOfTuples(smallTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedTuples
	avgSortedTuples = analyseCountFunctionOfSortedListOfTuples(smallTextfile)
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgSortedTuples
	print "With a large text file ... \n\n"
	avgSortedTuples = analyseGenerationOfSortedListOfTuples(largeTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedTuples
	avgSortedTuples = analyseCountFunctionOfSortedListOfTuples(largeTextfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgSortedTuples

	print "\n\n"

	print "Analysing hash table ... \n\n"
	print "With a small text file ... \n\n"
	avgHashtable = analyseGenerationOfHashTable(smallTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgHashtable
	avgHashtable = analyseCountFunctionOfHashTable(smallTextfile)
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgHashtable
	print "With a large text file ... \n\n"
	avgHashtable = analyseGenerationOfHashTable(largeTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgHashtable
	avgHashtable = analyseCountFunctionOfHashTable(largeTextfile)
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgHashtable

	print "\n\n"

	print "Analysing singly linked list ... \n\n"
	print "With a small text file ... \n\n"
	avgSinglyLinkedList = analyseGenerationOfSinglyLinkedList(smallTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSinglyLinkedList
	avgSinglyLinkedList = analyseCountFunctionOfSinglyLinkedList(smallTextfile)
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgSinglyLinkedList
	print "With a large text file ... \n\n"
	avgSinglyLinkedList = analyseGenerationOfSinglyLinkedList(largeTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSinglyLinkedList
	avgSinglyLinkedList = analyseCountFunctionOfSinglyLinkedList(largeTextfile)
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgSinglyLinkedList

	print "\n\n"

	# print "Analysing sorted singly linked list ... \n\n"
	# print "With a small text file ... \n\n"
	# avgSortedSinglyLinkedList = analyseGenerationOfSortedSinglyLinkedList(smallTextfile)
	# print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedSinglyLinkedList
	# avgSortedSinglyLinkedList = analyseCountFunctionOfSortedSinglyLinkedList(smallTextfile)
	# print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgSortedSinglyLinkedList
	# print "With a large text file ... \n\n"
	# avgSortedSinglyLinkedList = analyseGenerationOfSortedSinglyLinkedList(largeTextfile)
	# print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedSinglyLinkedList
	# avgSortedSinglyLinkedList = analyseCountFunctionOfSortedSinglyLinkedList(largeTextfile)
	# print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgSortedSinglyLinkedList

	# print "\n\n"

	print "Analysing doubly linked list ... \n\n"
	print "With a small text file ... \n\n"
	avgDoublyLinkedList = analyseGenerationOfDoublyLinkedList(smallTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgDoublyLinkedList
	avgDoublyLinkedList = analyseCountFunctionOfDoublyLinkedList(smallTextfile)
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgDoublyLinkedList
	print "With a large text file ... \n\n"
	avgDoublyLinkedList = analyseGenerationOfDoublyLinkedList(largeTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgDoublyLinkedList
	avgDoublyLinkedList = analyseCountFunctionOfDoublyLinkedList(largeTextfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgDoublyLinkedList

	print "\n\n"

	print "Analysing trie ... \n\n"
	print "With a small text file ... \n\n"
	avgTrie = analyseGenerationOfTrie(smallTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgTrie
	avgTrie = analyseCountFunctionOfTrie(smallTextfile)
	print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgTrie
	print "With a large text file ... \n\n"
	avgTrie = analyseGenerationOfTrie(largeTextfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgTrie
	avgTrie = analyseCountFunctionOfTrie(largeTextfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgTrie

	print "\n\n"

	# print "Analysing binary search tree ... \n\n"
	# print "With a small text file ... \n\n"
	# avgBinarySearchTree = analyseGenerationOfHashTable(smallTextfile)
	# print "--- Generation of sorted list of tuples - %s seconds ---" % avgBinarySearchTree
	# avgBinarySearchTree = analyseCountFunctionOfHashTable(smallTextfile)
	# print "--- Count function of sorted list of tuples - %s seconds --- \n" % avgBinarySearchTree
	# print "With a large text file ... \n\n"
	# avgBinarySearchTree = analyseGenerationOfHashTable(smallTextfile)
	# print "--- Generation of sorted list of tuples - %s seconds ---" % avgBinarySearchTree
	# avgBinarySearchTree = analyseCountFunctionOfHashTable(smallTextfile)
	# print "--- Count function of sorted list of tuples - %s seconds ---" % avgBinarySearchTree

	# print "\n\n"

	