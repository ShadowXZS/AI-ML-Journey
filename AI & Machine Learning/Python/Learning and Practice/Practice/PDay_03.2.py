#Who Will pay the Bill 
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
friends_index = len(friends)
who_pays = random.randint(0,friends_index-1)
print(friends[who_pays]+", Pays the Bill.")
# This will print who pays the bill, Even if some one joins the friends group. 
# Alternative Solution, Found this after watching the solution. 
print(random.choice(friends))