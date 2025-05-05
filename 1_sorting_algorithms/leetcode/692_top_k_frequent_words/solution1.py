from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count words into hashmap O(n)
        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        # Gather unique O(n)
        words = list(freq.keys())

        # Sort O(nlogn)
        words.sort(key=lambda x: (-freq[x], x))
        return words[:k]
