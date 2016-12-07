import time
start_time = time.time()

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedListBinarySearchable(object):

	def __init__(self, iterable=None):
		self.head = None
		self.tail = None
		self.list = []
		# if conditions: 
		# 	self.conditions = conditions
		# else: 
		# 	self.conditions = lambda(item: item > node.data)
		if iterable:
			for item in iterable:
				self.append(item)
        return time.time() - start_time
	# create a list that represents the linked list,
	# each index contains a pointer to the node 
	#  updated on append and delete


	def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedListBinarySearchable({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

	def append(self, item):
		"""Insert the given item into a sorted linked list"""
        node = Node(item)

    	# before
        p1 = self.head
        # current
        p2 = self.head.next
        #  not sure if I need this third pointer
        # next
        p3 = self.head.next.next

        # linked list is empty
        if self.tail is None:
        	self.head = node
        	self.tail = node
        	self.list.append(item)
        	return
        # item is greater than or equal to the head (will become head)
        elif item >= p1:
        	self.head = node 
        	self.head.next = p1
        	self.list.insert(0, item)
        	return
        # item is less than or equal the tail (will become the tail)
        elif item <= self.tail:
        	self.tail.next = node
        	self.tail = node
        	self.list.insert(-1, item)
        	return
        # item is equal to a node.data that already exists in the linked list
        elif self.contains(item):
        	current = self.head
        	while current is not None:
        		#  if p1 > item && p2 <= item:
        		if p1 > item && p2 == item:
        			# insert before p2
        			p1.next = node
        			node.next = p2
        			indexOfItem = self.list.index(item)
        			self.list.insert(indexOfItem, item)
        			return
        		else: 
        			current = current.next
        			p1 = p1.next
        			p2 = p2.next
        			p3 = p3.next
        #  item is not already in the linked list
	    else:
        	current = self.head
        	while current is not None:
        		if p1 > item && p2 < item:
        			# insert before p2
        			p1.next = node
        			node.next = p2
        			indexOfItem = self.list.index(p2)
        			self.list.insert(indexOfItem, item)
        			return
        		else: 
        			current = current.next
        			p1 = p1.next
        			p2 = p2.next
        			p3 = p3.next

        



        




    	# linked list is empty
        if self.tail is None:
        	self.head = node
        	self.tail = node
        	self.list.append(item)
        	return
        #  linked list has one item
        elif self.head.next is None:
        	# if self.head.data > item:
        	currentOrderOfItems = [p1, p2, p3]
        	sortedOrderOfItems = sorted(currentOrderOfItems)
        	
        	if currentOrderOfItems != sortedOrderOfItems:



        	pass
        # linked list has one item
        elif self.head.next.next is None:
        	pass
        else: 
        	# item is greater than head (will become head)
        	# item is equal to head
        	# item is less than tail (will become tail)
        	# item is equal to tail
        	# item is equal to a node.data that is not the head or tail

        	# item is not equal to any other node, and fits between two nodes
        	


        if self.tail is not None:
            currentTailNode = self.tail
            currentTailNode.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
	# sort on append
	# need 2 or 3 pointers to keep track of current, previous and next 
	# if alphabetical, sort by that
	# if numerical, sort by that 
		pass

	# binary search the list, and then the pointer 
	# will indicate the linked list node
	def search(self, item):
		pass
		middleIndex = len(self.list) // 2
		middleNode = self.list[middleIndex]




	def contains(self, item):
		current = self.head
		while current is not None:
			if current.data == item:
				# return True
                return time.time() - start_time
			current = current.next
		# return False
        return time.time() - start_time

	# is it possible to provide the conditions for sorting?
	# if I use lambda, probably 
