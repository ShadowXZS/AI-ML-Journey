#Coin Flipper, Generates Heads or Tails. 
import random

random_coin = random.randint(0,1)
if random_coin == 1:
    print("Heads")
else:
    print("Tails")