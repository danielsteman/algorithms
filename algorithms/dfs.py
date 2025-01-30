def dfs(tree, start):
    visited = set()
    stack = [start]

    nodes = []

    while stack:
        print(f"stack: {stack}")
        node = stack.pop()  # get last item from stack
        print(f"node: {node}")
        if node not in visited:
            visited.add(node)
            stack.extend(reversed(tree[node]))

            # keep track of traversed nodes
            nodes.append(node)

    return nodes
