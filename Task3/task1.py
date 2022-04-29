
class pawn:
	
	def __init__(self, x = 0, y = 0, dist = 0):
		self.x = x
		self.y = y
		self.dist = dist

def isInside(x, y, N):
	if (x >= 1 and x <= N and
		y >= 1 and y <= N):
		return True
	return False

def howManySteps(N):
	
	dx = [2, 2, -2, -2, 1, 1, -1, -1]
	dy = [1, -1, 1, -1, 2, -2, 2, -2]
	
	queue = []
	
	
	queue.append(pawn(N))
	
	visited = [[False for i in range(N + 1)]
					for j in range(N + 1)]
	
	

	
	
	while(len(queue) > 0):
		
		t = queue[0]
		queue.pop(0)
		
		
			
		
		for i in range(8):
			
			x = t.x + dx[i]
			y = t.y + dy[i]
			
			if(isInside(x, y, N) and not visited[x][y]):
				visited[x][y] = True
				queue.append(pawn(x, y, t.dist + 1))


if __name__=='__main__':
	N = int(input())
	print(howManySteps(N))
	

