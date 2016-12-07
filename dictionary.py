import sys
import time
start_time = time.time()


class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)
        

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for word in iterable:
            if word in self:
                self[word] = self[word] + 1
                self.tokens += 1
            else:
                self[word] = 1
                self.types += 1
                self.tokens += 1
        

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        if item in self: 
            # return self[item]
            return time.time() - start_time
        else: 
            # return 0
            return time.time() - start_time


if __name__ == "__main__":
	generateHistogramFromFile(sys.argv[1])

