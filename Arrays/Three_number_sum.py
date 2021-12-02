''' 
Brute Force Approach: We can use three for loops and scan through the whole array three times to find and check all possible combinations of numbers which
gives us the targetSum.
Time complexity: Time Complexity of this solution is O(n^3)
Space Complexity: O(n) | which we used to create the new array of triplets. 

'''

'''
Optimal Solution: 
Here we used two pointer technique. First we sort the array in ascending order. Then, we pick a number using for loops and two pointer. The first pointer will
point to the next number of the number and the second pointer will point to the last number of the array. We can find three scenarios:
  
  i) If we find that the total sum of the three number is equal to the targetSum, we will add all three numbers in the triplet. we will increment left and decrement right pointer.
  ii) If we find the total sum is less than targetSum we will increase the left pointer. because thats the only way we can get closer to the targetSum.
  iii) If we find the total sum is greater than targetSum we will decrease the right pointer. because thats the only way we can get closer to the targetSum.

Time complexity: Time Complexity of this solution is O(n logn + n^2) = O(n^2)
Space Complexity: O(n) | which we used to create the new array of triplets. 



'''
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplet = []
	arrayLength = len(array)
	for i in range(arrayLength-2):
		left = i + 1
		right = arrayLength - 1
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				triplet.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			elif currentSum > targetSum:
				right -= 1
	return triplet




  
