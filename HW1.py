##Class:  Graph

class graph:
	def __init__(self):
		nodeDict={}

	def addNode(self, name):
		nodeDict[name] = node(name)



class node:
	def __init__(self, name):
		self.name = name
		self.neighbours = [] 

	def addNeighbour(self, neighbourName):
		self.neighbours.add(neighbourName)


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
			print('ok')
			line = g.readline().strip().split(",")
			print line
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
	



#main
  
if __name__ == "__main__":

	f = open("hw1solution.txt", 'w')
	f.write("vhl8" + "\n")

	paperF = open("HW1_data.txt", "r")
	listOfPaper = readPapers(paperF)
	print len(listOfPaper)
	listOfPaper = filter(lambda x: 1985<= x.year <=2005, listOfPaper)

	 

	f.close
	paperF.close	 
