gesture = ['剪刀', '石頭', '布']
visited = [False] * 3
arrangement = [''] * 3


def dfs(layer):
    if layer == 3:
        print(*arrangement, sep='\t\t')
        return

    for i in range(3):
        if visited[i]:
            continue
        visited[i] = True
        arrangement[layer] = gesture[i]
        dfs(layer + 1)
        visited[i] = False

dfs(0)
