current_count = [2, 1, 1]
arrangement = [''] * 4
candy = {0: '紅', 1: '藍', 2: '黃'}


def dfs(layer):
    if layer == 4:
        print(*arrangement, sep='  ')
        return

    for i in range(3):
        if current_count[i] == 0:
            continue
        current_count[i] -= 1
        arrangement[layer] = candy[i]
        dfs(layer+1)
        current_count[i] += 1


dfs(0)
