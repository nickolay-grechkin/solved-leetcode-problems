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
    node_values, visited, stack = [], [], [root]

    while stack:
        node = stack.pop()

        if node not in visited:
            if node.right or node.left:
                stack.append(node)
            if node.right:
                node.append(node.right)
            if node.left:
                node.append(node.left)
            if not node.left and not node.right:
                node_values.append(node.val)
        else:
            node_values.append(node.val)
        visited.append(node)
