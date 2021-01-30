def is_prime(number):
    i = 2
    while i*i <= number:
        if number%i==0:
            return 1
        i+=1
    return 0

def sort_divisions(number):#約数列挙
    i = 2
    front, back = [],[]
    for i*i <= number:
        if number%i==0:
            front.append(i)
            if i!=number//i: back.append(number//i)
        i+=1
    return front+back[::-1]