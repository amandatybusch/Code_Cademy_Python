#CODECADEMY_LISTS

#LISTS_GRADEBOOK_PROJECT_FROM_CODECADEMY

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create a list called subjects and fill it with the classes you are taking: "physics" "calculus" "poetry" "history"
subjects = ["physis", "calculus", "poetry", "history"]

#Create a list called grades and fill it with your scores: 98 97 85 88
grades = [98, 87, 85, 88]

#Manually (without any methods) create a two-dimensional list to combine subjects and grades.
gradebook = [
  ["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]
]
print (gradebook)

#Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook
gradebook.append(["computer science", 100])
print (gradebook)

#Use append to add ["visual arts", 93] to gradebook.
gradebook.append(["visual arts", 93])
print (gradebook)

#Access the index of the grade for your visual arts class and modify it to be 5 points greater.
gradebook[-1][-1] += 5
print (gradebook)

#Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it. 
gradebook[2].remove(85)
#Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.
gradebook[2].append("Pass")
print (gradebook)

#Create a new variable that combines both last_semester_gradebook and gradebook using + to have one complete grade book.
full_gradebook = last_semester_gradebook + gradebook
print (full_gradebook)


#WORKING_WITH_LISTS_REVIEW

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Jiho has compiled a list of inventory items into a list called inventory. How many items are in the warehouse?
inventory_len = len(inventory)

#Select the first element in inventory. Save it to a variable called first.
first = inventory[0]

#Select the last element from inventory. Save it to a variable called last.
last = inventory[-1]

#Select items from the inventory starting at index 2 and up to, but not including, index 6. Save your answer to a variable called inventory_2_6.
inventory_2_6 = inventory[2:6]

#Select the first 3 items of inventory. Save it to a variable called first_3.
first_3 = inventory[0:3]

#How many 'twin bed's are in inventory? Save your answer to a variable called twin_beds.
twin_beds = inventory.count("twin bed")

#Remove the 5th element in the inventory. Save the value to a variable called removed_item.
removed_item = inventory.pop(4)

#Use the .insert() method to place "19th Century Bed Frame" as the 11th element in our inventorY.
inventory.insert(10, "19th Century Bed Frame")

#Sort inventory using the .sort() method or the sorted() function.
inventory.sort()
print (inventory)


#LISTS_LENS_SLICE_PROJECT_FROM_CODECADEMY

#To keep track of the kinds of pizzas you sell, create a list called toppings.
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchoives", "mushrooms"]

#To keep track of how much each kind of pizza slice costs, create a list called prices
prices = [2, 6, 1, 3, 2, 7, 2]

#Your boss wants you to do some research on $2 slices.
num_two_dollar_slices = prices.count(2)
print (num_two_dollar_slices)

#Find the length of the toppings list and store it in a variable called num_pizzas.
num_pizzas = len(toppings)
print (num_pizzas)

#Print the string We sell [num_pizzas] different kinds of pizza!
print ("We seel " + str(num_pizzas) + " different kinds of pizza!")

#Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.
pizza_and_prices = [
  [2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2,"mushrooms"]
]
print (pizza_and_prices)

#Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
pizza_and_prices.sort()
print (pizza_and_prices)

#Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheapest_pizza = pizza_and_prices[0]
print (cheapest_pizza)

#Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza = pizza_and_prices[-1]
print (priciest_pizza)

#It looks like the most expensive pizza was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.remove([7, "anchovies"])
print (pizza_and_prices)

#pizza_and_prices.pop(-1)
#print (pizza_and_prices)

#Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers"
pizza_and_prices.insert(4, [2.5, "peppers"])
print (pizza_and_prices)

#pizza_and_prices.append([2.5, "peppers"])
#pizza_and_prices.sort()
#print (pizza_and_prices)

#Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest
three_cheapest = pizza_and_prices[0:3]
print (three_cheapest)


#LISTS_ZIP_FUNCTION_FROM_CODECADEMY

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

#combine owners and dogs_names lists into a zip object.
names_and_dogs_names = zip(owners, dogs_names)

#create a new variable named list_of_names_and_dogs_names by calling the list() function on names_and_dogs_names.
list_of_names_and_dogs_names = list(names_and_dogs_names)
print (list_of_names_and_dogs_names)
