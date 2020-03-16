first_name = input("What is your first name? ")
print("Hello, ", first_name)
# if / elif statement
if first_name == "Craig":
    print(first_name, "is learning Python")
elif first_name == "Max":
    print(first_name, "is learning with fellow students in the COmunity! Me too!")
else:
    # This is just in case we have a younger user who can't yet read
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow you're {}! If you're conmfident with reading already...".format(age))
    print("You should totally learn Python, {}!".format(first_name))
# .format adds the first_name to the brackets
print("Have a great day {}!".format(first_name))
