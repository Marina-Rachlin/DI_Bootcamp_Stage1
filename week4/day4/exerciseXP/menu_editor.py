from menu_item import MenuItem
from menu_manager import MenuManager


# add_item_to_menu() - this function should ask the user to input the item’s name and price. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was added successfully print a message which states: item was added successfully.

def add_item_to_menu():
    name = input("Enter the item's name: ").capitalize()
    price = input("Enter the item's price: ")

    # Validate if the price is an integer
    try:
        price = int(price)
    except ValueError:
        print("Invalid price. Price must be an integer.")
        return
    
    item = MenuItem(name, price)
    try:
        item.save()
        print("Item was added successfully.")
    except Exception as e:
        print(str(e))


# remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was deleted successfully – print a message to let the user know this was completed.
def remove_item_from_menu():
    name = input("Enter the item's name to be removed: ").capitalize()

    item = MenuItem(name, None)
    try:
        if item.delete():
            print("Item was deleted successfully.")
        else:
            print("Item does not exist.")
    except Exception as e:
        print(str(e))


# update_item_from_menu()- this function should ask the user to input the name and price of the item they want to update from the restaurant’s menu, as well as to input the name and price they want to change them with. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was updated successfully – print a message to let the user know this was completed.
def update_item_from_menu():
    current_name = input("Enter the name of the item you want to update: ").capitalize()
    current_price = input("Enter the price of the item you want to update: ")
    new_name = input("Enter the new name for the item: ")
    new_price = input("Enter the new price for the item: ")

    try:
        current_price = int(current_price)
    except ValueError:
        print("Invalid current price. Price must be an integer.")
        return

    try:
        new_price = int(new_price)
    except ValueError:
        print("Invalid new price. Price must be an integer.")
        return

    item = MenuItem(current_name, current_price)
    try:
        item.update(new_name, int(new_price))
    except Exception as e:
        print(str(e))



# show_restaurant_menu() - print the restaurant’s menu.
def show_restaurant_menu():
    try:
        menu_items = MenuManager.all()
        if menu_items:
            print("Restaurant Menu:")
            for item in menu_items:
                name, price = item
                print(f"- {name}: ${price}")
        else:
            print("The restaurant menu is empty.")
    except Exception as e: 
        print(str(e))




def show_user_menu():
    while True:
        print("Program Menu:")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("Q - Quit the program")

        choice = input("Enter your choice: ").upper()

        if choice == "V":
            view_item()
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "Q":
            break
        else:
            print("Invalid choice. Please try again.")

def view_item():
    name = input("Enter the name of the item to view: ")
    item = MenuManager.get_by_name(name)
    if item is not None:
        print("Item found:")
        print("Name:", item[0][0])
        print("Price:", item[0][1])
        print (item)
    else:
        print("Item not found.")

show_user_menu()        




 
