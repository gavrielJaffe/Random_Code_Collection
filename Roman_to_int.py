class Solution:
    def romanToInt(self, s: str) -> int:
        counter = 0 
        romen_number = s    
        for i in romen_number:
            print('i', i)
            if i == 'I':
                counter += 1 
            elif i -1 == 'I':
                pass
            elif i == 'V':
                counter += 5
            elif i == 'X' : 
                counter += 10 
            elif i == 'L':
                counter += 50 
            elif i == 'C' :
                counter += 100 
            elif i == 'D' :
                counter += 500 
            elif i == 'M' :
                counter += 1000
        return counter 
                




        return print('x', 10 )
    

our_solution = Solution()


n = our_solution.romanToInt("XI")
print('n', n)



# IV , for i in range of (romen) if the i is from the left side subtract , else add them up toughter . 



# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# https://leetcode.com/problems/roman-to-integer/?envType=featured-list&envId=top-interview-questions