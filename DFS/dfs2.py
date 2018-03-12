inf = -1
e = []
visited = [False] * 7


def dfs(now):
    print(now, ' visited.')
    for j in range(1, 7):
        if not visited[j] and e[now][j] == 1:
            visited[j] = True
            dfs(j)


for i in range(0, 7):
    e.append([inf] * 7)  # e[i][j] 為 i 到 j 的距離, inf 代表走不到
for i in range(1, 7):
    e[i][i] = 0  # 0 代表就是自己

for i in range(0, 8):
    a, b = input().split()
    a, b = int(a), int(b)
    e[a][b] = 1  # 1 代表可以走到
    e[b][a] = 1

visited[1] = True
dfs(1)
