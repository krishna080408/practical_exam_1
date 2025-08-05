def inventory_products():
    print("Welcome to data of products!\n")
    items = []

    while True:
        item_name = input("Enter product name: ").strip()
        item_category = input("Enter product category: ").strip().lower()
        quantity = int(input("Enter product quantity: "))

        items.append({
            'name': item_name,
            'category': item_category,
            'quantity': quantity
        })

        cont = input("\nDo you want to add more products? (y/n): ").lower()
        if cont != 'y':
            break

    print("\n========== PRODUCT SUMMARY ==========")

    total_items = len(items)
    print(f"\nTotal Different Items: {total_items}")
    item_names = [item['name'] for item in items]
    print(f"Explanation: You entered {total_items} different items: {', '.join(item_names)}.")

    total_quantity = sum(item['quantity'] for item in items)
    print(f"\nTotal Quantity in Stock: {total_quantity}")
    quantities = " + ".join(str(item['quantity']) for item in items)
    print(f"Explanation: Sum of all quantities: {quantities} = {total_quantity}")


    average = total_quantity / total_items
    print(f"\nAverage Quantity per Item: {average:.2f}")
    print(f"Explanation: Average = {total_quantity} total / {total_items} items")


    most_stocked = max(items, key=lambda x: x['quantity'])
    least_stocked = min(items, key=lambda x: x['quantity'])

    print(f"\nMost Stocked Item: {most_stocked['name']} ({most_stocked['quantity']} units)")
    print(f"Explanation: {most_stocked['name']} has the highest quantity among all items.")

    print(f"\nLeast Stocked Item: {least_stocked['name']} ({least_stocked['quantity']} units)")
    print(f"Explanation: {least_stocked['name']} has the lowest quantity.")

  
    categories = {item['category'] for item in items}
    print(f"\nUnique Categories in Inventory: {categories}")
    print("Explanation: Categories are taken from user input and converted to lowercase.\nNo duplicates are shown here.")


    sorted_items = sorted(items, key=lambda x: x['quantity'], reverse=True)
    print("\nItems Sorted by Quantity (High to Low):")
    for idx, item in enumerate(sorted_items, 1):
        print(f"{idx}. {item['name']} - {item['quantity']} units")
    print("\nExplanation: Items are sorted using the quantity field from highest to lowest.")


    sorted_categories = sorted(categories)
    print("\nCategories in Alphabetical Order:")
    for idx, cat in enumerate(sorted_categories, 1):
        print(f"{idx}. {cat}")
    print("\nExplanation: The set of unique categories was sorted alphabetically for display.")

    print("\n========== END OF DATA REPORT ==========")



inventory_products()
'''
Welcome to data of products!

Enter product name: choco-bar
Enter product category: ice food
Enter product quantity: 1

Do you want to add more products? (y/n): n

========== PRODUCT SUMMARY ==========

Total Different Items: 1
Explanation: You entered 1 different items: choco-bar.

Total Quantity in Stock: 1
Explanation: Sum of all quantities: 1 = 1

Average Quantity per Item: 1.00
Explanation: Average = 1 total / 1 items

Most Stocked Item: choco-bar (1 units)
Explanation: choco-bar has the highest quantity among all items.

Least Stocked Item: choco-bar (1 units)
Explanation: choco-bar has the lowest quantity.

Unique Categories in Inventory: {'ice food'}
Explanation: Categories are taken from user input and converted to lowercase.
No duplicates are shown here.

Items Sorted by Quantity (High to Low):
1. choco-bar - 1 units

Explanation: Items are sorted using the quantity field from highest to lowest.

Categories in Alphabetical Order:
1. ice food

Explanation: The set of unique categories was sorted alphabetically for display.

========== END OF DATA REPORT ==========


'''
