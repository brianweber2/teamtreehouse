shopping_list = []


def remove_item(idx):
  index = idx - 1
  item = shopping_list.pop(index)
  print("Removed {}.".format(item))
  
def clear_list():
  shopping_list.clear()
  print("\nShopping list is cleared!")
  
def move_item(old_index,new_index):
  item = shopping_list.insert(new_index, shopping_list.pop(old_index))

def show_help():
  print("\nSeparate each item with a comma.")
  print("Type DONE to quit, SHOW to see the current list, REMOVE to delete an item, MOVE an item and HELP to get this message.")
  
  
def show_list():
  count = 1
  for item in shopping_list:
    print("{}: {}".format(count, item))
    count += 1
    
print("Give me a list of things you want to shop for.")
show_help()

while True:
  new_stuff = input("> ")
  
  if new_stuff == "DONE":
    print("\nHere's your list: ")
    show_list()
    break
  elif new_stuff == "HELP":
    show_help()
    continue
  elif new_stuff == "SHOW":
    show_list()
    continue
  elif new_stuff == "REMOVE":
    show_list()
    idx = input("Which item? Tell me the number.")
    remove_item(int(idx))
  elif new_stuff == "CLEAR":
    clear_list()
    continue
  elif new_stuff == "MOVE":
    if len(shopping_list) == 0:
      print("\nThere are no items in your shopping list.")
      show_help()
    else:
      show_list()
      idx_old = input("\nGive me the number of the item you want to move: ")
      old_index = int(idx_old) - 1
      idx_new = input("\nWhere do you want to place the " + shopping_list[old_index] + "?")
      # or idx_new = input("\nWhere do you want to place the {}?".format(shopping_list[old_index]))
      new_index = int(idx_new) - 1
      move_item(old_index, new_index)
  else:
    new_list = new_stuff.split(",")
    index = input("Add this at a certain spot? Press enter for the end of the list, or give me a number, Currently {} items in the list.".format(len(shopping_list)))
    if index:
      try:
        spot = int(index) - 1
        for item in new_list:
          shopping_list.insert(spot, item.strip())
          spot += 1
      except:
        print("\nCan only accept a number. Currently there are {} items in the shopping list".format(len(shopping_list)))
    else:
      for item in new_list:
        shopping_list.append(item.strip())