# Lets Code Our Program 3. Enjoy!!!

with open('Currency-Rates.txt') as f:  # Reading the file with open fuc
    a = f.readlines()                  # making variable 'a' to read the 'whole line' of data in Currency-Rates.txt

curlist = []            # Making a empty list for appending data using for loop and 'spit' fuc in srting slicing in a list

for item in a:          # Creating the loop for appending items in the list
    curlist.append(item.split(' '))
    

userInput = int(input("Enter the Number : "))  # User input
    
for i in curlist:               # Using for loop to print all the values in ones
    print(f"{userInput} Rupees is equal to {float(i[2])*userInput} {i[0]} {i[1]}")   # Printing the values using f string


# Data For Currency-Rates.txt

# Mauritian Rupee 0.564951 1.770065
# Mexican Peso 0.205500 4.866173
# Nepalese Rupee 1.600750 0.624707
# New-Zealand Dollar 0.019667 50.846559
# Norwegian Krone 0.125865 7.945012
# Omani Rial 0.004638 215.614735
# Pakistani Rupee 3.364907 0.297185
# Philippine Peso 0.674085 1.483492
# Polish Zloty 0.048509 20.614769
# Qatari Riyal 0.043847 22.806589
# Romanian-New Leu 0.055629 17.976086
# Russian Ruble 1.110915 0.900159
# Saudi-Arabian Riyal 0.045172 22.137596
# Singapore Dollar 0.016215 61.673149
# South-African Rand 0.227541 4.394817
# South-Korean Won 16.042502 0.062334
# Sri-Lankan Rupee 3.765537 0.265566
# Swedish Krona 0.125748 7.952400
# Swiss Franc 0.010610 94.247628
# Taiwan-New Dollar 0.378021 2.645356
# Thai Baht 0.434915 2.299301
# Trinidadian Dollar 0.081639 12.249021
# Turkish Lira 0.371514 2.691691
# US Dollar 0.012046 83.015986
# Venezuelan Bolivar 43591.904568 0.000023