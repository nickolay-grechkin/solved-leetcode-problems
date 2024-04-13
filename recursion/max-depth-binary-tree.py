import lctk

def maxDepth(root) -> int:
    depth = 0;

    def calculateDepth(root, depth):
        if (root == None):
            return depth;

        depth += 1;
            
        return max(calculateDepth(root.left, depth), calculateDepth(root.right, depth));
        
    return calculateDepth(root, depth);



maxDepth(lctk.binaryTree([1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1, None, 1, 1, 1, 1]));

arr = [1, 2]

print(pow(2.00000, 10))