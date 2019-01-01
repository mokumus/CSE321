def plan(city1, name1, city2, name2, travelCost, numOfMonths) :
	cost1 = city1[0]
	cost2 = city2[0]
	plan = []

	temp1 = city1[1] + min(cost1, travelCost + cost2)
	temp2 = city2[1] + min(cost2, travelCost + cost1)
	if min(temp1, temp2) == temp1 :
		plan.append(name1)
	else :
		plan.append(name2)


	for i in range (1, numOfMonths) :
		cost1 = city1[i] + min(cost1, travelCost + cost2)
		cost2 = city2[i] + min(cost2, travelCost + cost1)
		if min(cost1, cost2) == cost1 :
			plan.append(name1)
		else :
			plan.append(name2)

	return min(cost1,cost2), plan,
 
#Driver code for Q2, b
def main() :
	ny = [1,3,20,30]
	sf = [50,20,2,4]
	m = 10
	print plan(sf,'SF',ny, 'NY', m, 4)

	la = [1,2,1,2]
	tx = [2,1,2,1]
	m = 5
	print plan(la,'LA',tx, 'TX', m, 4)
main()