# list = used to store multiple items in a single variable

food = ["pizza", "hamburguer", "hotdog", "spaghetti"]
print(food[0])
food[-1] = "rice"
print(food)
food.append("beans")
food.pop() 
food.insert(0, "meat")
for foods in food:
    print(foods)