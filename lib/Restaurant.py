from Review import Review

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
    
    # restaurant review
    def reviews(self):
        return [review for review in Review.all() if review.restaurant() == self] 

    def customers(self):
        return list(set([review.customer() for review in self.reviews()]))
    
    def average_star_rating(self):
        ratings = [review.rating() for review in self.reviews()]
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return None
 
    
  

    