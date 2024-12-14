import random

pet_names = ["Luna", "Milo", "Bella", "Max", "Daisy", "Charlie", "Stella", "Finn", "Lola", "Rosie", "Ollie", " Flounder", "Caramel", "Apollo", "Barbie", "Wesley", "Cookie", "Ender", "Zoro"]
pet_species = ["puppy", "kitten", "bunny", "snake", "turtle", "parrot"]
pet_traites = ["only eats mac and cheese", "dose not like humans", "yaps all day", "trips over nothing", "scared of the color brown"]


#this stores the users pets
user_collection = []


def generate_mystery_pet():
    Name = random.choice(pet_names)
    Species = random.choice(pet_species)
    Traites = random.choice(pet_traites)

    pet = {
        "Name": Name,
        "Species": Species, 
        "Traites": Traites,
    }
    return pet




def display_pet(pet):
    print("Mystery pet details")
    print("Name: " + pet["Name"])
    print("Species: " + pet["Species"])
    print("Traites: " + pet["Traites"])

def Mystery_pet_shop():
    print("welcome to the Mystery_pet_shop")

    while True:
        action = input("would you like to exit")
        if action == "exit" :
            print("thanks fo visiting")
            break
        elif action == "buy":
            pet = generate_mystery_pet()
            display_pet(pet)

            decision = input("would you like to buy? yes or no")

            if decision = "yes":
                user_collection.append
                print(pet["Name"] + "was added to your cart")
            else:
                print("no worries, lets try another pet")
        else:
            print("exit or buy")





My_pet = generate_mystery_pet()
display_pet(My_pet)
#print(My_pet)