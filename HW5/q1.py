from __future__ import division #For flaot division in python2


def bubbleSort(arr) : 
    n = len(arr) 

    for i in range(n) : 
        swapped = False

        for j in range(0, n-i-1) : 

            if tdw(arr[j]) > tdw(arr[j+1]) : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        if swapped == False: 
            break

def tdw(job) :
	return job[0] / job[1]

def txw(job) :
	return job[0] * job[1]

def totalWeight(jobs) :
	t = 0
	txw = 0
	bubbleSort(jobs)
	print("Job order: " + str(jobs))
	for job in jobs :
		txw += (t+job[0]) * job[1]
		t += job[0]
	return txw


#Driver code for Q1
def main() :
	# [time, weight]
	jobs = [ 
			[1, 10],
			[3, 2],
			[4, 100],
			[100, 1],
			[100, 1],
			[20, 10]
	]
	print("Job list: " + str(jobs))
	print("Weighted time: " + str(totalWeight(jobs))) 
	print("Time/Weight: " + str(map(tdw,jobs)))
main()













