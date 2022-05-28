# ';' - пересечение путей
def dfs(u, visited, dist):
    visited[u] = dist
    dist += 1
    for v in edges[u]:
        if dist < visited[v]:
            dfs(v, visited, dist)

def getPath(vistied, finish, target_dist = 0):
    path = []
    if finish in visited:
        u = finish
        dist = visited[u] 
        while dist >= target_dist:
            path.append(u)
            dist -= 1
            for v in edges[u]:
                if visited[v] == dist:
                    u = v
                    break
        return path[::-1]

def getLabirint(walls, path1, path2):
    n = len(walls)
    m = len(walls[0])
    s = ''

    finish1 = path1[-1]
    path1 = set(path1[:-1])

    path2 = set(path2[:-1])

    for i in range(n):
        for j in range(m):
            c = '#'
            if walls[i][j] == 0:
                if (i, j) in path1 and (i, j) in path2:
                    c = ';'
                elif (i, j) in path1:
                    c = '.'
                elif (i, j) in path2:
                    c = ','
                elif (i, j) == finish1:
                    c = '*'
                else:
                    c = ' '
            s += c
        s += '\n'
    return s


with open('C:/Users/Xenia/OneDrive/Рабочий стол/Doc/maze-for-me-done.txt') as f:
    s = [line.strip() for line in f]

n, m = len(s), len(s[0])

cells = set()
walls = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if s[i][j] == ' ':
            cells.add((i, j))
        else:
            walls[i][j] = 1

edges = dict()
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

for i, j in cells:
    edges[(i, j)] = set()
    for di, dj in moves:
        ni, nj = i + di, j + dj
        if (ni, nj) in cells:
            edges[(i, j)].add((ni, nj))
print("Enter row and column")
start = (0, 1)
fi, fj = map(int, input().split())

finish = (fi, fj)

if finish in cells:
    visited = {c: n*m for c in cells}

    dfs(start, visited, 0)
    path1 = getPath(visited, finish, 0)
            
        
    start = (n-1, m-2)

    q = [(start, 0)]

    visited = {c: n*m for c in cells}

    while q:
        u, dist = q.pop(0)
        visited[u] = dist
        dist += 1
        for v in edges[u]:
            if dist < visited[v] and (v, dist) not in q:
                q.append((v, dist))

    path2 = getPath(visited, finish)

    res = getLabirint(walls, path1, path2)
    print(res)
    with open('maze-for-u.txt', 'w') as f:
        f.write(res)
else:
    print(finish,'is not in available cells')