# Recursive alghoritm with memoization

def fibRecursive(n: int) -> int:
    cache = {}

    def fibNum(val):
        if (val in cache):
            return cache[val];
    
        if (val < 2):
            result = val
        else:
            result = fibNum(val - 1) + fibNum(val - 2)

        cache[val] = result
        return result

    return fibNum(n);    

# Binet’s Simplified Formula for finding Fibonacci terms

def fib(n):
    golden_ratio = (1+5**0.5)/2;

    return round((golden_ratio**n)/5**0.5)

print(fib(30))