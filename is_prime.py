def is_prime(number):
    i = 2
    while i*i <= number:
        if number%i==0:
            return 1
        i+=1
    return 0