import random


first_names = ["Artemis" ,"Bastian" ,"Anakin" ,"Draco" ,"aragorn" ,"Albus","Caspian"]
last_names = ["Solace" ,"skywalker" ,"Malfoy" ,"Percival" ,"Wulfric" ,"Brian","Dumbledore"]
species = ["Mermaid" ,"fairy" ,"spider" ,"Centaurs" ,"orc" ,"gnome" ,"elf"]
powers =  ["water" ,"Ice" ,"air" ,"fire" ,"lava" ,"meatal" ,"earth"]



first_name = random.choice(first_names)
last_name = random.choice(last_names)
email = first_name + "." + last_name + "@elf-mail.santa"
Species = random.choice(species)
power = random.choice(powers)

print(first_name)
print(last_name)
print(Species)
print(power)
print(email)