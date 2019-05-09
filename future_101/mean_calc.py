# fractional code
# elif command == "average":
how_many = input("How many numbers> ")
how_many = int(how_many)
total = 0
for number_count in range(how_many):
    number = input("Enter number " + str(number_count) + "> ")
    total = total + int(number)
result = total / how_many
print("the average = " + str(result))
