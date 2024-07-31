# A PROGRAM THAT LETS YOU 'add', 'remove' items as purchased

def create_list():
    shopping_list = []
    size_of_list = len(shopping_list)

    if size_of_list < 1:
        print("A list has been created to track your shopping list!")
        return shopping_list
    else:
        print(shopping_list)

def add(shopping_list):
    while True:
        user_input = input("type the item you would like to add: ")
        try:
            item = str(user_input)
            print(f"you included an item: {item}")
            shopping_list.append(item)   # include item at last index
            break
        except ValueError:
            print(f"the {item} is invalid, please try again.")

def remove(shopping_list):
    while True:
        user_input = input("type the item you would like to remove: ")
        try:
            item = str(user_input)
            print(f"you removed an item: {item}")
            shopping_list.remove(item)   # search and remove an item
            break
        except ValueError:
            print(f"the {item} is either not on the list, please try again.")


my_list = create_list()
add(my_list)
remove(my_list)
