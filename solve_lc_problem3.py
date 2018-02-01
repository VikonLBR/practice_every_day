'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        max_string = ""
        answer = ""
        original_length = len(s)
        for i in range(original_length):
            for j in range(len(s[i:])):
                if s[i + j] not in max_string:
                    max_string += s[i + j]

                else:
                    break
            if len(max_string) > max_length:
                answer = max_string
                max_length = len(answer)
                max_string = ""
            else:
                max_string = ""
        return len(answer)









