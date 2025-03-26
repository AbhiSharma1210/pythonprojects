items = ["apple", "banana", "orange", "apple", "mango", "mango", "Dragon fruit", "banana", "grapes"]
duplicates = []
for item in items:
    if items.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
if not duplicates: # A more pythonic way to check if a list is empty
    print("No duplicates")
else:
    print(f"Duplicates are: {', '.join(duplicates)}")
