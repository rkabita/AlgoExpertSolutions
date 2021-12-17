
# Time Complexity: O(m log(m) + n log(n)) time || m & n are the array length
# Space Complexity: O(1) 



def smallestDifference(arrayOne, arrayTwo):
  arrayOne.sort()
	arrayTwo.sort()
	
	pointer1 = 0
	pointer2 = 0
	
	smallest = float("inf")
	current = float("inf")
    
	while pointer1 <len(arrayOne) and pointer2 < len(arrayTwo):
		firstNum = arrayOne[pointer1]
		secondNum = arrayTwo[pointer2]
		
		if firstNum < secondNum: 
			current = secondNum- firstNum
            pointer1 += 1
			
		elif secondNum < firstNum:
			current = firstNum - secondNum
			pointer2 += 1
		else: 
			return [firstNum, secondNum]
		
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
			
	return smallestPair
