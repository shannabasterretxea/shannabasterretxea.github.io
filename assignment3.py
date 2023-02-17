# Converting from base 10 to base 2 and base 8

# Ask for input to the user 
num = int(input("Enter a number in base 10: "))


# Convert to base 2 and print the conversion
bin_num = bin(num)
print("Conversion to base 2: " + str(bin_num))


# Convert to base 8 and print the conversion
oct_num = oct(num)
print("Conversion to base 8: " + str(oct_num))

