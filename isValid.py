def pattern(bracketed_pattern):
    new_list = []
    skip_next = False

    for i, element in enumerate(bracketed_pattern):
        if skip_next:
            skip_next = False
            continue
        
        if element == 'open' and i < len(bracketed_pattern) - 1 and bracketed_pattern[i + 1] == 'close':
            skip_next = True
        else:
            new_list.append(element)

    return new_list

class Solution:
    def isValid(self, s: str) -> bool:
        print('s:',s)
        bracketed_pattern = []
        # Test for only even numbers,Odds are out . 
        if len(s) % 2 != 0 :
            print('it has odds numbers of bracketed')
            return False
        for i in s:
            if i == '(':
                bracketed_pattern.append('open')
            elif i == ')':
                bracketed_pattern.append('close')

        # Count the amount that ther is 'open ' and 'close' in the list .
        amount_open = bracketed_pattern.count('open')
        amount_close = bracketed_pattern.count('close')

        for _ in range(amount_open):
            bracketed_pattern = pattern(bracketed_pattern)
        print("Final Output:", bracketed_pattern)


        if amount_open != amount_close:
            return False  
        if len(bracketed_pattern) > 0 :
            if amount_close == amount_open and bracketed_pattern[0] == 'close' :
                print('bracketed_pattern[0]',bracketed_pattern[0])
                print('There is closing before a starting')
                return False
                
                
        return True

s = "())(" 
sel = Solution()
answer = sel.isValid(s)
print('answer is :',answer)


# sequences = [
#     "(()",
#     "((()",
#     "())(", # false 
#     "))((",
#     "()((",
#     ")()(",
#     "(()(",
#     "())(",
#     ")))(",
#     "()()",
#     "))()",
#     ")(())",
#     ")()(",
#     "(())",
#     "((()",
#     "()(",
#     "())",
#     "(((",
#     "))",
#     "())",
#     "))",
#     "((()))()",
#     ")(",
# ]

# for s in sequences:
#     print('s',s)
#     sel = Solution()
#     answer = sel.isValid(s)
#     print('answer is :',answer)
    

