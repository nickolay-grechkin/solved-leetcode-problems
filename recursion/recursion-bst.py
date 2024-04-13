import lctk

def searchBST(root, val):
    if (root.val == val):
        return root
    
    if (root == None):
        return []
    
    leftSide = searchBST(root.left, val)
    rigthSide = searchBST(root.right, val)

    if (len(leftSide) == 0):
        return rigthSide
    if (len(rigthSide) == 0):
        return leftSide

binaryTree = lctk.binaryTree([4,2,7,1,3])

print(searchBST(binaryTree, 2))
        