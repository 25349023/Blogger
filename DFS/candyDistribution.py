current_count = [2, 1, 1]  # 用來儲存各還有幾顆糖果
arrangement = [''] * 4
candy = {0: '紅', 1: '藍', 2: '黃'}


def dfs(layer):
    if layer == 4:
        print(*arrangement, sep='  ')
        return

    for i in range(3):
        if current_count[i] == 0:  # 如果沒有剩下了
            continue
        current_count[i] -= 1  # 用掉一顆
        arrangement[layer] = candy[i]
        dfs(layer + 1)  # 下一層 DFS
        current_count[i] += 1
        

dfs(0)
