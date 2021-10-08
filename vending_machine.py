"""
// Author: David Tung
// This is just a prototype program
// Belows are what I would do if given more time
// TODO: Reorganize it into a class
// TODO: Validate the input
// TODO: Create a database for storing items info
// TODO: Create functions to remove/add/update items info
"""

def vending_machine():
    # This is just a shortcut to store items info temporarily
    # TODO: Move it to a database or a model and build a functionality to add new items.
    menu = {
        "1": {
            "name": "Candy Bar",
            "price": 200,
        },
        "2": {
            "name": "Chips",
            "price": 150,
        },
        "3": {
            "name": "Soda",
            "price": 100,
        }
    }

    print("Welcome to Neurotrack Vending Machine!")
    # TODO: getting the items from the dataset instead
    print(
        """
        1) Candy Bar: $2.00
        2) Chips: $1.50
        3) Soda: $1.00
        """
    )

    # TODO: Validate the input
    choice = input("Please enter the item number you would like to purchase: ")
    coins = input("Please insert coins (5¢, 10¢, 25¢, $1, $2): ")
    # TODO: need to convert to cents if $1 or $2 is inserted
    total = int(coins)

    while total < menu[choice]["price"]:
        # TODO: Show the remaining coins needed for the item
        more_coins = input(f"Total coins inserted: {total} Please insert more coins: ")
        total += int(more_coins)

    change = total - menu[choice]["price"]

    if change > 0:
        print(f"{change} is your change")
    print(f"Thank you for purchasing {menu[choice]['name']}!")


if __name__ == '__main__':
    vending_machine()
