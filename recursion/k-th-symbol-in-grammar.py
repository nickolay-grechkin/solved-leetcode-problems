def kthGrammar(n: int, k: int) -> int:
    
    def function(n, index):
        if (n == 0):
            return 0 if index == 1 else 1;

        previousRowNodesQuantity = pow(2, n - 1);

        res = function(n - 1, index - previousRowNodesQuantity if index > previousRowNodesQuantity else index);

        if (index > previousRowNodesQuantity):
            return 0 if res == 1 else 1;
        return res;


    return function(n - 1, k)


print(kthGrammar(6, 26))

