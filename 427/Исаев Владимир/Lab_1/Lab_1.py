

def find(maze):
    d = {
        (0, 0): {"shortest distance": 0, "previous": None}
    }
    queue = [(0, 0)]
    targets = set()
    
    while len(queue) > 0:

        
        i, j = queue.pop(0)
        previous = (i, j)
        shortest_distance = d[(i, j)]["shortest distance"]

       
        for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:

            
            ni, nj = i + di, j + dj

          
            if ni < 0 or nj < 0:
                continue

            
            if ni >= len(maze) or nj >= len(maze[0]):
                continue

            
            if maze[ni][nj] not in "X-P,":
                continue

           
            if (ni, nj) not in d:
                d[(ni, nj)] = {"shortest distance": shortest_distance + 1, "previous": previous}
                queue.append((ni, nj))

            else:
                original_shortest_distance = d[(ni, nj)]["shortest distance"]
                if shortest_distance + 1 < original_shortest_distance:
                    d[(ni, nj)] = {"shortest distance": shortest_distance + 1, "previous": previous}

           
            if maze[ni][nj] == "X":
                targets.add((ni, nj))

   
    out = {}
   
    for target in targets:
        path = []
        current = target
        while current != None:
            path.append(current)
            current = d[current]["previous"]
        out[target] = path[::-1]

    return path


f = open('C:/tmp/maze-for-u.txt')

maze = []
for i in f:
    maze.append(i.replace('\n', '').replace(' ', '-'))
f.close()
while True:
    print("Введите координаты сокровища")
    x = int(input())
    y = int(input())
    if (maze[x][y] == "-"):
        maze[x] = maze[x][:y] + 'X' + maze[x][y + 1:]
        break
mypathx=[]
mypathy=[]
mypathx.append(0)
mypathy.append(maze[0].find('-'))

for k in find(maze):
    if (k[0] != 0 and k[1] != 0):
        mypathx.append(k[0])
        mypathy.append(k[1])
maze[x] = maze[x][:y] + 'P' + maze[x][y + 1:]
maze[len(maze) - 1] = maze[len(maze) - 1].replace('-', 'X')


for k in find(maze):
    if (k[0] != 0 and k[1] != 0):
        mypathx.append(k[0])
        mypathy.append(k[1])
for i in range(len(mypathx)):
    maze[mypathx[i]] = maze[mypathx[i]][:mypathy[i]] + ',' + maze[mypathx[i]][mypathy[i] + 1:]
maze[x] = maze[x][:y] + '*' + maze[x][y + 1:]

f = open('C:/tmp/maze-for-me-done.txt', 'w')
for i in maze:
    f.write(i.replace('-', ' ') + '\n')
f.close()

