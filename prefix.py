from typing import List

# strs = ["a"]
strs = ["reflower","flow","flight"]

def find_prefix(word_list: List, strs: List):
    
    if len(strs) == 1:
        return strs[0]


    prefix = []
    for i in strs[1:]:
        temp_prefix = [*i]
        prefix = list(set(word_list) & set(temp_prefix))

    return sorted(prefix)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word_list = [*strs[0]][:len(strs[0]) // 2]
        print(word_list)
        prefix = find_prefix(word_list, strs)

        # Initialize an empty string
        ans = ""

        # Traverse in the string
        for ele in prefix:
            ans += ele

        if prefix == []:
            return ""

        return ans

# Example usage:
sol = Solution()
ans = sol.longestCommonPrefix(strs)
print('ans', ans)
