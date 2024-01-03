# Vending Machine

#  There will be a number of beverage lists displayed in this area, including the prices of the beverages.

import os

Beverages = {f"Coca Cola": 1.35, "Red Bull": 1.40, "Dr Pepper": 2.00, "Fanta": 1.50}

Introduction = f"˗ˏˋ ★ ˎˊ˗ Please Select An Item ˗ˏˋ ★ ˎˊ˗"

import shutil

columns = shutil.get_terminal_size().columns

print("╭── ⋅ ⋅ ── ⋅ ⋅ D ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋆ ☆ ⋆ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ──╮".center(columns))

print("────── ⋆⋅We are glad to have you here at the Solace Saturn's Vending machine ☽ Would you like to purchase anything in particular? ˙ᵕ˙⋅⋆ ──────".center(columns))



print("⋆⋅SOLACE SATURN'S VENDING MACHINE𓇢𓆸⋅⋆".center(columns))


print("𓏲 ๋࣭ ࣪ ˖𝘉𝘌𝘝𝘌𝘙𝘈𝘎𝘌𝘚".center(columns))

print("╔═══════════════════════╗".center(columns))

print("║ Coca Cola ║  $ 1.35   ║".center(columns))
                
print("║═══════════║═══════════║".center(columns))

print("║ Red Bull  ║  $ 1.40   ║".center(columns))

print("║═══════════║═══════════║".center(columns))

print("║ Dr Pepper ║  $ 2.00   ║".center(columns))

print("║═══════════║═══════════║".center(columns))

print("║   Fanta   ║  $ 1.50   ║".center(columns))

print("╚═══════════════════════╝".center(columns))


#  In this part. When the user types a beverage, the quantity and price of the selected beverage will be displayed.

def transaction():

    item_Beverages = input("🗨  You will need to enter the name of the beverage here ➔".center(columns))
    
    item_quantity = int(input("Enter the quantity here ➔ "))
    
    if item_Beverages in Beverages:
        
        price = Beverages[item_Beverages]

        total_price = item_quantity * price

        print("Beverages:".center(os.get_terminal_size().columns))

        print(f"{item_Beverages}".center(os.get_terminal_size().columns))

        print("Quantity:".center(os.get_terminal_size().columns))

        print(f"{item_quantity}".center(os.get_terminal_size().columns))

        print("Price:".center(os.get_terminal_size().columns))

        print(f"${total_price:.2f}".center(os.get_terminal_size().columns))

        user_amount = float(input("Enter the amount: "))

        if user_amount >= total_price:

            change = user_amount - total_price

            print(f"Transaction complete ☺✓! Your change is ${change:.2f}".center(os.get_terminal_size().columns))

            return True
        
        #  Upon entering the correct answer, the following message will appear: "Transaction complete ☺✓! Your change is $"

        #  If the user has a limited amount of money or chooses to enter 1 or 0, the message will appear as follows: "Not enough money ✗!"

        #  Finally, if the user inserts an item code that does not appear in the final output. this message will appear instead: "Invalid item code ☹!"

        else:

            print("Not enough money ✗! Sorry!".center(os.get_terminal_size().columns))

    else:

        print("Invalid item code ☹!".center(os.get_terminal_size().columns))

    return False

while True:

    print(Introduction.center(os.get_terminal_size().columns))

    if not transaction():

        break

    