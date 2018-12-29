#------QUESTION 1-------
#Utility function to print path in reference to the hotel indices
def printPath(path, i) :
	if i == 0 :
		return
	printPath(path, path[i])
	print(str(i) + " ")


def optimalPath(hotelList) :
	penalties = [0] * len(hotelList)
	path = [0] * len(hotelList)

	#Iterate through the distances(hotelList) and find the minimum penalty
	for i in range (1, len(hotelList)) :
		for j in range(0, i) :
			tempPen = (penalties[j] + (200 - (hotelList[i] - (hotelList[j])))**2)
			if penalties[i] == 0 or tempPen < penalties[i] : #Find min here
				penalties[i] = tempPen
				path[i] = j
	
	#Printing results
	for i in range (1, len(hotelList)) :
		print("Hotel: " + str(hotelList[i]) + ", penalty: " + str(penalties[i]) + ", path: ")
		printPath(path, i)		

	print("Penalties: " + str(penalties))

#Driver code for Q1
def main () :
	hotelList = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]
	optimalPath(hotelList)

main()