
def sort_divisions(number):#約数列挙
    i = 1
    front, back = [],[]
    while i*i <= number:
        if number%i==0:
            front.append(i)
            if i!=number//i: back.append(number//i)
        i+=1
    return front+back[::-1]