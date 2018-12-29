#------QUESTION 3-------
# Merge all lists into the first list in the given list
# Pre: A list of lists and a lists are sorted
# Post: First element is the given list is changed, rest untouched
# Return: A sorted list, leveled and rearraged version of the provided input
def mergeAll(listOfLists) :
	if len(listOfLists) == 0 :
		return []

	if len(listOfLists) == 1 :
		return listOfLists[0]

	for i in range(1, len(listOfLists)/2 +1) :
		listOfLists[0] = mergeArrays(listOfLists[0], listOfLists[i])
		if len(listOfLists)-i != i: #Middle duplicate check
			listOfLists[0] = mergeArrays(listOfLists[0], listOfLists[len(listOfLists)-i])

	return listOfLists[0]

# Merge arrays into new array and return it
# Pre: Two sorted arrays
# Post: No side effects
# Return: New array[size(arr1) + size(arr2)]
def mergeArrays(arr1, arr2) :
	n1 = len(arr1)
	n2 = len(arr2) 
	arr3 = [None] * (n1 + n2) 
	i, j, k = 0, 0, 0

	# Traverse both arrays
	while i < n1 and j < n2 : 
		if arr1[i] < arr2[j] : 
			arr3[k] = arr1[i] 
			k += 1
			i += 1
		else : 
			arr3[k] = arr2[j] 
			k += 1
			j += 1
	

	#Add rest of the first array if any left
	while i < n1 : 
		arr3[k] = arr1[i] 
		k += 1
		i += 1

	#Add rest of the second array if any left
	while j < n2 : 
		arr3[k] = arr2[j] 
		k += 1
		j += 1
	return arr3
	

#Driver code for Q3
def main() :
	arr1 = [1, 3, 5, 7] 
	arr2 = [-1, 1, 2, 30] 
	arr3 = [10, 20, 24, 25] 
	arr4 = [-100,-50,-25,100] 
	arr = [arr1,arr2,arr3,arr4]

	arr1 = mergeAll(arr); 
	print arr1 #[-100, -50, -25, -1, 1, 1, 2, 3, 5, 7, 10, 20, 24, 25, 30, 100]

main()