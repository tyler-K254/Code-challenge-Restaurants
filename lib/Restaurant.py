class Restaurant:
    # Class variable to store all restaurant instances
    all_restaurants = [] 

     #Restaurants should be initialized with a name, as a string
    def __init__(self, name):
        self.name = name
        Restaurant.all_restaurants.append(self)

     #returns the restaurant's name 
    def name(self):
        return self.name
    
  

    