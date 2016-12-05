class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            if item in self:
                index = self._index(item)
                count = self[index][1]
                self[index] = (item, count + 1)
                self.tokens += 1
            else: 
                self.append((item, 1))
                self.types += 1
                self.tokens += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        index = self._index(item)
        if index != None:
            return self[index][1]
        return 0


    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""
        for element in self:
            if element[0] == item:
                return True
        else: 
            return False

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        for i in range(len(self)):
            if self[i][0] == target:
                return i 
        return None