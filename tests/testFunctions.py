from Calculator import engine
from Calculator import MathOperations

class testCases():

    def __init__(self):
        self._testObj = engine.engine()
        self.testAppend()
        self.peek()
        self.pop()
    def testAppend(self):
        correctList = [0,1,2,3,4,5,6,7,8,9]
        for x in range(10):
            self._testObj.push(x)
        assert self._testObj.getWholeStructure() == correctList, "Error appending to structure"

    def peek(self):
        assert self._testObj.peek() == 9, f"Error in peek: {self._testObj.getWholeStructure()[len(self._testObj.getWholeStructure())-1]} does not equal 9"
        assert self._testObj.peek() == 9, f"Removal happened in peek: {self._testObj.getWholeStructure()[len(self._testObj.getWholeStructure()) - 1]} does not equal 9"

    def pop(self):
        beforePop = len(self._testObj.getWholeStructure())
        self._testObj.pop()
        afterPop = len(self._testObj.getWholeStructure())
        assert afterPop == beforePop-1, f"\nError in func pop call: \nLengths should be the same. {beforePop-1} != {afterPop}"

    def testAdd(self):
        self._testObj.push(1)
        self._testObj.push(2)
        # operator assumed "+"

        #assert MathOperations.operations.add(self._testObj) == 3, "Add test case failed"


    def testSubtraction(self):
        pass


testCases()
