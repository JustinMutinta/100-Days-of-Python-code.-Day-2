print("Welcome to the tip Calculator")                                      #Welcoming print output
amount = input("What was the total bill? $")                                #Get the total bill from the user
tip = input("What percentage tip would you like to tip? 10, 12, or 15? ")   #Get the tip amount
people = input("How many people to split the bill? ")                       #How many people were involved

float_amount = float(amount)                                                #Change amount value to float for the decimal point
int_people = int(people)                                                    #Change people to int
int_tip = (int(tip) / 100) * float_amount                                   #Change tip to int

result = round((float_amount + int_tip) / int_people , 2)                   #Calculate the result for each person
print(f"Each person should pay: ${result}")                                 #Display Output

