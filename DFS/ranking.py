visited = [False] * 5
arrangement = [''] * 3
people = ['甲', '乙', '丙', '丁', '戊']


def dfs(layer):
    if layer == 3:
        print(*arrangement, sep='  ')
        return

    for i in range(5):
        if visited[i]:
            continue
        visited[i] = True
        arrangement[layer] = people[i]
        dfs(layer + 1)
        visited[i] = False


dfs(0)
