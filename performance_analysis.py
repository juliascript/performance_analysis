import dictionary, list_of_tuples, sorted_list_of_tuples
import hashtable, singly_linked_list, sorted_singly_linked_list
import doubly_linked_list, trie, binary_search_tree
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
	# todo: update all files to return ints instead of the actual values for averaging
	# todo: implement and test sorted linked list
	# todo: implement and test binary search tree
	# todo: update function calls to correct functions in this file
	# todo: implement binary search on all sorted data structures 

	smallTextfile = "..."
	largeTextfile = "..."

	print "Analysing dictionary ... \n\n"
	avgDict = analyseGenerationOfDictionary(textfile)
	print "--- Generation of dictionary - %s seconds ---" % avgDict
	avgDict = analyseCountFunctionOfDictionary(textfile)
	print "--- Count function of dictionary - %s seconds ---" % avgDict

	print "\n\n"

	print "Analysing list of tuples ... \n\n"
	avgSortedTuples = analyseGenerationOfListOfTuples(textfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedTuples
	avgSortedTuples = analyseCountFunctionOfListOfTuples(textfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgSortedTuples

	print "\n\n"

	print "Analysing sorted list of tuples ... \n\n"
	avgSortedTuples = analyseGenerationOfSortedListOfTuples(textfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgSortedTuples
	avgSortedTuples = analyseCountFunctionOfSortedListOfTuples(textfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgSortedTuples

	print "\n\n"

	print "Analysing hash table ... \n\n"
	avgHashtable = analyseGenerationOfHashTable(textfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgHashtable
	avgHashtable = analyseCountFunctionOfHashTable(textfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgHashtable

	print "\n\n"

	print "Analysing singly linked list ... \n\n"
	avgHashtable = analyseGenerationOfSinglyLinkedList(textfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgHashtable
	avgHashtable = analyseCountFunctionOfSinglyLinkedList(textfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgHashtable

	print "\n\n"

	# print "Analysing sorted singly linked list ... \n\n"
	# avgHashtable = analyseGenerationOfSortedSinglyLinkedList(textfile)
	# print "--- Generation of sorted list of tuples - %s seconds ---" % avgHashtable
	# avgHashtable = analyseCountFunctionOfSortedSinglyLinkedList(textfile)
	# print "--- Count function of sorted list of tuples - %s seconds ---" % avgHashtable

	# print "\n\n"

	print "Analysing doubly linked list ... \n\n"
	avgHashtable = analyseGenerationOfDoublyLinkedList(textfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgHashtable
	avgHashtable = analyseCountFunctionOfDoublyLinkedList(textfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgHashtable

	print "\n\n"

	print "Analysing trie ... \n\n"
	avgHashtable = analyseGenerationOfTrie(textfile)
	print "--- Generation of sorted list of tuples - %s seconds ---" % avgHashtable
	avgHashtable = analyseCountFunctionOfTrie(textfile)
	print "--- Count function of sorted list of tuples - %s seconds ---" % avgHashtable

	print "\n\n"

	# print "Analysing binary search tree ... \n\n"
	# avgHashtable = analyseGenerationOfHashTable(textfile)
	# print "--- Generation of sorted list of tuples - %s seconds ---" % avgHashtable
	# avgHashtable = analyseCountFunctionOfHashTable(textfile)
	# print "--- Count function of sorted list of tuples - %s seconds ---" % avgHashtable

	# print "\n\n"

	