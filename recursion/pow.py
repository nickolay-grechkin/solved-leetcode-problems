def myPow(x: float, n: int) -> float:
    def calculatePow(x, n):
        
        if (n == 0):
            return 1;
        
        if (n == 1):
            return x;
        
        res = calculatePow(x, n // 2);
        
        if (n % 2 == 0):
            return res * res;
        else:
            return res * res * x;
    
    return 1 / calculatePow(x, abs(n)) if n < 0 else calculatePow(x, abs(n));

    


print(myPow(-1, 2147483647))

'''
    1. Implement alghoritm to calculate even exponent
    2. Implement alghoritm to calculate even and odd exponents
    3. Implement alghoritm to calculate negative exponents
'''

'''
    Test cases:

    x = 2.0
    n = 214748364
    result = 0

    x = -1
    n = 2147483647
    result = -1

    x = 1
    n = 214748364
    result = 1

    x = 1.0
    n = 2147483647
    result = 1
'''