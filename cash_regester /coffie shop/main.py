Espresso_price = 2.50
Americano_price = 3.00
Latte_price = 2.50
cappucchino_price = 3.00
macchitao_price = 2.50
Mocha_price = 3.50
Flat_white_price = 2.50
small_price = 0.00
medium_price = 0.50
large_price = 1.00


price = 0
size = input("would you like a small medium or large")
if size.upper() == "SMALL":
    price = price + small_price
elif size.upper() == "MEDIUM":
    price = price + medium_price
else:
    price = price + large_price

drinks = input("what drink would you like? we have Espresso Americano Latte cappucchino macchitao Mocha Flat white")
if drinks.upper() == "ESPRESSO":
    price = price + Espresso_price
elif drinks.upper() == "AMERICANO":
    price = price + Americano_price 
elif drinks.upper() == "LATTE":
    price = price + Latte_price
elif drinks.upper() == "CUPPUCCHINO":
    price = price + cappucchino_price
elif drinks.upper() == "MACCHITAO":
    price = price + macchitao_price
elif drinks.upper() == "MOCHA":
    price = price + Mocha_price
elif drinks.upper() == "FLAT WHITE":
    price = price + Flat_white_price

print("your total is $" +str(price))