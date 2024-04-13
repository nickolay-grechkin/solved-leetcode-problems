import lctk;


def preorderTraversalRecursion(root):
    node_values = []

    def function(root):
        if (not root):
            return
        
        node_values.append(root.val);

        function(root.left);
        function(root.right);

        return;

    function(root);

    return node_values

binaryTree = lctk.binaryTree([1, 5, 6, 7, 4, None, 3, None, None, 2, 9, 8])

def preorderTraversalIterative(root):
    stack = [root]
    node_values = []

    while (stack):
        node = stack.pop()

        if (node):
            node_values.append(node.val)
            
            stack.append(node.right)
            stack.append(node.left)

    return node_values;

print(preorderTraversalIterative(binaryTree))