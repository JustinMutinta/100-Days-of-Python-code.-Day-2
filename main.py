print("Welcome to the tip Calculator")
amount = input("What was the total bill? $")
tip = input("What percentage tip would you like to tip? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

float_amount = float(amount)
int_people = int(people)
int_tip = (int(tip) / 100) * float_amount

result = round((float_amount + int_tip) / int_people , 2)
print(f"Each person should pay: ${result}")

