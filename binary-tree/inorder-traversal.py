import lctk

def inorderTraversalRecursion(root):
    node_values = []

    def function(root):
        if not root:
            return
        
        function(root.left)
        node_values.append(root.val)
        function(root.right)

        return
    
    function(root)

    return node_values;

binaryTree = lctk.binaryTree(["F","B","G", "A", "D", None, "I", None, None, "C", "E", "H"])
res, stack = [], [(binaryTree, False)]

print(stack)
# binaryTree = lctk.binaryTree([1])

def inorderTraversalIterative(root):
    node_values, stack = [], [(root, False)]

    while stack:
        node, visited = stack.pop()
        
        if node:
            if visited:
                node_values.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
    return node_values

print(inorderTraversalIterative(binaryTree))