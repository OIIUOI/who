from collections import deque

y, x = map(int, input().split(" "))
graph = [ list(map(int, input())) for _ in range(y)]

def BFS():
    que = deque((0,0))
    while que:
        ay, ax = que.popleft()

        for i in range(4):
            dy = [0, 1, -1, 0]
            dx = [-1, 0, 0, 1]
            ny, nx = ay + dy[i], ax + dx[i]

            if 0 <= ny < y and 0 <= nx < x and graph[ny][nx]:
                graph[ny][nx] = graph[ay][ax] + 1
                que.append((ny,nx))
BFS()
print(graph[y-1][x-1])