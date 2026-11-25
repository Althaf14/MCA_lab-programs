import math
import random
import datetime
import os


print("--- 1. Math Module ---")
print("Square root of 144:", math.sqrt(144))
print("Factorial of 5:", math.factorial(5))
print("Value of Pi:", math.pi)


print("\n--- 2. Random Module ---")
print("Random float between 0 and 1:", random.random())
print("Random integer between 1 and 10:", random.randint(1, 10))

colors = ["Red", "Green", "Blue", "Yellow"]
print("Randomly chosen color:", random.choice(colors))

print("\n--- 3. Datetime Module ---")
current_time = datetime.datetime.now()
print("Current Date & Time:", current_time)
print("Formatted Date:", current_time.strftime("%B %d, %Y"))

print("\n--- 4. OS Module ---")
print("Current Working Directory:", os.getcwd())
print("Operating System Name:", os.name)
