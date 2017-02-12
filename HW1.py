##Class:  Graph

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
		for i in range(0, m):
			for j in range(i+1, m):
				A1 = paper.authors[i]
				A2 = paper.authors[j]
				edge = frozenset([A1, A2])
				if edge not in self.edgeSet:
					self.edgeSet.add(edge)
					
					#also update nodes for neighbours if new edge
					self.nodeDict[A1].addNeighbour(A2)
					self.nodeDict[A2].addNeighbour(A1)
		



class node:
	def __init__(self, name):
		self.name = name
		self.neighbours = [] 
		self.degree = 0 

	def addNeighbour(self, neighbour):
		self.neighbours.append(neighbour)
		self.degree = self.degree +1

class paper:
	def __init__(self, traits):
		(year, authors, title) = traits
		self.year = year
		self.authors = authors
		self.title = title



def readPapers(g):
	listOfPaper = []

	while True:
		try:
			line = g.readline().strip().split(",")
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
			break

	return listOfPaper		
	

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

	return listOfDegree


#main
  
if __name__ == "__main__":

	f = open("hw1solution.txt", 'w')
	f.write("vhl8" + "\n")

	paperF = open("HW1_data.txt", "r")
	listOfPaper = readPapers(paperF)
	listOfPaper = filter(lambda x: 1985<= x.year <=2005, listOfPaper)


	G= graph()
	for paper in listOfPaper:
		G.buildGraph(paper)	
	 

	degreeCount = questionOne(G)
	print degreeCount
	print sum(degreeCount)
	print len(G.nodeDict)
	print len(G.edgeSet)
	

	f.close
	paperF.close	 
