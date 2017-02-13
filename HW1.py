import math
import matplotlib.pyplot as plt

###############################

##Classes
###############################

class graph:
	def __init__(self):
		self.nodeDict={}
		self.edgeSet = set()

	def buildGraph(self, paper):
		#put nodes into graph
		for a in paper.authors:
			if a not in self.nodeDict:
				newNode = node(a)
				self.nodeDict[a] = newNode

		#put edges into graph
		m = len(paper.authors)
		for i in range(0, m-1):
			for j in range(i+1, m):
				A1 = paper.authors[i]
				A2 = paper.authors[j]
				if A1 != A2:
					edge = frozenset([A1, A2])
					if edge not in self.edgeSet:
						self.edgeSet.add(edge)
					
					#also update nodes for neighbours if new edge
						self.nodeDict[A1].addNeighbour(self.nodeDict[A2])
						self.nodeDict[A2].addNeighbour(self.nodeDict[A1])
		



class node:
	def __init__(self, name):
		self.name = name
		self.neighbours = set() 
		self.degree = 0 

	def addNeighbour(self, neighbour):
		#since edge isn't there yet, this has to be a new neighbour
		self.neighbours.add(neighbour)
		self.degree = self.degree +1

class paper:
	def __init__(self, traits):
		(year, authors, title) = traits
		self.year = year
		self.authors = authors
		self.title = title


#########################

#functions
#########################


def readPapers(g):
	listOfPaper = []

	while True:
		try:#see if there is a line to read
			line = g.readline()
	

			line = line.strip().split(",")
	
			title = line[1]
	
			line = line[0].strip("(Ed.)").split("&")  #after removing author
			m = len(line)

			authors = []
			for i in range(1, m): #add authors 2 onwards
				authors.append(line[i].strip())

			line = line[0].strip().split(" ") #(year, [num], conf, 1st author)

			m = len(line)
			authors.append(line[m-1])
		

			year = int(line[0]) #num and conf ignored for now

			x = paper((year, authors, title))
			listOfPaper.append(x)

		except:
			if len(line[0])<=2:
				break
			else:
#				print line
				pass	
	
	return listOfPaper		
	
############################################
def questionOne(G):
	tempDict = {}

	for x in G.nodeDict:
		degree = G.nodeDict[x].degree
		if degree in tempDict:
			tempDict[degree] = tempDict[degree]+1
		else:
			tempDict[degree] = 1

	maxDegree = max(tempDict)
	listOfDegree = [0 for i in range(0, maxDegree+1)]

	for i in range(0, maxDegree+1):
		if i in tempDict:
			listOfDegree[i] = tempDict[i]

		else:
			listOfDegree[i] = 0

	return maxDegree, listOfDegree

###########################################
def questionTwo(G):
	listOfComp = []
	verticesChecked = set()

	if G.nodeDict: #i.e. if not empty, then we have at least 1 comp
		for v in G.nodeDict:
			if G.nodeDict[v] not in verticesChecked:
				(verticesChecked, currentComp) = BFS(G.nodeDict[v], verticesChecked)
				listOfComp.append(currentComp)
				

	return listOfComp
	

def BFS(v, verticesChecked):
	currentComp={v}
	verticesChecked.add(v)

	toCheck = [v]
	while toCheck:
		u = toCheck.pop(0)

		for w in u.neighbours:
			if w not in verticesChecked:
				currentComp.add(w)		
				verticesChecked.add(w)
				toCheck.append(w)

	return (verticesChecked, currentComp)
		
#############################

def questionThree(root):
	distanceDict = BFSDistance(root)

	distances = [distanceDict[x] for x in distanceDict]
	maxDist = max(distances)
	distanceCount = []

	for j in range(0, maxDist+1):
		r_j = len(filter(lambda x: x == j, distances))
		distanceCount.append(r_j)

	return (maxDist, distanceCount, distances, distanceDict)


def BFSDistance(root):

	distDict = {} 
	distDict[root.name] = 0

	toCheck = [root]

	while toCheck:
		u = toCheck.pop(0)
		
		for w in u.neighbours:
			if w.name not in distDict:
				distDict[w.name] = distDict[u.name]+1
				toCheck.append(w)

	return distDict	




def questionFour(maxDist, distDict, distCount):

	potentParent = [0 for i in range(1, maxDist+1)]

	for v in distDict:
		neighboursOfV = G.nodeDict[v].neighbours
		parents = filter(lambda x: distDict[x.name] == distDict[v] -1, neighboursOfV)
		potentParent[distDict[v]-1] = potentParent[distDict[v]-1] + len(parents)
	

	listOfP_j = [round(potentParent[i]* 1.0 / distCount[i], 3) for i in range(0, maxDist)]
	
	return listOfP_j	
	
########################

#main
########################  
if __name__ == "__main__":

	f = open("hw1solution.txt", 'w')
	f.write("vhl8" + "\n")

	paperF = open("HW1_data.txt", "r")
	listOfPaper = readPapers(paperF)
	listOfPaper = filter(lambda x: 1985<= x.year <=2005, listOfPaper)


	G= graph()
	for paper in listOfPaper:
		G.buildGraph(paper)	
	 
	numOfNodes = len(G.nodeDict)
	numOfEdges = len(G.edgeSet)

	####################
	#Question 1:
	(maxD, degreeCount) = questionOne(G)
	for i in range(0, maxD+1):
		f.write("@ 1 "+ str(i) + " " + str(degreeCount[i])+ "\n")
		
	#set up scatterplot
	x=[]
	y=[]
	for i in range(1, maxD+1):
		if degreeCount[i]!=0:
			x.append(math.log(i))
			y.append(math.log(degreeCount[i]))

	fig = plt.figure()
	plt.xlabel("Log of degree")
	plt.ylabel("Log of number of nodes")
	plt.title("Question 1:  Log-degree Log-Nodes Plot")
	plt.plot(x, y)
	fig.savefig("plot1.png")
	plt.close(fig)

	#############
	#Q1 checker take logs first
#	total =0
#	for i in range(0, len(x)):
#		total = x[i]*y[i]+ total
#	total = total/2.0
#
#	print "Q1 check edges" + str(total)



	#########################
	#Question 2

	components = questionTwo(G)
	sizeOfComp = map(lambda x: len(x), components)

	maxComp = max(sizeOfComp)
	ratioComp = round(maxComp*1.0/numOfNodes, 3)

	f.write("@ 2 " + str(maxComp) + " " + str(numOfNodes) + " " + str(ratioComp)+ "\n")

	cStar = max(filter(lambda x: x < maxComp, sizeOfComp)) #look at everything smaller than max

	#output and set up scatterplot
	x=[]
	y=[]
	for j in range(1, cStar+1):
		k_j = len(filter(lambda x: x==j, sizeOfComp))
		f.write("@ 2 " + str(j) + " " + str(k_j)+"\n")
	
		if k_j!=0:
			x.append(math.log(j))
			y.append(math.log(k_j))

	fig = plt.figure()
	plt.xlabel("Log of component size")
	plt.ylabel("Log of number of components")
	plt.title("Question 2:  Log-component size vs Log-Num of components")
	plt.plot(x, y)
	fig.savefig("plot2.png")
	plt.close(fig)
	
	#########
	#Q2 checker take logs first
	#total = maxComp
	#for i in range(0, len(x)):
	#	total = total + x[i]*y[i]
	

	#print "Q2 check nodes" + str(total) 



	#######################
	#Question 3
	
	root = G.nodeDict["Hartmanis"]
	
	(maxDist, distCount, distances, distDict) = questionThree(root) 
	for j in range(1, maxDist+1):
		f.write("@ 3 " + str(j) + " " + str( distCount[j]) + "\n")

	bins = [i for i in range(1, maxDist+1)]

	fig = plt.figure()
	plt.xlabel("Distance from Hartmanis")
	plt.ylabel("Number of nodes at this distance")
	plt.title("Question 3:  Count of distance from Hartmanis")
	plt.hist(distances, bins)
	fig.savefig("plot3.png")
	plt.close(fig)


	####
	#Q3 checker

	#rootComp = filter(lambda x: root in x, components)[0]
	#print len(rootComp) == sum(distCount) + 1
	


	##############################
	#Question 4
	distCount.pop(0)
	listOfP_j = questionFour(maxDist, distDict, distCount)

	for j in range(1, maxDist+1):
		f.write("@ 4 " + str(j) + " " + str(listOfP_j[j-1]) + "\n")

		
	fig = plt.figure()
	plt.xlabel("Distance from Hartmanis")
	plt.ylabel("Average number of parents")
	plt.title("Question 4:  Average number of parents on BFS rooted on Hartmanis")
	plt.bar(bins, listOfP_j, align = 'center')
	fig.savefig("plot4.png")
	plt.close(fig)

	f.close
	paperF.close	 

	#checks
	print "nodes" + str(numOfNodes)
	print "edges" + str(numOfEdges)
	print "isolated" + str(degreeCount[0])
