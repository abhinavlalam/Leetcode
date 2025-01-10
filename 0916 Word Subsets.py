from collections import Counter
from typing import List
import time

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char in word_count:
                max_freq[char] = max(max_freq[char], word_count[char])
    
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= max_freq[char] for char in max_freq):
                result.append(word)

        return result
    
# Test inputs
test_cases = [
    (["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]),
    (["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"])
]

# Instantiate the solution class
solution = Solution()

# Measure performance and execute test cases
for i, (words1, words2) in enumerate(test_cases, 1):
    start_time = time.time()
    output = solution.wordSubsets(words1, words2)
    elapsed_time = time.time() - start_time
    print(f"Test Case {i}:")
    print(f"Input words1: {words1}")
    print(f"Input words2: {words2}")
    print(f"Output: {output}")
    print(f"Execution Time: {elapsed_time:.6f} seconds\n")


# Additional things to learn
# 1. How to implement a word counted