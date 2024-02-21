# Lets Code Our Program 2. Enjoy!!!

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)

def factorialTrailingZeros(number):
    fac = factorial(number)
    print(fac)
    count = 0 
    while (fac%10 == 0):
        count = count +1 
        fac = fac/10
    return count
if __name__ == "__main__":
    number = int(input("Enter The Number : "))

    fact = factorial(number)
    print(f"The factorial is {fact}")
    print(factorialTrailingZeros(number))


# I don't know what this is ...