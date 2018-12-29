def degreeOf(V, E) :
	numOfEdges = 0
	for pair in E :
		if pair[0] == V or pair[1] == V :
			numOfEdges += 1
	return numOfEdges

# Debug utility to print number of edges for a vertex
# given the Vertices and Edges lists
def degreeAll(Vertices,Edges) :
	for v in Vertices :
		print(v + ": " + str(degreeOf(v, Edges)))

def deleteEdgesOf(V, E) :
	for index, pair in enumerate(E) :
		if pair[0] == V or pair[1] == V :
			del E[index]

def getMaxEdges(V,E) :
	currentMax = 0
	for v in V : 
		temp = degreeOf(v, E)
		if temp > currentMax :
			currentMax = temp
 	return currentMax

def getMinEdges(V,E) :
	currentMin = 99999
	for v in V : 
		temp = degreeOf(v, E)
		if temp < currentMin :
			currentMin = temp
 	return currentMin

def inviteList(Vertices, Edges) :
	while getMinEdges(Vertices,Edges) < 5 or getMaxEdges(Vertices,Edges) > (len(Vertices) - 5) :
		for index, v in enumerate(Vertices) :
			#vertex has degree less than five or greater than n - 5
			#In other words knows less then 5 people
			#Or knows too many people so there can't be 
			#less then 5 people that she/he doesn't know at the party
			if degreeOf(v, Edges) < 5 or degreeOf(v, Edges) > len(Vertices) - 5 : 
				del Vertices[index]
				deleteEdgesOf(v, Edges)
	return Vertices

#Driver code for Q4
def main() :

	people = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	pairs = [
			['a', 'b'], #------------------
		   	['a', 'c'],
		   	['a', 'd'], # Friend group of
		   	['a', 'e'], # 6 people
		   	['a', 'f'], # a-b-c-d-e-f
		 	['b', 'c'], # So they all know
		 	['b', 'd'], # 5 other people
		 	['b', 'e'], # i.e: 
		 	['b', 'f'], # f knows a,b,c,d,e
		 	['c', 'd'], 
		 	['c', 'e'],
		 	['c', 'f'],
		 	['d', 'e'], 
		 	['d', 'f'],
		 	['e', 'f'], #------------------
		 	['g', 'h'], #------------------
		 	['g', 'i'],
		 	['g', 'j'],
		 	['g', 'k'],
		 	['g', 'l'], 
		 	['h', 'i'],
		 	['h', 'j'],
		 	['h', 'k'], # g-h-i-j-k-l
		 	['h', 'l'],
		 	['i', 'j'],
		 	['i', 'k'],
			['i', 'l'],
		 	['j', 'k'],
		 	['j', 'l'],
		 	['k', 'l'], #------------------
		 	['m', 'n'],
		 	['m', 'a'],
		 	['m', 'a'],
		 	['n', 'o'],
		 	['p', 'q'],
		 	['r', 's'], # people with 3 or less friends
		 	['t', 'u'],
		 	['v', 'w'],
		 	['x', 'y'],
		 	['x', 'z'],
		 	['y', 'z'],
		 	['z', 'n'],
		 	['z', 'o'],
		 	['z', 'p'], # z knows 5 people
		  ]
	print("Who knows how many: ")	  
	degreeAll(people, pairs)
	print("Party goers: ")
	print inviteList(people, pairs)
	print("Guests knows how many: ")
	degreeAll(people, pairs)

main()


