num = int(input("Enter a number: "))
c=0
if num > 1:
    for i in range(2, int(num**0.5)+1 ):
        if num % i == 0:
            print(num, "is not a prime number")
            c=c+1
            break
    if c==0:
        print(num, "is a prime number.")

else:
    print(num, "is not a prime number" )