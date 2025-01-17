'''m, n = map(int,input().split())
mg = []
for i in range(m):
    c = list(map(int,input().split()))
    mg.append(c)
for i in range(m):
    for j in range(n):
        k = mg[i][j]
        mg[i][j] = [k, False]
sx, sy = map(int,input().split())
edx, edy = map(int,input().split())
s = []
road = ''
def findRoad(x, y, road):
    mg[x][y][1] = True
    preroad = road
    if x == edx - 1 and y == edy - 1:
        road += f'({x + 1},{y + 1})'
        s.append(road)
    else:
        road += f'({x + 1},{y + 1})->'
        if x - 1 > 0 and mg[x - 1][y][0] != 0 and mg[x - 1][y][1] == False:#up
            findRoad(x - 1, y, road)
            mg[x - 1][y][1] = False
            road = preroad
        if y + 1 < n and mg[x][y + 1][0] != 0 and mg[x][y + 1][1] == False:#right
            findRoad(x, y + 1, road)
            mg[x][y + 1][1] = False
            road = preroad
        if x + 1 < m and mg[x + 1][y][0] != 0 and mg[x + 1][y][1] == False:#down
            findRoad(x + 1, y, road)
            mg[x + 1][y][1] = False
            road = preroad
        if y - 1 > 0 and mg[x][y - 1][0] != 0 and mg[x][y - 1][1] == False:#left
            findRoad(x, y - 1, road)
            mg[x][y - 1][1] = False
            road = preroad
findRoad(sx - 1,sy - 1, road)
for i in s:
    print(i)'''
def dfs(maze, m, n, x, y, end_x, end_y, path, visited, all_paths):
    # 基本条件：到达终点
    if (x, y) == (end_x, end_y):
        all_paths.append(path[:])
        return
    
    # 四个方向：上、右、下、左
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # 递归探索四个方向
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 判断新位置是否有效且没有被访问过
        if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 1 and (nx, ny) not in visited:
            visited.add((nx, ny))  # 标记为已访问
            path.append((nx + 1, ny + 1))  # 记录该点，注意输出坐标从1开始
            # 继续探索
            dfs(maze, m, n, nx, ny, end_x, end_y, path, visited, all_paths)
            # 回溯
            visited.remove((nx, ny))
            path.pop()

def find_paths(maze, m, n, start_x, start_y, end_x, end_y):
    if maze[start_x][start_y] == 0 or maze[end_x][end_y] == 0:
        return []  # 起点或终点是障碍，返回空路径
    
    all_paths = []
    visited = set()
    visited.add((start_x, start_y))
    dfs(maze, m, n, start_x, start_y, end_x, end_y, [(start_x + 1, start_y + 1)], visited, all_paths)
    return all_paths

def main():
    m, n = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(m)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    
    # 调整为从0开始索引
    start_x -= 1
    start_y -= 1
    end_x -= 1
    end_y -= 1
    
    paths = find_paths(maze, m, n, start_x, start_y, end_x, end_y)
    
    if paths:
        for path in paths:
            print("->".join(f"({x},{y})" for x, y in path))
    else:
        print(-1)

# 执行程序
if __name__ == "__main__":
    main()