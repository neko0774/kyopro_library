def gcd(x,y):#最大公約数
    while y:
        x,y = y,x%y
    return x

def lcm(x,y):#最小公倍数
    return x * y // gcd (x, y)

def ceil(x,y):
    if x%y == 0:
        return x//y
    else:
        return x//y+1

def floor(x,y):
    if x%y==0:
        return x//y
    else:
        return x//y-1