'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #Create two pointers
        p1 = 0  #index at 0
        p2 = len(numbers) -1  #index at the end


        #While p1 < p2
        while p1 < p2:
            #if the sum equals the target
            if numbers[p1] + numbers[p2] == target:
                return [p1+1,p2+1]  #return the indexes plus one

            #if the sum is grater than the target
            elif numbers[p1] + numbers[p2] > target:
                #search the index of the grater and move it
                if p1 > p2:
                    p1 += 1
                else:
                    p2 -= 1

            #if the sum is less than the target
            elif numbers[p1] + numbers[p2] < target:
                #search the index of the minor and move it
                if p1 < p2:
                    p1 += 1
                else:
                    p2 -= 1

'''
Time complexity: O(n)
'''
                

