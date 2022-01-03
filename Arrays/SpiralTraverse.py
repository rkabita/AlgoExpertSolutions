##### Approach: We can think this problem that we have to print the perimeter of a rectangle, and The rectangle progressively gets smaller.




def spiralTraverse(array):
    # Write your code here.
    result = []
	startRow, endRow = 0 , len(array)-1
	startCol, endCol = 0, len(array[0]) - 1
	
	while startRow<= endRow and startCol<= endCol:
		for col in range(startCol, endCol + 1):
			result.append(array[startRow][col])
		
		for row in range(startRow+1, endRow+1):
			result.append(array[row][endCol])
			
		for col in reversed(range(startCol, endCol)):
			if startRow == endRow:
				break
			result.append(array[endRow][col])
			
		for row in reversed(range(startRow+ 1, endRow)):
			if startCol == endCol:
				break
			result.append(array[row][startCol])
			
		startCol += 1
		endCol -= 1
		startRow += 1
		endRow -= 1
    return result
  
  
  ######## Time Complexity: O(n) 
  ######## Space Complexity: O(n)
