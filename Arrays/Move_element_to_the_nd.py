# Time Complexity: O(n) | n = length of the array
# Space Complexity: O(1)




def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 0
	j = len(array) - 1
    
	while i < j:
		while i < j and array[j] == toMove:
			j -= 1
		if array[i] == toMove:
			array[i], array[j] = array[j], array[i]
			
		i += 1
	return array
