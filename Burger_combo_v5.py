"""Burger combo program use to store a quick menu of combo meals v5
develop the delete_combo function to delete a combo meal from the dictionary
Created by Qingxiao
"""
# pylint: disable = W0621, W0612, C0103, C0206

combos = {
         "Value": {
             "Combo name": "Value",
             "Combo items": [
                 {"Item": "Beef burger", "Price": 5.69},
                 {"Item": "Fries", "Price": 1.00},
                 {"Item": "Fizzy drink", "Price": 1.00}
             ]
         },
         "Cheezy": {
             "Combo name": "Cheezy",
             "Combo items": [
                 {"Item": "Cheeseburger", "Price": 6.69},
                 {"Item": "Fries", "Price": 1.00},
                 {"Item": "Fizzy drink", "Price": 1.00}
             ]
         },
         "Super": {
             "Combo name": "Super",
             "Combo items": [
                 {"Item": "Cheeseburger", "Price": 6.69},
                 {"Item": "Large fries", "Price": 2.00},
                 {"Item": "Smoothie", "Price": 2.00}
             ]
         }
     }

all_items = {
    "Beef burger": 5.69,
    "Fries": 1.00,
    "Fizzy drink": 1.00,
    "Cheeseburger": 6.69,
    "Large fries": 2.00,
    "Smoothie": 2.00
}

def add_combo(all_items):
    # Show all available items
    for i, (item_name, price) in enumerate(all_items.items(), 1):
        print(f"{i}. {item_name} (${price:.2f})")
    # Make sure the input is out of the loop
    combo_name = input("\nEnter combo name: ").strip()
    # Check if the combo already exists
    if combo_name in combos:
        if input("Combo exists! Overwrite? (y/n): ").lower() != 'y':
            return
    selected_items = []
    while True:
        choice = input("Enter item number (0 to finish): ").strip()
        if choice == "0":
            if not selected_items:  # No items selected
                print("Must select at least 1 item!")
                continue
            break
        try:
            index = int(choice) - 1
            item = list(all_items.items())[index]
            selected_items.append({"Item": item[0], "Price": item[1]})
        except (ValueError, IndexError):
            print("Invalid input")

    # Add the combo to the dictionary
    combos[combo_name] = {
        "Combo name": combo_name,
        "Combo items": selected_items
    }
    print(f"\nNew Combo {combo_name} created successfully. Details:")
    print(f"[{combo_name}]The combo contains:")
    total = 0.0
    for item in selected_items:
        print(f"▫ {item['Item']} (${item['Price']:.2f})")
        total += item["Price"]
    print(f"Total price: ${total:.2f}\n")
    return combos

def find_combo(combos, search_input):
    """Find combo meal based on user input"""
    found_combo = [
        combo for combo in combos.values() if combo["Combo name"].lower() == search_input.lower()
    ]#Find combo based on user input

    if found_combo:
        for combo in found_combo:
            print(f"Combo name: {combo['Combo name']}")
            for item in combo["Combo items"]:
                print(f"{item['Item']} - {item['Price']:.2f}")
            print()
    else:
        print("No combo meal found.")

def delete_combo():
    """Delete a combo meal from the dictionary"""
    search_term = input("\nEnter combo name to delete: ").strip()
    matched_key = None
    target_combo = None
    for combo_key in combos:
        if combo_key.lower() == search_term.lower():
            matched_key = combo_key
            target_combo = combos[combo_key]  # Save the target combo for deletion
            break
    if not all([matched_key, target_combo]):
        print(f"No combo named '{search_term}' found")
        return
    # Output the target combo for confirmation
    print(f"\n--- [ {target_combo['Combo name']} ] ---")
    total = sum(item["Price"] for item in target_combo["Combo items"])
    for item in target_combo["Combo items"]:
        print(f"{item['Item']} (${item['Price']:.2f})")
    print(f"Total: ${total:.2f}\n")
    # Ask for confirmation before deletion
    if input(f"Confirm delete {matched_key}? (y/n): ").lower() == 'y':
        del combos[matched_key]
        print(f"Combo '{matched_key}' successfully deleted\n")
    else:
        print("Deletion cancelled\n")


def Output_all(combos):
    """Output all available combos"""
    if combos:
        message = "Here are all the available combos:\n\n"
        for combo_id, combo in combos.items():
            items_str = "\n".join([
                f"    {i+1}. {item['Item']} (${item['Price']:.2f})"
                for i, item in enumerate(combo['Combo items'])
            ])  # Create a string of items
            total_price = sum(item["Price"] for item in combo["Combo items"])# Calculate total price
            message += (
                f"Combo ID: {combo_id}\n"
                f"Name: {combo['Combo name']}\n"
                f"Total Price: ${total_price:.2f}\n"
                f"Includes:\n{items_str}\n"
                f"{'-' * 30}\n"
            )
        print(message)
#main routine


choice = ""
while choice != "5":
    print("What would you like to do?")
    print()
    print("1. Add a combo")
    print("2. Find a combo")
    print("3. Delete a combo")
    print("4. Output all combos")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_combo(all_items)

    elif choice == "2":
        search_input = input(
            "\nEnter the name of the combo you want to find (e.g. Value, Cheezy, Super): "
        ).strip()
        find_combo(combos, search_input)

    elif choice == "3":
        delete_combo()

    elif choice == "4":
        Output_all(combos)

    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid choice, please try again.")
