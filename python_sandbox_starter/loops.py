x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [int(i) for i in x if int(i) % 2 == 0]

print(y)
