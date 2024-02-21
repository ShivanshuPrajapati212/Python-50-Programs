# Lets Code Our Program 1. Enjoy!!!

print("Kirana Calculator Pe Aap ka Swagat Hai!!!")

total = 0

while True:
    bills = input("Dam Batao : ")

    if bills == "bas":
        print(f"Abi Tak {total} Rupeya hua Hai.")
        break
    else:
        try:
            total = total + int(bills)
            print(total)

        except:
            print("Number Dalna Tha.")