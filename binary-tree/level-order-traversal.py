import collections;

def levelOrderWithTuples(root):
    stack = [(root, 0)]
    nodes = []

    while stack:
        node, level = stack.pop()
        if node: 
            stack.append((node.right, level+1))
            stack.append((node.left, level+1))

            if level >= len(nodes):
                nodes.append([])

            nodes[level].append(node.val)
    return nodes

def levelOrderWithoutTuples(root):
    queue, nodes = collections.deque(), []    
    queue.append(root)

    while queue:
        level = []
        level_len = len(queue);

        for _ in range(level_len):
            node = queue.popleft();
            if node:
                level.append(node.val)
                queue.appendleft(node.right)
                queue.appendleft(node.left)
            
            if level:
                nodes.append(level)
        return nodes
