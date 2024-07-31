# A PROGRAM THAT LETS YOU 'add', 'remove ', 'mark' ITEMS as purchased

grocery_list = []

def create_list():
    print("A list has been created to track your shopping list!")


def add():
    while True:
        user_input = input("type the item you would like to add: ")
        try:
            item = str(user_input)
            print(f"you included an item: {item}")
            grocery_list.append(item)   # include item at last index
            break
        except ValueError:
            print(f"the {item} is invalid, please try again.")

def remove():
    while True:
        user_input = input("type the item you would like to remove: ")
        try:
            item = str(user_input)
            print(f"you removed an item: {item}")
            grocery_list.remove(item)   # search and remove an item
            break
        except ValueError:
            print(f"the {item} is either not on the list, please try again.")


print(grocery_list)
add()
print(grocery_list)
remove()
print(grocery_list)
