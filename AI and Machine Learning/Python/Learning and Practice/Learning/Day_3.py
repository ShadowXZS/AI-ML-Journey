#Randomisation and Python Lists 
#Random Module 
#Python Uses Mersenne Twister 
#Need to import rand
import random

random_integer = random.randint(1,10)
print(random_integer)
#Modules, Are like Bricks in a House 
#How to create own Module 
#Import Python_File_Name.. To use it Python_File_Name.Function
random_float = random.random() * 10
print(random_float)
#Can use Multiplication To Increase the Number 
random_floatone = random.uniform(1,10)
print(random_floatone)
#Recomended to use random.random.
#Python List : Data Structure 
# variable = ["item 1", "item 2"] :> Lists 
# Order is Important, 
states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa"]
print(states_of_india[0])
#[] Likely Lists , Can use Negative Index -1 , Stats counting from the last 
#To Modify variable_where_the_list_is_stored[Index of the Item you Want to change ] = "Modified Item", Can be used to Modify the Items on the list 
states_of_india[0] = "Andhra Pradesh (AP)"
#To Append a List variable_where_list_is_stored.append(Item to be Added), This will add Item to a List. 
states_of_india.append("Karnataka")
#To Extend the List variable_where_list_is_stored.extend(["Item1, ItemN"]), This can add any number of items to the list. 
#You can also use Len Fucntion on List to find how many items are there on the list. 
#Random Item from List : random.choice(variable)
#Index Errors and Working with Nested Lists 
# Index Out of Range Error, : Common Error When you Index Something out of the List 
# Nested List Variable = [variable of list 1 , variable of list n]

