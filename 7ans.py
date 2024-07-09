def maxScore(cardPoints, k):
    n = len(cardPoints)
    
    if k == n:
        return sum(cardPoints)
    curr_sum = sum(cardPoints[:k])
    max_sum = curr_sum
    
    for i in range(k):
        curr_sum = curr_sum - cardPoints[k-i-1] + cardPoints[n-i-1]
        max_sum = max(max_sum, curr_sum)
        
    return max_sum
input_string = input("Input: cardPoints = ")
cardPoints = [int(x) for x in input_string.split(',')]
k = int(input("ENter number of cards: "))
res = maxScore(cardPoints,k)
print(f"Output: {res}")
