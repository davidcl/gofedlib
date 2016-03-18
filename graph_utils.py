class GraphUtils(object):

	# based on http://www.fit.vutbr.cz/study/courses/GAL/public/gal-slides.pdf
	@staticmethod
	def transposeGraph(graph):
		nodes, edges = graph
		tedges = {}
		for u in edges:
			for v in edges[u]:
				# (u,v) -> (v,u)
				if v not in tedges:
					tedges[v] = [u]
				else:
					tedges[v].append(u)

		return (nodes, tedges)

	@staticmethod
	def getLeafPackages(graph):
		nodes, edges = graph

		leaves = []

		for u in nodes:
			# u has no edges or edges[u] is empty
			if u not in edges or edges[u] == []:
				leaves.append(u)

		return leaves

	@staticmethod
	def getRootPackages(graph):
		nodes, edges = graph

		visited = {}
		for u in nodes:
			visited[u] = 0

		for u in nodes:
			if u in edges:
				for v in edges[u]:
					visited[v] = 1

		roots = []
		for u in nodes:
			if visited[u] == 0:
				roots.append(u)

		return roots

	@staticmethod
	def joinGraphs(g1, g2):
		g1_nodes, g1_edges = g1
		g2_nodes, g2_edges = g2

		nodes = g1_nodes
		edges = g1_edges

		for u in g2_nodes:
			if u not in nodes:
				nodes.append(u)

			if u not in g2_edges:
				continue

			for v in g2_edges[u]:
				if u in edges:
					if v in edges[u]:
						continue
					edges[u].append(v)
				else:
					edges[u] = [v]

		return (nodes, edges)

	@staticmethod
	def getSCCs(graph):
		return SCCBuilder(graph).build().getSCC()

	@staticmethod	
	def getReacheableSubgraph(graph, node)
		nodes, edges = graph
		dfs = DFS(graph)
		reacheable = dfs.DFSSimpleWalk(node)

		r_edges = {}
		for u in reacheable:
			if u not in edges:
				continue

			r_edges[u] = []
			for v in edges[u]:
				if v in reacheable:
					r_edges[u].append(v)

		return (reacheable, r_edges)

class SCCBuilder(object):

	def __init__(self, graph)
		self._graph = graph
		self._sccs = []

	def getSCC(self):
		return self._sccs

	def build(self):
		nodes, edges = self._graph
		f, d = DFS(self._graph).DFSWalk()
		tgraph = transposeGraph(self._graph)
		start_nodes, pred = DFS(tgraph).DFSWalk(f)
		trees = []
		for node in start_nodes:
			trees.append(self._getSucc(node, pred))
	
		# some trees can overlap
		sccs = []
		for i_tree in trees:
			iss = False
			for j_tree in trees:
				if i_tree == j_tree:
					continue
				if set(i_tree).issubset(j_tree):
					iss = True
			if iss == False:
				sccs.append(i_tree)
	
		self._sccs = sccs

		return self

	@staticmethod
	def _getSucc(s, pred):
		if pred[s] == '':
			return [s]
		else:
			return [s] + self._getSucc(pred[s], pred)

class DFS:

	def __init__(self, graph):
		self.nodes, self.edges = graph

		self.WHITE=0
		self.GRAY=1
		self.BLACK=2

		self.color = {}
		self.d = {}
		self.f = {}
		self.time = 0
		self.pred = {}

	def DFSVisit(self, node):
		self.color[node] = self.GRAY
		self.time += 1
		self.d[node] = self.time

		if node in self.edges:
			for adj in self.edges[node]:
				if self.color[adj] == self.WHITE:
					self.pred[adj] = node
					self.DFSVisit(adj)

		self.color[node] = self.BLACK
		self.time += 1
		self.f[node] = self.time

	def DFSSimpleWalk(self, start_node):
		for node in self.nodes:
			self.color[node] = self.WHITE
			self.pred[node] = ""

		self.time = 0
		self.DFSVisit(start_node)

		reachable = []		
		for node in self.nodes:
			if self.color[node] != self.WHITE:
				reachable.append(node)

		return reachable

	def DFSWalk(self, f = []):
		for node in self.nodes:
			self.color[node] = self.WHITE
			self.pred[node] = ""

		self.time = 0

		if f == []:
			for node in self.nodes:
				if self.color[node] == self.WHITE:
					self.DFSVisit(node)
			return (self.f, self.d)
		else:
			start_nodes = []
			for node, _ in sorted(f.items(), key=operator.itemgetter(1), reverse=True):
				if self.color[node] == self.WHITE:
					self.DFSVisit(node)
				start_nodes.append(node)

			return (start_nodes, self.pred)





