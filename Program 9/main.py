# Lets Code Our Program 9. Enjoy!!!

print("Welcome To MyCal.com !!!")

print("""
Enter + for Addition
Enter - for Subtraction
Enter X for Multiplication
Enter / for Division
Enter q to Quit
""")
while True:
    
    operation = input("Enter the Operation : ")

    if operation == 'q':
        print("Thanks for using Me!!!")
        break

    input_1 = int(input("Enter the First Number : "))
    input_2 = int(input("Enter the Sencond Number : "))

    if operation == '+':
        print(f"The Sum of Both Numbers is {input_1+input_2}")
    
    elif operation == '-':
        print(f"The Diffrence of Both Numbers is {input_1-input_2}")
    
    elif operation.lower() == 'X':
        print(f"The Product of Both Numbers is {input_1*input_2}")
    
    elif operation == '/':
        print(f"The Division of Both Numbers is {input_1/input_2}")
    else:
        print("Error....")