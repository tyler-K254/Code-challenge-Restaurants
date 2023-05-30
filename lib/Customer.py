class Customer:
    customers = []

    #Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.customers.append(self)

    #returns the customer's given name
    def given_name(self):
        return self.given_name
    
    #returns the customer's family name
    def family_name(self):
        return self.family_name
    
    #full name
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    # Return all customer instances
    @classmethod
    def all(cls):
        return cls.customers  
