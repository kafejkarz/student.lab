





class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        
    
    def new_name(self):
        self.name = "Mike"
        
    def new_cohort(self):
        self.cohort = "G21"    

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, Python):
        return "I love Python"
         


