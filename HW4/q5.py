#------QUESTION 5-------
def validatePair(i1,i2, v, constraints):
	status = True
	for c in constraints :
		if (v[i1] == v[c[0]] and v[i2] == v[c[1]]) or (v[i1] == v[c[1]] and v[i2] == v[c[0]]) :
			if c[2] == "==" :
				status = v[i1] == v[i2]
			elif c[2] == "!=":
				status = v[i1] != v[i2]
			else :
				return False

	return status

def isSatisfied(constraints, variables) :
	for c in constraints :
		if validatePair(c[0],c[1], variables, constraints) == False :
			return False
	return True


#Driver code for Q5
def main() :
	variables = [1,1,5,5,4]
	constraints = [ [0,1, "=="], # [i1,i2,constraint]
			  		[1,2, "!="],
			  		[2,3, "=="],
			  		[2,4, "!="]
			]
	print variables
	print constraints
	print isSatisfied(constraints, variables)
	variables = [1,1,4,5,4]
	constraints = [ [0,1, "=="], # [i1,i2,constraint]
			  		[1,2, "!="],
			  		[2,3, "=="],
			  		[2,4, "!="]
			]
	print variables
	print constraints
	print isSatisfied(constraints, variables)
	variables = [1,1,4,5,4]
	constraints = [ [0,1, "=="], # [i1,i2,constraint]
			  		[1,2, "!="],
			  		[2,3, "!="],
			  		[2,4, "=="]
			]
	print variables
	print constraints
	print isSatisfied(constraints, variables)

main()