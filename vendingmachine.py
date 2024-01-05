# Vending Machine

#  There will be a set of numbers of beverage lists displayed in this area, including the prices of the beverages.

#  Aligning the text to the middle.

import os

Beverages = {f"COCA COLA": 1.35, "RED BULL": 1.40, "DR PEPPER": 2.00, "SPRITE": 2.10, "FANTA": 1.50, "PEPSI": 2.20, "LIPTON": 2.25, "SUNKIST": 1.75, "7UP": 2.55}

Introduction = f"˗ˏˋ ★ ˎˊ˗ Please Select An Item ˗ˏˋ ★ ˎˊ˗"

import shutil

columns = shutil.get_terminal_size().columns

#  Implemented a design using print function in python In order to make it appear more visually engaging and captivating to the eye.

print("╭── ⋅ ⋅ ── ⋅ ⋅ D ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋆ ☆ ⋆ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ──╮".center(columns))

print("────── ⋆⋅We are glad to have you here at the Solace Saturn's Vending machine ☽ Would you like to purchase anything in particular?⋅⋆ ──────".center(columns))

print("Try our Solace Saturn's Vending Machine and drink your heart out! ˙ᵕ˙".center(columns))

#  Title of the vending machine.

print("⋆⋅SOLACE SATURN'S VENDING MACHINE𓇢𓆸⋅⋆".center(columns))

print("╭─────── ୨୧ ───────╮".center(columns))

print("BEVERAGES❀".center(columns))

print("╰──────────────────╯".center(columns))

print(" ".center(columns))

print("⊹˚₊‧╔═══════════════════════╗‧₊˚⊹".center(columns)) 

print("║ COCA COLA ║  $ 1.35   ║".center(columns))
                
print("║═══════════║═══════════║".center(columns))

print("║ RED BULL  ║  $ 1.40   ║".center(columns))

print("║═══════════║═══════════║".center(columns))

print("║ DR PEPPER ║  $ 2.00   ║".center(columns))

print("║═══════════║═══════════║".center(columns))

print("║  SPRITE   ║  $ 2.10   ║".center(columns))

print("║═══════════║═══════════║".center(columns))

print("║   FANTA   ║  $ 1.50   ║".center(columns))

print("║═══════════║═══════════║".center(columns))

print("║   PEPSI   ║  $ 2.20   ║".center(columns))

print("║═══════════║═══════════║".center(columns))

print("║  LIPTON   ║  $ 2.25   ║".center(columns))

print("║═══════════║═══════════║".center(columns))

print("║  SUNKIST  ║  $ 1.75   ║".center(columns))

print("║═══════════║═══════════║".center(columns))

print("║   CRUSH   ║  $ 2.15   ║".center(columns))

print("║═══════════║═══════════║".center(columns))

print("║   7UP     ║  $ 2.55   ║".center(columns))

print("⊹˚₊╚═══════════════════════╝‧₊˚⊹".center(columns))


#  In this part. When the user enters a beverage, the quantity and price of the selected beverage will be displayed.

def money_transactions():

    item_Beverages = input("🗨  You will need to enter the name of the beverage here! ➔".center(columns))
    
    item_quantity = int(input("Enter the quantity here! ➔ ".center(columns)))
    
    if item_Beverages in Beverages:
        
        price = Beverages[item_Beverages]

        total_price = item_quantity * price

        print("Beverages ⊹ ࣪ ˖:".center(columns))

        print(f"{item_Beverages}".center(columns))

        print("Quantity ⊹ ࣪ ˖:".center(columns))

        print(f"{item_quantity}".center(columns))

        print("Price ⊹ ࣪ ˖:".center(columns))

        print(f"${total_price:.2f}".center(columns))

        user_amount = float(input("Enter the amount of money: ".center(columns)))

        if user_amount >= total_price:

            change = user_amount - total_price

            print(f"Thank you so much for purchasing ๋࣭⭑!".center(columns))

            print(f"Transaction complete ☺✓! Your change is ${change:.2f}".center(columns))

            return True
        
        #  Upon entering the correct answer, the following message will appear: "Transaction complete ☺✓! Your change is $"

        #  If the user has a limited amount of money or chooses to enter less than 1 or 0, the message will appear as follows: "Not enough money ✗!"

        #  Finally, if the user inserts an item code that does not appear in the final output. this message will appear instead: "Invalid item code ☹!"

        else:

            print("Not enough money ✗! Sorry!".center(columns))

    else:

        print("Invalid item code ☹!".center(columns))

    return False

while True:

        print(Introduction.center(columns))

        if not money_transactions():

            break

    