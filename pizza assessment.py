pizza_on_order = False

pizza_menu = [[ 10,"Cheese", "None", "None", "", "", "", ""], [ 14, "Hawaiian", "None", "Ham", "Pinapple", "", "", ""], [ 14, "Pepperoni", "None", "Pepperoni", "", "", "", ""], [ 16, "Meatlovers", "Barbeque", "Pepperoni", "Sausage", "Onion", "", ""], [ 16, "Chicken", "Mayonnaise", "Chicken", "Onion", "Bell Pepper", "", ""], [ 18, "Supreme", "None", "Pepperoni", "Sausage", "Mushroom", "Onion", "Bell Pepper"]]
order = []
custom_pizza_toppings = []
all_toppings = ["Ham", "Pepperoni", "Sausage", "Chicken", "Onion", "Bell Pepper", "Mushroom", "Pinapple"]

def menu_gui():
    print("Welcome to the Pizza Cabin ordering system")
    while True:
        print("")
        print("(1) | Show menu ")
        print("(2) | Order pizza")
        if not order:
            print("(3) | Leave")
        elif order:
            print("(3) | Show order")
            print("(4) | Edit order")
            print("(5) | Check out")
            print("(6) | Cancel order")
        else:
            print("Invalid input.")
        nav = input("  > ").strip()
        if nav == "1":
            show_pizza_menu()
        elif nav == "2":
            order_pizza()
        elif nav == "3":
            if not order:
                break
            elif order:
                show_order()
        elif nav == "4":
            if not order:
                print("Invalid input.")
            elif order:
                edit_order()
        elif nav == "5":
            if not order:
                print("Invalid input.")
            elif order:
                finish_order
        elif nav == "6":
            if not order:
                print("Invalid input.")
            elif order:
                order.clear()
        else:
            print("Invalid input.")

def show_pizza_menu():
    print(" Price | Pizza | Sauce | Toppings")
    for person in pizza_menu:
        print(f" ${person[0]} | {person[1]} | {person[2]} | {person[3]} {person[4]} {person[5]} {person[6]} {person[7]}")
    print("\nAll pizzas come with a tomato base sauce and cheese")

def order_pizza():
    while True:
        num = 1
        print("What pizza would you like to order?")
        print("Number | Price | Pizza ")
        for person in pizza_menu:
            print(f"({num}) | ${person[0]} | {person[1]}")
            num += 1
        print("(7) | $10+ | Custom")
        nav = input("  > ").strip()
        try:
            num = int(nav) - 1
            if 0 <= num < len(pizza_menu) or nav == 7:
                print()
        except ValueError:
            print("")
        if 0 <= num < len(pizza_menu): 
            while True:
                print(f"Would you like to add a {pizza_menu[num][1]} pizza to your order?")
                print("(1) | Yes")
                print("(2) | No")
                nav = input("  > ").strip()
                if nav == "1":
                    order.append(pizza_menu[num])
                    print(f"{pizza_menu[num][1]} pizza added to order successfully.")
                    show_order()
                    break
                elif nav == "2":
                    return ""
                else:
                    print("Invalid input.")
            break
        elif nav == "7":
            while True:
                print("Would you like to make a custom pizza?")
                print("(1) | Yes")
                print("(2) | No")
                nav = input("  > ").strip()
                if nav == "1":
                    custom_pizza()
                elif nav == "2":
                    return ""
                else:
                    print("Invalid input.")
        else:
            print("Invalid input.")


def custom_pizza():
    if custom_pizza_toppings:
        custom_pizza.clear()
    custom_pizza_toppings.append(10)
    custom_pizza_toppings.append("Custom")
    while True:
        print("What sauce would you like to add to your pizza? (pizza already has a tomato base sauce)")
        print("(1) | Barbeque")
        print("(2) | Mayonnaise")
        print("(3) | None")
        nav = input("  > ").strip()
        if nav == "1":
            custom_pizza_toppings.append("Barbeque")
            custom_pizza_toppings[0] += 1
            break
        elif nav == "2":
            custom_pizza_toppings.append("Mayonnaise")
            break
        elif nav == "3":
            custom_pizza_toppings.append("None")
            break
        else:
            print("Invalid input.")
    while True:
        print("What is the first topping you would like to add?")
        num = 1
        topping_num = 0
        for person in all_toppings:
            print(f"({num}) | {all_toppings[topping_num]}")
            num += 1
            topping_num += 1
        nav = input("  > ").strip()
        num = int(nav) - 1
        try:
            num = int(nav) - 1
            if 0 <= num < len(pizza_menu):
                print()
        except ValueError:
            print("Invalid input.")
        if 0 <= num < len(all_toppings): 
            custom_pizza_toppings.append(all_toppings[num])
            print(custom_pizza_toppings)


        

    
def show_order():
    print("Would you like to see your current order?")
    print("(1) | Yes")
    print("(2) | No")
    nav = input("  > ").strip()
    while True:
        if nav == "1":
            print(" Price | Pizza ")
            for person in order:
                print(f" ${person[0]} | {person[1]}")
            break
        elif nav == "2":
            return ""
        else:
            print("Invalid input.")

def edit_order():
    print()

def finish_order():
    print()

menu_gui()

