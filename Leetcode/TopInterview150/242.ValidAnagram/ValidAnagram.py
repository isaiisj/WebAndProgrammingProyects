'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #first lower the strings in case thery not
        s = s.lower()
        t = t.lower()

        #build the hash maps
        dict1 = {}
        dict2 = {}

        #fill the dict1 with s
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        #fill the dict2 with t
        for j in t:
            if j in dict2:
                dict2[j] += 1
            else:
                dict2[j] = 1

        #First we check if we have the same amount of
        #letters in each word
        if len(dict1) != len(dict2):
            return False
        else:
            #if we have the same letters
            #in dict1 and dict 2 they're anagrams
            for i in dict1:
                if i in dict2 and dict1[i] == dict2[i]:
                    pass
                else:
                    return False
        
        return True
