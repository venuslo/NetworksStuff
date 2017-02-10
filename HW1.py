##Class:  Graph

class graph:
	def __init__(self):




class node:
	def __init__(self, name):
		self.name = name
		self.neighbours = [] 

	def addNeighbour(self, neighbourName):
		self.neighbours.add(neighbourName)


class paper:
	def __init__(self, traits):
		(year, number, conference, authors) = traits
		self.year = int(year)
		self.number = int(number)
		self.conference = conference
		self.authors = authors







#main
  
if __name__ == `__main__':

	f = open("hw1solution.txt")
	f.write("vhl8" + "\n")

	 
