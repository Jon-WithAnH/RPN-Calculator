### main structure of the calculator ###
# push peek and pop


class engine():

    def __init__(self):
        self._stack = []

    def pop(self):
        # return item at end of list, remove after
        return self._stack.pop()

    def push(self, number):
        self._stack.append(number)

    def peek(self):
        # return top value but do not remove it
        return self._stack[len(self._stack)-1]

    ## testing values ##

    def getWholeStructure(self):
        return self._stack

