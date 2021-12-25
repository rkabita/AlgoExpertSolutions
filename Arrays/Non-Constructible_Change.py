def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
	totalChange = 0 
	for coin in coins:
		if coin>totalChange+1:
			return totalChange+1
		totalChange = totalChange+ coin
			
	return totalChange+1
 
  
  
  
  ##### Time Complexity: O(n log n)
  ##### Space Complexity: 0(1)
  
