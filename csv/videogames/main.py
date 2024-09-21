file = open ("videogames.csv", "r")

def display_games():
    for line in file:
        data = line.split(",")

        title = data [0]
        release_year = data [1]
        genre = data [2]
        developer =  data [3]
        platform = data[4]
        print(platform)

        print("Title: " + title)
        print("Release_year: " + release_year)
        print("genre: " + genre)
        print("developer: " + developer)
        print("platform: " + platform)
        print()

def list_games_by_year():
    year = input("what year are youu intrested in?")
 
    for line in file:
        data = line.split(",")

        title = data [0]
        release_year = data [1]
        genre = data [2]
        developer =  data [3]
        platform = data[4]
       
       
        if year == release_year:
            print("Title: " + title)
            print("Release_year: " + release_year)
            print("genre: " + genre)
            print("developer: " + developer)
            print("platform: " + platform)
            print()

def list_games_by_developer():
    dev = input("what developer are you intrested in?")
 
    for line in file:
        data = line.split(",")

        title = data [0]
        release_year = data [1]
        genre = data [2]
        developer =  data [3]
        platform = data[4]
       
        if dev.lower() == developer.lower():
            print("Title: " + title)
            print("Release_year: " + release_year)
            print("genre: " + genre)
            print("developer: " + developer)
            print("platform: " + platform)
            print()

def list_games_by_genre():
    genre = input("what genre are you intrested in?")
 
    for line in file:
        data = line.split(",")

        title = data [0]
        release_year = data [1]
        Genre = data [2]
        developer =  data [3]
        platform = data[4]
       
       
        if genre == Genre:
            print("Title: " + title)
            print("Release_year: " + release_year)
            print("genre: " + genre)
            print("developer: " + developer)
            print("platform: " + platform)
            print()

def list_games_before_year():
    user_year = int(input("Enter a year:"))
    
    with open("videogames.csv","r") as file:
        next(file)
        
        for line in file:
            data = line.split(",")

            title = data [0]
            release_Year = data [1]
            Genre = data [2]
            developer =  data [3]
            platform = data[4]
        
        
            if int(release_Year) <= user_year:
                print("Title: " + title)
                print("Release_year: " + release_Year)
                print("genre: " + Genre)
                print("developer: " + developer)
                print("platform: " + platform)
                print()     

def list_games_by_platform():
    user_Platform = input("Enter a platform:")
    
    with open("videogames.csv","r") as file:
        next(file)
        
        for line in file:
            data = line.split(",")

            title = data [0]
            release_Year = data [1]
            Genre = data [2]
            developer =  data [3]
            platform = data[4]
        
        
            if user_Platform.lower() in platform.lower():
                print("Title: " + title)
                print("Release_year: " + release_Year)
                print("genre: " + Genre)
                print("developer: " + developer)
                print("platform: " + platform)
                print()     

#display_games()
#list_games_by_year()
#list_games_by_developer()
#list_games_by_genre()
#list_games_before_year()
list_games_by_platform()