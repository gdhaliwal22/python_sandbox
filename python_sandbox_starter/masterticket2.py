SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100


def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


# Run this code continously until we run out of tickets
while tickets_remaining >= 1:
    # Output how many tickets remaining using the tickets_remaining variable

    print("There are {} tickets remaining".format(tickets_remaining))

    # Gather the user name and assign it to new  variable
    name = input("What is your name? ")

    # Prompt user by name and ask how many tickets they would like
    num_tickets = input("How many tickets would you like, {}? ".format(name))
    # Expect ValueError to happen and handle it
    try:
        num_tickets = int(num_tickets)
        # Raise a ValueError if request is for more tickets than are available
        if num_tickets > tickets_remaining:
            raise ValueError(
                "There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        # Include the error text in the output
        print("Not a valid # of tickets. {}. Please try agian".format(err))
    else:
        # Calculate the price num of tickets multiplied by price and assign it to a variable
        amount_due = calculate_price(num_tickets)

        # Output the price to the screen
        print("Total due is ${}".format(amount_due))

        # Prompt user if they want to proceed Y/N?
        should_proceed = input("Do you want to proceed? (Enter Y/N)")
        # If they want to proceed
        if should_proceed.lower() == "y":
            # print out to screen "SOLD!" to confirm purchase
            print("SOLD!")
        # and then decrement the tickets remaining by the number of tickets purchased
            tickets_remaining -= num_tickets
        # Otherwise....
        else:
            # Thank them by name
            print("Thank you {}".format(name))
print("Sorry tickets are sold out")
