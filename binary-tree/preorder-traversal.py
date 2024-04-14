import lctk;


def preorderTraversalRecursion(root):
    node_values = []

    def function(root):
        if (not root):
            return 

        node_values.append(root.val)

        function(root.left)
        function(root.right)

        return;

    function(root)

    return node_values

binaryTree = lctk.binaryTree(["F", "B", "G", "A", "D", None, "I", None, None, "C", "E", "H"])

def preorderTraversalIterative(root):
    stack = [root]
    node_values = []

    while (stack):
        node = stack.pop()

        if (node):
            stack.append(node.right)

            node_values.append(node.val)
            
            stack.append(node.left)

    return node_values

print(preorderTraversalRecursion(binaryTree))