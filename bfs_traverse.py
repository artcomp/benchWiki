import time
# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph: 
  
	# Constructor 
	def __init__(self): 
  
		# default dictionary to store graph 
		self.graph = defaultdict(list) 
  
	# function to add an edge to graph 
	def addEdge(self,u,v):
		
		self.graph[u].append(v) 
  
	# Function to print a BFS of graph 
	def BFS(self, s): 
  
		# Mark all the vertices as not visited 
		visited = [False] * (len(self.graph)) 
  
		# Create a queue for BFS 
		queue = [] 
  
		# Mark the source node as  
		# visited and enqueue it 
		queue.append(s) 
		visited[s] = True
  
		while queue: 
  
			# Dequeue a vertex from  
			# queue and print it 
			s = queue.pop(0) 
			print (s) 

			# Get all adjacent vertices of the 
			# dequeued vertex s. If a adjacent 
			# has not been visited, then mark it 
			# visited and enqueue it 

			for i in self.graph[s]: 
				try:
					if visited[i] == False: 
						queue.append(i) 
						visited[i] = True
				except:
					pass
			
# Create a graph given in 
# the above diagram 
def main():

	for i in range(10):
		start_time = time.time()

		g = Graph() 

		l = []
		with open("wiki.txt", "r") as f:
			l = [(line.split()[0], line.split()[1]) for line in f]
		
		for i in l:
			print i[0], i[1]
			g.addEdge(long(i[0]), long(i[1]))

		# print ("Following is Breadth First Traversal (starting from vertex 0)") 
		g.BFS(3) 
		print("\n")

   
		final_time = (time.time() - start_time)
		print(final_time)
		with open("Ubuntu_2GB_1CPU.txt", "a") as f:
			f.write(str(final_time)+'\n')


if __name__ == '__main__':
	main()
