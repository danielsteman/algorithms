def dfs(tree, start):
    visited = set()
    stack = [start]

    nodes = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            nodes.append(node)
            stack.extend(reversed(tree[node]))

    return nodes
