shopping_list = list()

print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
  new_item = input("> ")
  
  if new_item == 'DONE':
    break
    
  shopping_list.append(new_item)
  print("Added! List has {} items.".format(len(shopping_list)))
  continue
  
print("Here's your list:")

for item in shopping_list:
  print(item)
  