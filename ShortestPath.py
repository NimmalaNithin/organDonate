import sys

class Graph():

	def __init__(self, vertices,graph):
		self.V = vertices
		#self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
		self.graph=graph
		self.outputs=[]

	def printSolution(self, dist):
		#print("Vertex \tDistance from Source")
		for node in range(self.V):
			#print(node, "\t", dist[node])
			self.outputs.append(dist[node])
		

	def minDistance(self, dist, sptSet):
		min = sys.maxsize
		min_index=sys.maxsize
		for u in range(self.V):
			if dist[u] < min and sptSet[u] == False:
				min = dist[u]
				min_index = u
		return min_index

	def dijkstra(self, src):
		dist = [sys.maxsize] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):
			x = self.minDistance(dist, sptSet)
			sptSet[x] = True
			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
					dist[y] = dist[x] + self.graph[x][y]

		self.printSolution(dist)


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]]
#g=Graph(9,graph)
#g.dijkstra(2)
#sprint(g.outputs)