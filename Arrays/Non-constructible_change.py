
# Time Complexity: O(n log n) time || n is the number of coins 
# Space Complexity: O(1)


def nonConstructibleChange(coins):
    # Write your code here.
	
	coins.sort()
	
	currentCreatedChange = 0
	for coin in coins: 
		if coin > currentCreatedChange +1:
			return currentCreatedChange +1
		
		currentCreatedChange += coin
	
	
    return currentCreatedChange +1
