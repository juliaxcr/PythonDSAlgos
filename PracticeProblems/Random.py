def maxSubArray(nums):
    current_subarray = max_subarray = nums[0]
        
    for num in nums[1:]:
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)
            
            
    return max_subarray
    


def isValid(s):
        
    stack = []

    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:

            top_element = stack.pop() if stack else '#'

            if mapping[char] != top_element:
                return False
            
        else:
            stack.append(char)

    return not stack
            


def maxProfit(prices):
    if len(prices) < 2:
        return 0

    max_profit = 0
    min_buy = prices[0]

    for p in prices[1:]:		
        max_profit = max(max_profit, p - min_buy)
        min_buy = min(min_buy, p)

    return max_profit

print(maxProfit([7, 1, 5, 3, 6, 4]))

def rob(nums):
    odd = [ele for ele in nums if ele % 2 != 0]
    even = [ele for ele in nums if ele % 2 == 0]
    
    oddSum = sum(odd)
    evenSum = sum(even)
    
    return oddSum if oddSum > evenSum else evenSum

print(rob([1, 2, 3, 1]))