class MyQueue(object):

    def __init__(self, data=None):
        """Initiate a queue

        Initiate an empty queue
        >>> MyQueue().size()
        0

        The same for empty list
        >>> MyQueue([]).size()
        0

        Assert on incorrect input
        >>> MyQueue(23)
        Traceback (most recent call last):
        ...
        AssertionError

        Initiate queue from tuple
        >>> MyQueue((10, 12, 13)).size()
        3

        Check get first element
        >>> MyQueue([1, 2, 3]).pop()
        1

        Add new element
        >>> s = MyQueue([1, 2, 3])
        >>> s.push(4)
        >>> s.size()
        4
        >>> s.pop()
        1
        >>> s.size()
        3
        """

        assert \
            data is None or \
            type(data) == list or \
            type(data) == tuple

        if data is None:
            self.data = []
        else:
            self.data = list(data)

    def push(self, data_to_add):
        self.data.append(data_to_add)

    def pop(self):
        return self.data.pop(0)

    def size(self):
        return len(self.data)

if __name__ == "__main__":
    import doctest
    doctest.testmod()