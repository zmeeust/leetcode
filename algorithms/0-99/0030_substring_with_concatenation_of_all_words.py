"""
You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once,
in any order, and without any intervening characters.
You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Constraints:
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or s is None or words is None:
            return []

        count = {}
        word_length = len(words[0])
        res = []
        words_length = word_length * len(words)

        for word in words:
            count[word] = count.get(word, 0) + 1

        for left in range(len(s) - words_length + 1):
            words_seen = {}
            for right in range(len(words)):
                word_index = left + right * word_length
                temp_word = s[word_index:word_index + word_length]
                if temp_word not in count:
                    break
                words_seen[temp_word] = words_seen.get(temp_word, 0) + 1
                if words_seen[temp_word] > count[temp_word]:
                    break
            if words_seen == count:
                res.append(left)

        return res


if __name__ == '__main__':
    solution = Solution()

    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    assert solution.findSubstring(s, words) == [0, 9]

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    assert solution.findSubstring(s, words) == []

    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    assert solution.findSubstring(s, words) == [6, 9, 12]
