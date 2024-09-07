file = open("Olympic.csv", "r")


for line in file:
    data = line.split(",")
    year = data[0]
    city = data[1] 
    country = data[2]
    season = data[3]


    # if country == "United States":
    #     print (city + " hosted the " + season + " Olympics in " + year)
    # if season == "winter":
    #   print (city + " hosted the " + season + " Olympics in " + year)
 
    if year == 2010:
   print (city + " hosted the " + season + " Olympics in " + year - 2010)