def postorderTraversalRecursion(root):
    node_values = []

    def function(root):
        if not root:
            return
        
        function(root.left)
        function(root.right)
        
        node_values.append(root.val)
        
        return
    function(root)

    return node_values

def postorderTraversalIterative(root):
    node_values, stack = [], [(root, False)]

    while stack:
        node, visited = stack.pop()

        if visited:
            node_values.append(node.val)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

    return node_values