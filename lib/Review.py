class Review:
    all_reviews = []
     
     #Reviews should be initialized with a customer, restaurant, and a rating (a number)
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
    
    #returns the rating for a restaurant.
    def rating(self):
        return self.rating
    
    #Return the list of all review instances
    @classmethod
    def all(cls):
        return cls.all_reviews  
    
    #returns customer
    def customer(self):
        return self.customer
    
    #returns the restaurant
    def restaurant(self):
        return self.restaurant

