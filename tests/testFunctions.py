from Calculator import engine
from Calculator import MathOperations

class testCases():

    def __init__(self):
        self._testObj = engine.engine()
        self.append()
        self.peek()
        self.pop()
        self.add()
        self.subtraction()

    def append(self):
        correctList = [0,1,2,3,4,5,6,7,8,9]
        for x in range(10):
            self._testObj.push(x)
        assert self._testObj.getWholeStructure() == correctList, "Error appending to structure"

    def peek(self):
        assert self._testObj.peek() == 9, f"Error in peek: " \
                                          f"{self._testObj.getWholeStructure()[len(self._testObj.getWholeStructure())-1]} does not equal 9"
        assert self._testObj.peek() == 9, f"Removal happened in peek: " \
                                          f"{self._testObj.getWholeStructure()[len(self._testObj.getWholeStructure()) - 1]} does not equal 9"

    def pop(self):
        beforePop = len(self._testObj.getWholeStructure())
        self._testObj.pop()
        afterPop = len(self._testObj.getWholeStructure())
        assert afterPop == beforePop-1, f"\nError in func pop call: \n" \
                                        f"Lengths should be the same. {beforePop-1} != {afterPop}"

    def add(self):
        # operator assumed "+"
        self._testObj.push(1)
        self._testObj.push(2)
        result = MathOperations.add(self._testObj) # 1+2
        assert result == 3, f"Add test case failed\n" \
                            f"{result} != 3"

    def subtraction(self):
        self._testObj.push(1)
        self._testObj.push(2)
        result = MathOperations.subtraction(self._testObj) # 2-1
        assert result == 1, f"Add test case failed\n" \
                            f"{result} != 1"



testCases()
