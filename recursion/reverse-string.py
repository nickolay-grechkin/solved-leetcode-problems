def printReverse(str):
    print(len(str))
    print(helper(0, len(str) - 1, str))

def helper(startIndex, endIndex, str):
    print(startIndex, endIndex)
    print(str)

    if len(str) == 0 or startIndex - endIndex == 1 or startIndex - endIndex == 0:
        return str;
    
    if (startIndex == 2 and endIndex == 27):
        print(str[startIndex], str[endIndex])

    tmpValue = str[startIndex];
    str[startIndex] = str[endIndex]
    str[endIndex] = tmpValue

    helper(startIndex + 1, endIndex - 1, str)

    return str;         
    
# ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]
# printReverse(["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"])

printReverse(["h", "e", "l", "l", "o", "!"])