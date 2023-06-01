import unittest
from problem3 import Solution

class TestSolution3(unittest.TestCase):
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring('Sheelan Misra'), 9)

    def test1(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring('abcabcbb'), 3)

    def test1(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring('bbbbb'), 1)

    def test1(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring('pwwkew'), 3)

if __name__ == '__main__':
    unittest.main()
