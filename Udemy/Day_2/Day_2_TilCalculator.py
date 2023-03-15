# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
Bill_Total = float(
    input("Welcome to the tip cal.\nWhat was the total bill? $"))
Tip_Per = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
Num_People = int(input("How many people to split the bill? "))

Bill_Total *= (1 + Tip_Per / 100)
print(f"Each person should pay: ${round(Bill_Total / Num_People, 3)}")
