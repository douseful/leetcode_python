"""
Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3.

    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def length_of_longest_substring(self, s):
        """
        双指针问题，使用一个字典来存储每个字母对应的坐标，如果发现当前遍历到的字母之前出现过，则触发更新左指针操作
        :param s: 输入的要判定的字符串
        :return: 最长子串的长度
        """
        left, result = 0, 0
        index_map = {}
        for right in range(len(s)):
            if s[right] in index_map:
                left = max(index_map[s[right]] + 1, left)
            result = max(result, right - left + 1)
            index_map[s[right]] = right
        return result


print(Solution().length_of_longest_substring('pwwkew'))
