from typing import List

# strs = ["a"]
strs = ["cir", "car"]

def find_prefix(word_list: List, strs: List):
    if len(strs) == 1:
        return strs[0]

    common_prefix = ""
    for i in range(min(len(word_list), len(strs[1]))):
        if word_list[i] == strs[1][i]:
            common_prefix += word_list[i]
        else:
            break

    return common_prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        word_list = list(strs[0])
        common_prefix = find_prefix(word_list, strs)

        return common_prefix

# Example usage:
sol = Solution()
ans = sol.longestCommonPrefix(strs)
print('ans', ans)
