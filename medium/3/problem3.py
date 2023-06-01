"""
    Problem 3. Longest Substring Without Repeating Characters
    Given a string s, find the length of the longest substringwithout repeating characters. 

    Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

    Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

    Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    
    Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def __init__(self):
        self.startIndex = 0
        self.endIndex = 0

        self.alreadySeenCharacters = set()

    def reset(self):
        self.startIndex = 0
        self.endIndex = 0

        self.alreadySeenCharacters = set()

    def findNextStartIndex(self, charToSearch: str, s: str, startIndex: int) -> int:
        searchString = s[startIndex:]
        for nextChar in searchString:
            startIndex += 1
            self.alreadySeenCharacters.remove(nextChar)

            if nextChar == charToSearch:
                break

        return startIndex

    def lengthOfLongestSubstring(self, s: str) -> int:
        self.reset()
        startIndex = 0
        endIndex = 0

        for nextChar in s:
            if nextChar in self.alreadySeenCharacters:
                startIndex = self.findNextStartIndex(nextChar, s, startIndex)

            endIndex += 1
            self.alreadySeenCharacters.add(nextChar)

            if (endIndex - startIndex) > (self.endIndex - self.startIndex):
                self.startIndex = startIndex
                self.endIndex = endIndex

        return self.endIndex - self.startIndex


if __name__ == "__main__":
    solution = Solution()

    s = "abcabcbb"
    print(solution.lengthOfLongestSubstring(s))

    s = "Sheelan Misra"
    print(solution.lengthOfLongestSubstring(s))

    s = "bbbbb"
    print(solution.lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))
