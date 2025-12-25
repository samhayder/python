def is_prime(num):
    count = 0
    for i in range(1,num):
        if num % i == 0:
            count = 1
        else:
            count = 0
    if count == 0:
        print("True")
    else:
        print("False")

is_prime(73)