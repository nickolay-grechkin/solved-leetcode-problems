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
# binaryTree = lctk.binaryTree([1])

def inorderTraversal(root):
    if not root:
        return []
    
    stack, visited, node_values = [root], [], []

    while stack:
        node = stack.pop()
            
        if node.right and not node in visited:
            stack.append(node.right)
        if node.left:
            if node in visited:
                node_values.append(node.val)
            else:
                stack.append(node)
                stack.append(node.left)
        if not node.left:
            node_values.append(node.val)

        visited.append(node) 
        

    return node_values

print(inorderTraversalIterative(binaryTree))