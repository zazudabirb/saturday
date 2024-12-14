import json
import random 

with open ("ages.json", "r") as file:
    ages = json.load(file)

print("Welcome to the time machine!")
print("Travel to any point in time and experience life")
print("Type th name of a period in time or tye exit to leave")
print("Avalible time periods: ")

for time_period in ages.keys():
    print(f" - {time_period}")


while True:
    user_choice = input("where would you like to go? ")

    if user_choice == "exit":
        print("Exiting the time machine")
        break  
    elif user_choice in ages:
        print(f"you have traveled to the {user_choice}!")

        selected_age = ages[user_choice]
        invention = random.choice(selected_age["Inventions"])
        major_event =  random.choice(selected_age["Major Events"])
        dily_life =  random.choice(selected_age["Daily Life"])

        print(f" - notable invention: {invention}")
        print(f" - major historical event: {major_event}")
        print(f" - what dily_life was like: {dily_life}")
        print("---------------------------------------------")

    
    else:
        print("invalid time period lease choose agian")