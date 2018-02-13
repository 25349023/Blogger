class Node:
    def __init__(self, s):
        self.data = s
        self.next = [None, None, None]


def build_tree():
    root = Node('red-1')
    root.next[0] = Node('orange-2')
    root.next[1] = Node('lime-3')
    root.next[2] = Node('green-4')
    root.next[0].next[0] = Node('yellow-5')
    root.next[2].next[0] = Node('blue-6')
    root.next[2].next[1] = Node('violet-7')

    return root


def dfs(start):
    if start is None:
        return
    print(start.data, ' visited.')
    for i in range(3):
        dfs(start.next[i])


tree = build_tree()
dfs(tree)
