class Store:
    def __init__(self, name, item, location):
        self.name = name
        self.item = item 
        self.location = location
        
my_store = Store("Matcha Verde","Matcha", "Nashville, TN" )


class Matcha:
    def __init__(self,name, ranking, grams, taste, season_available, price):
        self.name = name
        self.ranking = ranking
        self.grams = grams
        self.taste = taste
        self.season_available = season_available
        self.price = price
        
seasons = ["Fall", "Summer", "Winter", "Spring"]

my_matcha = Matcha("Hatsu", 8, "40g", "Astrigent",seasons[1], 25.00)
my_matcha2 = Matcha("Hatsu", 8, "40g", "Astrigent",seasons[2], 10.00)
my_matcha3 = Matcha("Waikiki", 6, "40g", "Astrigent",[seasons[0], seasons[3]], 46.00)


print(f"I just ordered 160g of {my_matcha.name} matcha")
        
class User:
    def __init__(self, first_name,money, current_season):
        self.first_name = first_name
        self.money = money
        self.current_season = current_season
        
user = User("Leya", 100.00, "Winter")
print(f"{user.first_name} spent ${user.money:,.2f} on this {user.current_season} matcha season. ")


        
    # def buy_matcha(self, money, current_season):
    #     pass
    
    
# class Work:
#     def __init__(self, hours, wage):
#         self.hours = hours
#         self.wage = wage
        
