import unittest
from inventory import inventory

class TestInventory(unittest.TestCase):
    def testNum1(self):
        i1 = inventory(1,2,3)
        self.assertEqual(i1.num1,1)
    def testNum2(self):
        i1 = inventory(1,2,3)
        self.assertEqual(i1.num2,2)
    def testNum3(self):
        i1 = inventory(1,2,3)
        self.assertEqual(i1.num3,3)
        
if __name__ == '__main__':
    unittest.main()