#	SuGo, 13 August 2018
#	BFS or level order traversal of a graph
import collections

def BFS(graph, root):
	visited, queue = set(), collections.deque([root])
	while queue:
		vertex = queue.popleft()
		print("visisted vertex  ", vertex)
		for neighbor in graph[vertex]:
			if neighbor not in visited:
				visited.add(neighbor)
				queue.append(neighbor)
	print("Queue:: ", queue)
	print("visited:: ", visited)

def DFS(graph, start):
	visited, stack = set(), [start]
	#stack.push(start)
	while stack:
		vertex = stack.pop()
		print("popped vertex:: ", vertex)
		for neighbor in graph[vertex]:
			if neighbor not in visited:
				visited.add(neighbor)
				stack.append(neighbor)
	print("Queue:: ", stack)
	print("visited:: ", visited)


if __name__ == '__main__':
	graph = {0:[1, 2], 1:[2, 4], 2:[3], 3:[], 4:[]}
	print("graph", graph)
	print("BFS ::  \n")
	BFS(graph, 0)
	print("DFS:  \n")
	DFS(graph, 0)	
